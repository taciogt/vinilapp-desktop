# coding=utf-8

import unittest
import os
from vinilapp.controller import Controller, Configuration, NoLibraryConfigured

config_file = 'test/configuration.cfg'


class ControllerTests(unittest.TestCase):
    # this tests must be executed from de desktop folder using nosetests
    # otherwise, the library path must be changed

    def test_search_music_folder(self):
        controller = Controller(config_file)
        self.assertEqual(controller.config.get_library_path(), './test/test-search-folder')

        controller.update_library()

        self.assertEqual(len(controller.musics), 5)

        titles = [m.title for m in controller.musics]

        self.assertItemsEqual(titles, ['Crystalised', 'Skies on Fire', 'Islands', 'VCR', 'Intro'])


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
