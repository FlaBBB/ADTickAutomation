import json

from pwn import log


class Target:
    def __init__(self, host: str) -> None:
        self.host = host
    
    
    @staticmethod
    def from_data(data: any) -> "Target":
        return Target(
            data
        )
        
    def iter_datas(datas: dict):
        return datas["data"]