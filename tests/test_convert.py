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

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2015 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU General Public License version 3 (GPL v3)"


from unittest import TestCase
import textwrap

import yaml2rst

class Test(TestCase):

    def _test(self, text, expected):
        text = textwrap.dedent(text)
        if isinstance(expected, basestring):
            expected = textwrap.dedent(expected).splitlines()
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
