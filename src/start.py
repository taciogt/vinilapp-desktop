# coding=utf-8


class Program:

    def set_music_folder(self, folder_path):
        self.music_folder = folder_path

    def update_library(self):
        pass


class NonExistingFolder(IOError):
    pass


if __name__ == '__main__':
    print 'main'
