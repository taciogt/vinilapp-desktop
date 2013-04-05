import unittest
import os

from src.song import Song



# def config_working_path():
#     'Lets you call the tests from test folder or from project folder'
#     working_directory = os.getcwd()
#     folders = working_directory.split(os.sep)
#     if folders[-1] != 'test':
#         os.chdir(os.path.join(working_directory, 'test'))


class Mp3Test(unittest.TestCase):
    def test_file_not_found(self):
        pass

    def test_file_not_mp3(self):
        pass

    def test_mp3_constructor(self):

        song = Song(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'song-test.mp3'))
        self.assertEqual(song.title, 'Skies on Fire')

# if __name__ == '__main__':
    # config_working_path()
    # working_directory = os.getcwd()
    # unittest.main()
