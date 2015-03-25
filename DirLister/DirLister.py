#!/usr/local/bin/python

"""
Description:

This script is used to walk a directory and print out each filename and  directory including the full path.

Author: Name

Usage:
  DirLister.py (-d <directory>)
  DirLister.py -h | --help
  DirLister.py --version

Options:
  -d <directory>     The top level directory you want to list files and directories from.
  -h --help          Show this screen.
  --version          Show version.
  """

import os
from docopt import docopt

class Walking:
    def __init__(self, directory):
        self.directory = directory

    def walk(self, directory):
        for root, dirs, files in os.walk(self.directory):
            for filename in files:
                print os.path.join(root, filename)

if __name__ == '__main__':

    arguments = docopt(__doc__, version= '1.0.0')
    walking = Walking(arguments['-d'])
    print arguments
    if arguments['-d'] is None:
        print __doc__
        exit(0)
    else:
        walking.walk(arguments['-d'])