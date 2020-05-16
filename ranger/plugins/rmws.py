import ranger.api
from ranger.api.commands import *
from time import sleep


class rmws(Command):
    """
    :rmws

    removes whitespace and rename files
    """

    def execute(self):

        files = []

        for f in self.fm.thistab.get_selection():

            name = f.basename
            files.append(name)

        files = map(lambda x: x.replace(' ', '_'), files)

        self.fm.notify(list(files))






