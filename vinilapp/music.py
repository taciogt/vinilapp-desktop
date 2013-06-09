# coding=utf-8

import os
import pygame
import pygame.mixer


class MusicFile:

    hash_seed = 0

    def __init__(self, filepath):
        self.title = 'default'
        self.filepath = os.path.join(os.getcwd(), filepath)
        # should open the file with a try/except
        file = open(self.filepath, 'rb')
        file.seek(-128, 2)
        tagdata = file.read(128)
        if tagdata[:3] != 'TAG':
            # should raises some kind of exception
            pass
        else:
            self.title = tagdata[3:33].strip('\x00')
            self.artist = tagdata[33:63].strip('\x00')
            self.album = tagdata[63:93].strip('\x00')
            self.year = tagdata[93:97].strip('\x00')
            self.hash = MusicFile.hash_seed

            MusicFile.hash_seed += 1

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.filepath)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()


    def to_dict(self):
        music_dict = {'artist': self.artist,
                      'title': self.title,
                      'hash': self.hash}
        return music_dict


if __name__ == '__main__':
    s = MusicFile('./src/BigJack.mp3')
    s.play()
