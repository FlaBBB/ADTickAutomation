import subprocess

from pwn import log


class Runner:
    def __init__(self, name, path, args):
        self.name = name
        self.path = path
        self.args = args

    def run(self, ip):
        command = [self.path, ip, *self.args]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if stderr:
            stderr = stderr.decode().strip()
            log.error(f"Error in {self.name} on {ip}: {stderr}")

        result = stdout.decode().strip()
        log.info(f"Result of {self.name} on {ip}: {result}")
