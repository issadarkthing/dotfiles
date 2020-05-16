from __future__ import (absolute_import, division, print_function)
import ranger.api
from ranger.core.linemode import LinemodeBase
import subprocess
from .devicons import *
from ranger.ext.human_readable import human_readable

@ranger.api.register_linemode
class DirsizeLinemode(LinemodeBase):

    name = "dir_size"

    def filetitle(self, fobj, metadata):
        return devicon(fobj) + ' ' + fobj.relative_path

    def infostring(self, fobj, metadata):

        if fobj.is_directory:
            dir_size = subprocess.getoutput('du -sh "{}"'.format(fobj.path)).split("\t")[0]
            return dir_size
        else:
            return human_readable(fobj.size)

