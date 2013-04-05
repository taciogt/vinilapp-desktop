# coding=utf-8

import os


class Song:
    '''Abstraction of a song file
    Represents all formats of files, like mp3, wma, flac.
    '''

    def __init__(self, filename):
        self.title = 'default'
        self.path = os.path.join(os.getcwd(), filename)
        self.title = self.path
        # try:
        file = open(self.path, 'rb')
        file.seek(-128, 2)
        tagdata = file.read(128)
        if tagdata[:3] != 'TAG':
            # 'raises some kind of exception'
            self.title = 'adasdsads'
            pass
        else:
            
            self.title = tagdata[3:33]
            # self.title = 'qweqwewqe'
        # except IOError:
            
