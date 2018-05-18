#!/usr/bin/env python3
import json
import os.path
import sys
from urllib.parse import urlparse

from requests import Session


class Subscripts:
    """
    Class to demonstrate subscript implementation
    """

    def __init__(self, max_size=None):
        self.max_size = max_size or 64

    def __len__(self):
        return self.max_size

    def __getitem__(self, i) -> str:
        """
        implement indexing for Foo class
        :param i: index of item
        :return: string with reference to class instance and index
        """
        if isinstance(i, slice):
            start, stop, step = i.start, i.stop, i.step
            if start is None:
                start = 0
            elif abs(start) > self.max_size:
                raise IndexError
            elif start < 0:
                start = self.max_size + start
            if stop is None:
                if i.start is None or i.start >= 0:
                    stop = self.max_size
                else:
                    stop = 0
            elif stop < 0:
                stop = self.max_size + i.stop
            if step is None:
                step = 1 if start < stop else -1
            # print(f"> {i}=> {start}:{stop}:{step}")
            items = [i for i in range(start, min(stop, self.max_size), step)]
            return f"requested items {items} of {self.max_size}"
        elif isinstance(i, int):
            if abs(i) > self.max_size:
                raise IndexError
            if i < 0:
                return f"requested item {self.max_size+i} of {self.max_size}"
            return f"requested item {i} of {self.max_size}"
        else:
            raise KeyError
        # TODO: if only one of (start,end,step) is None - adjust


class Retriever:
    _retrievers = dict()

    def __init__(self, login_url=None, auth=None, mode=None):
        self.mode = mode
        self.s = Session()
        self.schema, self.host, self.port = self.urlparse(login_url)
        self.cookies = self.retrieve_cookies()
        self.auth = auth
        for c in self.cookies:
            self.s.cookies.set(c, self.cookies[c])
        if not self.login(login_url):
            print("Failed to log in")
        else:
            print("Login seems to work")
            self.store_cookies(self.s.cookies.get_dict())
            self._retrievers[self.host] = self

    @staticmethod
    def urlparse(url):
        schema, netloc, *_ = urlparse(url)
        if ":" in netloc:
            host, port = netloc.split(":")
        else:
            host = netloc
            port = 80 if schema == "http" else 443
        return schema, host, port

    def retrieve_cookies(self) -> dict:
        if os.path.exists(f"data/{self.host}.cookies"):
            with open(f"data/{self.host}.cookies") as f:
                return json.load(f)
        return {}

    def store_cookies(self, cookies: dict) -> None:
        with open(f"data/{self.host}.cookies", "wt") as f:
            json.dump(cookies, f)

    def login(self, login_url: str) -> bool:
        try:
            if self.mode == "JSON":
                res = self.s.post(login_url, json=self.auth)
            elif self.mode == "FORM":
                res = self.s.post(login_url, data=self.auth)
            elif self.mode == "BASIC":
                self.s.auth = self.auth
                res = self.s.get(login_url)
                # TODO: implement AUTH
            else:
                res = self.s.get(login_url)
            # print(res.headers)
            # print(res.content)
            res.raise_for_status()
        except Exception as e:
            print(e)
            print(sys.exc_info())
            return False
        else:
            return True

    @classmethod
    def for_url(cls, login_url, **kwargs):
        schema, host, port = cls.urlparse(login_url)
        if host in cls._retrievers:
            return cls._retrievers[host]
        else:
            return cls(login_url, **kwargs)


def subscripts():
    x = Subscripts()
    print(x[1])
    print(x[-1])
    print(x[0])
    print(x[-10])
    # print(x[-500])
    # print(x[500])
    print(x[0:0])
    print(x[0:10])
    print(x[0::2])
    print(x[-1::])
    print(x[-1:1])
    print(x[-1::-1])
    print(x[::])


def passwd_reader(passwd_file="/etc/passwd") -> dict:
    passwd_entry = ["username", "password", "uid", "gid", "description", "home", "shell"]
    results = {}
    with open(passwd_file) as f:
        for line in f:
            params = line.strip().split(':')
            results[params[0]] = dict(zip(passwd_entry, params))
    return results


def nl_file(fname="/etc/passwd") -> None:
    with open(fname) as f:
        for index, line in enumerate(f):
            print(f"{index:03}. {line}")


if __name__ == "__main__":
    # r1 = Retriever("http://127.0.0.1:8112/json", mode='JSON')
    r2 = Retriever("https://rutracker.org/forum/login.php", mode="SKIP")
    print(r2)
    r4 = Retriever.for_url("https://rutracker.org/forum/login.php")
    print(r4)
    r5 = Retriever.for_url("https://rutracker.org/forum/login.php")
    print(r5)
