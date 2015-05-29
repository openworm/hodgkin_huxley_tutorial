#!/usr/bin/env python

# run this from the Tutorial directoy (i.e. `python live.py`) to have a live reloading version of the docs.
# you may need to do `pip install livereload` first

from livereload import Server, shell
server = Server()
server.watch('_static/*.rst', shell('make html', cwd='.'))
server.serve(root='_build/html')
