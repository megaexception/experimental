#!/usr/bin/env python3
# -*- coding: utf-8 *-
"""
"""
import os
from unittest import TestCase

import experiments


class TestRetriever(TestCase):
    def test_urlparse(self):
        cases = {
            'http://google.com/foo/bar': ('http', 'google.com', 80),
            'https://google.com/foo/bar': ('https', 'google.com', 443),
            'https://google.com:80/foo/bar': ('https', 'google.com', 80),
            'http://google.com:443/foo/bar': ('http', 'google.com', 443),
            'https://rutracker.org/forum/dl.php?t=5519684': ('https', 'rutracker.org', 443)
        }
        for case in cases:
            self.assertEqual(experiments.Retriever.urlparse(case), cases[case])

    def test_retrieve_cookies(self):
        for site in os.listdir("data"):
            self.assertIsNotNone(experiments.Retriever.retrieve_cookies(".".join(site.split('.')[:-1])))

    # def test_store_cookies(self):
    #     self.fail()

    # def test_login(self):
    #     self.fail()

    def test_fetch(self):
        self.fail()

    def test_for_url(self):
        # TODO: add list of urls, attemt to get Retriever, count number of unique instances?
        r1 = Retriever("http://127.0.0.1:8112/json", mode='JSON')
        r2 = Retriever("https://rutracker.org/forum/login.php", mode="SKIP")
        r4 = Retriever.for_url("https://rutracker.org/forum/login.php")
        r5 = Retriever.for_url("https://rutracker.org/forum/login.php")
        r5.fetch("https://rutracker.org/forum/dl.php?t=5519684", "data/5519684.torrent")
        self.fail()
