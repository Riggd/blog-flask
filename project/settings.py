# -*- coding: utf-8 -*-

import os

REPO_NAME = "blog-flask"
DEBUG = True

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))
    
PROJECT_ROOT = parent_dir(APP_DIR)

FREEZER_DESTINATION = PROJECT_ROOT

FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False # Setting to True will delete
                                   # all app files

FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'

'''
HOW TO FREEZE AND UPLOAD SITE

$ python freeze.py
$ git init
$ git add . --all
$ git commit -am "Initial commit"
$ git checkout -b gh-pages
$ git remote add origin https://github.com/username/flask-ghpages-example.git
$ git push origin --all

'''