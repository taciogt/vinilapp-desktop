# coding=utf-8
import ConfigParser


class Controller:

    def __init__(self):
        pass

    def update_library(self):
        if self.music_library_folder is None:
            pass  # handle this

        pass


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
