import unittest
import os
from vinilapp.music import MusicFile


class Mp3Test(unittest.TestCase):
    def test_file_not_found(self):
        pass

    def test_file_not_mp3(self):
        pass

    def test_mp3_constructor(self):

        music = MusicFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'song-test.mp3'))
        self.assertEqual(music.title, 'Skies on Fire')
        self.assertEqual(music.artist, 'AC/DC')
        self.assertEqual(music.album, 'Black Ice [Import]')
        self.assertEqual(music.year, '2008')
