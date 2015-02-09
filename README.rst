==========================
yaml2rst
==========================
--------------------------------------------------------------------------
A Simple Tool and Python-Module for Documenting YAML Files.
--------------------------------------------------------------------------

:Author:    Hartmut Goebel <h.goebel@crazy-compilers.com>
:Copyright: 2015 by Hartmut Goebel
:Licence:   GNU General Public Licence v3 or later (GPLv3+)


Usage::

  yaml2rst [-h] infile outfile

  positional arguments:
    infile      YAML-file to read (`-` for stdin)
    outfile     rst-file to write (`-` for stdout)

  optional arguments:
    -h, --help  show this help message and exit


How it works
----------------

This script takes all lines beginning with ``# `` (and lines
consisting of only a ``#``) as text-lines. Everything else will be
treated as "code". The text-lines will get the ``# `` removed and the
"code" will get spaces prepended.

Additionally at the start and at the end of a "code"-block, lines are
added as required by reStructuredText. Also at the begin of a
"code"-block, a ``::`` is added if required.


Examples
-------------

You can find example yaml-input, rst-output and generated html in the
examples directory. You may also view the generated html online at
https://rawgit.com/htgoebel/yaml2rst/develop/examples/main.html.

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
