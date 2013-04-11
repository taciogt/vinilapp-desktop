# coding=utf-8

import unittest
from start import Program

class StartTests(unittest.TestCase):
    def test_set_music_folder(self):
        program = Program()

        program.update_library()


        program.set_music_folder('blah')
        # self.assertRaises(NonExistingFolder, program.update_library)