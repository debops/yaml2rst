# -*- coding: utf-8 -*-
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


from unittest import TestCase
import textwrap
import os
import inspect

import yaml2rst

class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls._outfile = open(os.path.join(os.path.dirname(__file__),
                                         'patterns%s.rst' % cls.__name__), 'w')

    @classmethod
    def tearDownClass(cls):
        cls._outfile.close()

    def _write_pattern(self, *lines):
        """
        Write the expected pattern into a file to be able to (manually)
        verify the expected rst-code is valid and behaves as intented.
        """
        print(file=self._outfile)
        print(inspect.stack()[2][3], file=self._outfile)
        print('='*60, file=self._outfile)
        for line in lines:
            print(line, file=self._outfile)
        print(file=self._outfile)

    def _test(self, text, expected):
        text = textwrap.dedent(text)
        if isinstance(expected, basestring):
            expected = textwrap.dedent(expected).splitlines()
        self._write_pattern(*expected)
        res = list(yaml2rst.convert(text.splitlines()))
        self.assertListEqual(expected, res)
    
    def test_no_text_at_all(self):
        text = """\
        ---
        key: value
        """
        expected = ['::', '', '  key: value']
        self._test(text, expected)


    def test_only_text(self):
        text = """\
        # Some text
        """
        expected = ['Some text']
        self._test(text, expected)


    def test_some_text_behind(self):
        text = """\
        ---
        key: value
        # This is Text behind
        """
        expected = """\
        ::

          key: value

        This is Text behind
        """
        self._test(text, expected)

    def test_some_text_infront(self):
        text = """\
        ---
        # This is Text in front
        key: value
        """
        expected = """\
        This is Text in front
        ::

          key: value
        """
        self._test(text, expected)

    def test_some_text_infront_with_double_colon(self):
        text = """\
        ---
        # This is Text in front::
        key: value
        """
        expected = """\
        This is Text in front::

          key: value
        """
        self._test(text, expected)

    def test_empty_text_line(self):
        text = """\
        ---
        #
        key: value
        """
        expected = """\

        ::

          key: value
        """
        self._test(text, expected)

    def test_empty_text_line2(self):
        text = """\
        #
        key: value
        """
        expected = """\

        ::

          key: value
        """
        self._test(text, expected)

    def test_empty_text_line3(self):
        text = """\
        #
        """
        expected = ['']
        self._test(text, expected)

    def test_empty_line_keeps_state1(self):
        text = """\
        # Some Text

        # More Text
        """
        expected = ['Some Text', '', 'More Text']
        self._test(text, expected)

    def test_empty_line_keeps_state2(self):
        text = """\
        this is code

        More code
        """
        expected= """\
        ::

          this is code

          More code
        """
        self._test(text, expected)


    def test_more_indent(self):
        text = """\
        # Some text
        #
        # - list-entry 1
        # - list-entry 2
        Some code under list-entry 2
        """
        expected= """\
        Some text

        - list-entry 1
        - list-entry 2
          ::

            Some code under list-entry 2
        """
        self._test(text, expected)


    def test_no_more_indent(self):
        text = """\
        # Some text
        #
        # - list-entry 1
        # - list-entry 2
        #
        # ::
        Some code at outer level
        """
        expected= """\
        Some text

        - list-entry 1
        - list-entry 2

        ::

          Some code at outer level
        """
        self._test(text, expected)
