import json

from core.Target import Target
from pwn import log


class TargetPool:
    def __init__(self):
        self.servers = []
        
    def __iter__(self):
        return iter(self.servers)

    def add_server(self, server):
        self.servers.append(server)

    def get_servers(self):
        return self.servers

    def get_server(self, idx):
        return self.servers[idx]

    def get_server_by_host(self, host):
        for server in self.servers:
            if server.host == host:
                return server
        return None

    def get_server_by_idx(self, idx):
        return self.servers[idx]

    def remove_server(self, idx):
        self.servers.pop(idx)

    def remove_server_by_host(self, host):
        for i, server in enumerate(self.servers):
            if server.host == host:
                self.servers.pop(i)
                return

    def remove_server_by_idx(self, idx):
        self.servers.pop(idx)
        
    @staticmethod
    def parse_json(path: str) -> "TargetPool":
        pool = TargetPool()
        datas = json.load(open(path))
        for server in Target.iter_datas(datas):
            pool.add_server(Target.from_data(server))

        return pool
        
    def __len__(self):
        return len(self.servers)