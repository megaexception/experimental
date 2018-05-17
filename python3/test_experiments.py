#!/usr/bin/env python3
# -*- coding: utf-8 *-
"""
"""
from unittest import TestCase

from experiments import Foo


class TestExperiments(TestCase):
    def setUp(self):
        self.foo = Foo()

    def testSubscriptsIndex(self):
        """
        Test experiments.Foo for indexing with naturals, and negatives
        Matches result with pattern
        :return:
        """
        for index in [0, 3, 500, -1]:
            subscript = self.foo[index]
            self.assertIn(f"requested item {index}", subscript)

    def testSubcriptsSlices(self):
        """
        Test experiments.Foo for slicing
        Matches result with pattern
        :return:
        """
        for start, stop, step in [(0, 0, None), (0, 10, None), (0, 10, 2)]:
            subscript = self.foo[start:stop:step]
            self.assertIn(f"requested items {start} to {stop}{f' with step {step}' if step else ''} from", subscript)
