# coding=utf-8

import unittest
import os
from vinilapp.controller import Controller, Configuration, NoLibraryConfigured


class ControllerTests(unittest.TestCase):

    def test_none_folder(self):
        # check the behavior with a None music_folde
        pass

    def test_search_music_folder(self):
        controller = Controller()
        test_folder = os.path.join(os.path.realpath(__file__), 'test-search-folder')

        controller.music_folder = test_folder


config_file_test = 'test-configuration.cfg'


class ConfigurationTests(unittest.TestCase):

    def tearDown(self):
        os.remove(config_file_test)

    def test_creating_file(self):
        self.assertRaises(TypeError, Configuration)

        config = Configuration(config_file_test)
        self.assertRaises(NoLibraryConfigured, config.get_library_path)

        config.set_library_path('/home/music/')
        self.assertEqual(config.get_library_path(), '/home/music/')
