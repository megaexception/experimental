#!/usr/bin/env python3


class Foo:
    """
    Class to demonstrate subscript implementation
    """

    def __getitem__(self, i: int) -> str:
        """
        implement indexing for Foo class
        :param i: index of item
        :return: string with reference to class instance and index
        """
        return f"requested item {i} from {self}"


if __name__ == "__main__":
    x = Foo()
    print(x[1])
    print(x[-1])
    print(x[0])
