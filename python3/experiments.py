#!/usr/bin/env python3


class Foo:
    """
    Class to demonstrate subscript implementation
    """

    def __getitem__(self, i) -> str:
        """
        implement indexing for Foo class
        :param i: index of item
        :return: string with reference to class instance and index
        """
        if isinstance(i, slice):
            return f"requested items {i.start} to {i.stop}{f' with step {i.step}' if i.step else ''} from {self}"
        return f"requested item {i} from {self}"


if __name__ == "__main__":
    x = Foo()
    print(x[1])
    print(x[-1])
    print(x[0])
    print(x[0:10])
