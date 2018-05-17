#!/usr/bin/env python3
# -*- coding: utf-8 *-
"""
"""
from unittest import TestCase

from experiments import Foo


class TestExperiments(TestCase):
    def setUp(self):
        self.foo = Foo()

    def testSubscripts(self):
        for index in [0, 3, 500, -1]:
            subscript = self.foo[index]
            self.assertIn(f"requested item {index}", subscript)
