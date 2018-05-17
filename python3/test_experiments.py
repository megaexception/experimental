#!/usr/bin/env python3
# -*- coding: utf-8 *-
"""
"""
from unittest import TestCase

from experiments import Subscripts


class TestExperiments(TestCase):
    def setUp(self):
        self.foo = Subscripts()

    def testSubscriptsIndex(self):
        """
        Test experiments.Foo for indexing with naturals, and negatives
        Matches result with pattern
        :return:
        """
        for index in [0, 3, 63]:
            self.assertIn(f"requested item {index}", self.foo[index])
        for index in [-1, -3, -63]:
            self.assertIn(f"requested item {len(self.foo)+index}", self.foo[index])
        for index in [-100, 100, 500]:
            with self.assertRaises(IndexError):
                _ = self.foo[index]
        for index in ['', 'foobar']:
            with self.assertRaises(KeyError):
                _ = self.foo[index]

    def testSubcriptsSlices(self):
        """
        Test experiments.Foo for slicing
        Matches result with pattern
        :return:
        """
        for start, stop, step in [(0, 0, None), (0, 10, None), (0, 10, 2), (None, None, None)]:
            subscript = self.foo[start:stop:step]
            if start is None:
                start = 0
            if step is None:
                step = 1 if start >= 0 else -1
            if stop is None:
                if start >= 0:
                    stop = len(self.foo) - 1
                else:
                    stop = 0
            self.assertIn(
                f"requested items {[ i for i in range(start, min(stop, len(self.foo) - 1), step)]}",
                subscript)
