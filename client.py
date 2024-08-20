import argparse
import os

import requests

HOST = "localhost"
PORT = 5000


def new_runner(parser: argparse.ArgumentParser):
    parser.add_argument("name", type=str, help="Name of the runner")
    parser.add_argument("path", type=str, help="Path to the runner")
    parser.add_argument("args", nargs="*", help="Arguments to pass to the runner")

    args = parser.parse_args()

    name = args.name
    path = os.path.abspath(args.path)
    args = args.args

    data = {"name": name, "path": path, "args": args}
    response = requests.post(f"http://{HOST}:{PORT}/new", json=data)
    print(response.text)


def list_runners():
    response = requests.get(f"http://{HOST}:{PORT}/list")
    print(response.text)


def delete_runner(parser: argparse.ArgumentParser):
    parser.add_argument("--idx", type=int, help="Index of the runner to delete")
    parser.add_argument("--name", type=str, help="Name of the runner to delete")

    args = parser.parse_args()

    data = {"name": args.name}
    if args.idx:
        data["idx"] = args.idx

    response = requests.post(f"http://{HOST}:{PORT}/delete", json=data)
    print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["new", "list", "delete"])
    args, _ = parser.parse_known_args()

    if args.action == "new":
        new_runner(parser)
    elif args.action == "list":
        list_runners()
    elif args.action == "delete":
        delete_runner(parser)
