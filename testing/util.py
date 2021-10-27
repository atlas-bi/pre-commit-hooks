# https://github.com/pre-commit/pre-commit-hooks/blob/master/testing/util.py

import os.path
import subprocess

TESTING_DIR = os.path.abspath(os.path.dirname(__file__))


def get_resource_path(path):
    return os.path.join(TESTING_DIR, "resources", path)
