#!/usr/bin/env python3


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
        # TODO: detect start>end and adjust step
        # TODO: if only one of (start,end,step) is None - adjust


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
    # print(passwd_reader())
    nl_file()
