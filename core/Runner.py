import subprocess

from pwn import log
from Target import Target

from core import Submitter


class Runner:
    def __init__(self, name, path, submitter, args):
        self.name = name
        self.path = path
        self.args = args
        self.submitter: Submitter = submitter

    def run(self, target: Target):
        command = [self.path, target.host, *self.args]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if stderr:
            stderr = stderr.decode().strip()
            log.error(f"Error in {self.name} on {target.host}: {stderr}")
            return

        result = stdout.decode().strip()
        
        flag = self.submitter.validate_and_get_flag(result)
        if not flag:
            log.error(f"Vailed to get lag in {self.name} on {target.host}")
            return
        
        submit_result = self.submitter.submit(flag)
        if submit_result:
            log.success(f"Flag submitted for {self.name} on {target.host} with flag {flag}")
        else:
            log.error(f"Failed to submit flag for {self.name} on {target.host}")