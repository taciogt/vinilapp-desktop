import unittest
import os
from song import AudioFile


class Mp3Test(unittest.TestCase):
    def test_file_not_found(self):
        pass

    def test_file_not_mp3(self):
        pass

    def test_mp3_constructor(self):

        song = AudioFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'song-test.mp3'))
        self.assertEqual(song.title, 'Skies on Fire')
        self.assertEqual(song.artist, 'AC/DC')
        self.assertEqual(song.album, 'Black Ice [Import]')
        self.assertEqual(song.year, '2008')
