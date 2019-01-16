import os
import re
import sublime
import sublime_plugin


class QuickCreateFileCreatorBase(sublime_plugin.WindowCommand):


    def file_name_input(self, file_name):
        full_path = os.path.join(self.selected_dir, file_name)

        if os.path.lexists(full_path):
            sublime.error_message('File already exists:\n%s' % full_path)
            return
        else:
            self.create_and_open_file(full_path)

    def create(self, filename):
        base, filename = os.path.split(filename)
        self.create_folder(base)

    def create_folder(self, base):
        if not os.path.exists(base):
            parent = os.path.split(base)[0]
            if not os.path.exists(parent):
                self.create_folder(parent)
            os.mkdir(base)

class QuickCreateFileCommand(QuickCreateFileCreatorBase):
    INPUT_PANEL_CAPTION = 'File name:'

    def run(self):

    def create_and_open_file(self, path):
        if not os.path.exists(path):
            self.create(path)
        self.window.open_file(path)


class QuickCreateDirectoryCommand(QuickCreateFileCreatorBase):
    INPUT_PANEL_CAPTION = 'Folder name:'

    def run(self):

    def create_and_open_file(self, path):
        self.create_folder(path)



