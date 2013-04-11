# coding=utf-8

import unittest
import os
from vinilapp.controller import Controller


class ControllerTests(unittest.TestCase):

    def test_none_folder(self):
        # check the behavior with a None music_folder
        pass

    def test_search_music_folder(self):
        controller = Controller()
        test_folder = os.path.join(os.path.realpath(__file__), 'test-search-folder')

        controller.music_folder = test_folder
