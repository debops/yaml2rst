# -*- coding: utf-8 -*-
"""
yaml2rst – A Simple Tool for Documenting YAML Files
"""
#
# Copyright 2015 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import print_function

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2015 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU General Public License version 3 (GPL v3)"
__version__ = "0.1"

STATE_TEXT = 0
STATE_YAML = 1

def convert(lines):
    state = STATE_TEXT
    last_text_line = ''
    for line in lines:
        line = line.rstrip()
        if not line:
            # do not change state if the line is empty
            yield ''
        elif line.startswith('# ') or line == '#':
            if state != STATE_TEXT:
                yield ''
            line = last_text_line = line[2:]
            yield line
            state = STATE_TEXT
        elif line == '---':
            pass
        else:
            if line.startswith('---'):
                line = line[3:]
            if state != STATE_YAML:
                if not last_text_line.strip().endswith('::'):
                    yield '::'
                yield ''
            yield '  ' + line
            state = STATE_YAML

def convert_text(yaml_text):
    return '\n'.join(convert(yaml_text.splitlines()))
    

def convert_file(infilename, outfilename):
    with open(infilename) as infh:
        with open(outfilename, "w") as outfh:
            for l in convert(infh.readlines()):
                print(l.rstrip(), file=outfh)
