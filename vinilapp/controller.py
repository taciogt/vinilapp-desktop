# coding=utf-8
import os
import ConfigParser
from music import MusicFile


class Controller:

    def __init__(self, config_file):
        self.config = Configuration(config_file)

    def _searchFolders(self, directory):
        folders = [f for f in os.listdir(directory)
                   if os.path.isdir(os.path.join(directory, f))]
        for f in folders:
            self._searchFolders(os.path.join(directory, f))

        music_files = [m for m in os.listdir(directory)
                       if os.path.splitext(m)[1] in ['.mp3']]

        for m in music_files:
            self.musics.append(MusicFile(os.path.normcase(os.path.join(directory, m))))

    def update_library(self):
        self.musics = []
        directory = self.config.get_library_path()
        self._searchFolders(directory)

    def play(self):
        self.music_playing = self.musics[0]
        self.music_playing.play()

    def pause(self):
        self.music_playing.stop()

    def play_next(self):
        if self.music_playing:
            self.musics.append(self.music_playing)

        self.musics.pop(0)
        self.music_playing = self.musics[0]
        self.music_playing.play()

    def get_current_music(self):
        return self.music_playing

    def get_musics_list(self):
        return [music.to_dict() for music in self.musics]

    def reorder_music_list(self, first_music_hash):
        for music in self.musics:
            if music.hash == first_music_hash:
                self.musics.remove(music)
                self.musics.insert(0, music)


class Configuration:

    def __init__(self, config_file):
        self.config_file = config_file

        self.config = ConfigParser.SafeConfigParser()
        self.config.read(config_file)

    def get_library_path(self):
        if self.config.has_section('Library'):
            if self.config.has_option('Library', 'library_path'):
                return self.config.get('Library', 'library_path')
            else:
                raise NoLibraryConfigured()
        else:
            raise NoLibraryConfigured()

    def set_library_path(self, library_path):
        if not self.config.has_section('Library'):
            self.config.add_section('Library')
        self.config.set('Library', 'library_path', library_path)

        with open(self.config_file, 'wb') as file:
            self.config.write(file)


class NoLibraryConfigured(Exception):
    pass


if __name__ == '__main__':
    controller = Controller()
