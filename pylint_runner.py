#!/usr/bin/env python

"""
Runs pylint on all contained python files in this directory, printint out
nice colorized warnings/errors without all the other report fluff
"""
from __future__ import print_function
import os
from pylint.lint import Run

__author__ = "Matthew 'MasterOdin' Peveler"
__license__ = "The MIT License (MIT)"

IGNORE_FOLDERS = [".git", ".idea", "__pycache__"]


def run_runner():
    """
    Runs pylint on all python files in the current directory
    """

    pylint_files = get_files_from_dir(os.curdir)
    print("pylint running on the following files:")
    for pylint_file in pylint_files:
        print(pylint_file)
    print("----")
    Run(pylint_files)


def get_files_from_dir(current_dir):
    """
    Recursively Walk through a directory and get all python files and then walk
    through any potential directories that are found off current directory,
    so long as not within IGNORE_FOLDERS
    :return: all python files that were found off current_dir
    """
    files = []
    for dir_file in os.listdir(current_dir):
        if current_dir != ".":
            file_path = current_dir + dir_file
        else:
            file_path = dir_file
        if os.path.isfile(file_path):
            file_split = os.path.splitext(dir_file)
            if len(file_split) == 2 and file_split[0] != "" \
                    and file_split[1] == '.py':
                print(file_path)
                files.append(file_path)
        elif os.path.isdir(dir_file) and dir_file not in IGNORE_FOLDERS:
            files += get_files_from_dir(dir_file+"/")
    return files

if __name__ == "__main__":
    run_runner()
