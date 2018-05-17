#!/usr/bin/env python3


class Foo:
    def __getitem__(self, i):
        return f"requested item {i} from {self}"


if __name__ == "__main__":
    x = Foo()
    print(x[1])
    print(x[-1])
    print(x[0])
