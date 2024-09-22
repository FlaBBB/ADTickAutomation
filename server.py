import argparse
import json
import threading
import time
from typing import List

from core.Runner import Runner
from core.Submitter import Submitter
from core.TargetPool import TargetPool
from flask import Flask, request
from pwn import log

runners: List[Runner] = []
submitter: Submitter = Submitter()

app = Flask(__name__)

def run_runners(runner):
    for server in targets:
        threading.Thread(target=runner.run, args=(server,)).start()

def runners_workers(round_time: int, targets: TargetPool):
    while True:
        log.info("Starting new round")
        for server in targets:
            for runner in runners:
                threading.Thread(target=runner.run, args=(server,)).start()
        time.sleep(round_time)


@app.route("/new", methods=["POST"])
def new_runner():
    name = request.json["name"]
    path = request.json["path"]
    args = request.json["args"]
    runner = Runner(name, path, submitter, args)
    run_runners(runner)
    runners.append(runner)
    return "Runner created"


@app.route("/list", methods=["GET"])
def list_runners():
    return json.dumps({i: runner.name for i, runner in enumerate(runners)})


@app.route("/delete", methods=["POST"])
def delete_runner():
    idx = request.json["idx"] if "idx" in request.json else None
    name = request.json["name"]

    if idx is None:
        for i, runner in enumerate(runners):
            if runner.name == name:
                idx = i
                break

    if idx is None:
        return "Runner not found"

    runners.pop(idx)

    return "Runner deleted"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", type=str, help="Host to listen on", default="localhost"
    )
    parser.add_argument("--port", type=int, help="Port to listen on", default=5000)
    parser.add_argument(
        "--round-time", type=int, help="Time to run each runner", required=True
    )
    parser.add_argument(
        "targets",
        type=str,
        help="Path of JSON file containing base targets"
    )
    args = parser.parse_args()

    host = args.host
    port = args.port
    round_time = args.round_time
    targets = TargetPool.parse_json(args.targets)

    threading.Thread(target=runners_workers, args=(round_time, targets)).start()

    log.info(f"Server started on {host}:{port}")

    app.run(host=host, port=port)
