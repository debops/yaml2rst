#
# This file is part of `yaml2rst`.
# Based on prior work from `gitflow`
#   Copyright (c) 2010-2011 Vincent Driessen
#   Copyright (c) 2012-2015 Hartmut Goebel
# Distributed under a BSD-like license.
#

.PHONY : all clean celan-files clean-all clean-tox
.PHONY : xunit-test test test-dist cover
.PHONY : dump-requirements install-requirements
.PHONY : dist examples test-upload test-install

all: cover

clean: clean-files

clean-files:
	find . -name '*.py[co]' -delete
	rm -rf *.egg *.egg-info
	rm -f nosetests.xml *.egg-lnk pip-log.txt

clean-all: clean-tox clean
	rm -rf build dist .coverage examples/*.rst examples/*.html

clean-tox:
	rm -rf .tox

xunit-test:
	nosetests --with-xunit

test:
	nosetests --with-spec --spec-color

test-dist:
	PIP_DOWNLOAD_CACHE=~/Projects/pkgrepo/pkgs
	tox

cover:
	nosetests --with-coverage3 --cover-package=gitflow --with-spec --spec-color

dump-requirements:
	pip freeze -l > .requirements

install-requirements:
	pip install -r .requirements

dist:
	@# ensure a clean build
	rm -rf build
	python setup.py sdist bdist

examples: examples/main.rst examples/main.html tests/patternsTest.html

examples/main.rst: examples/fold-markers-debops.yml examples/main.yml
	PYTHONPATH=.
	sed --regexp-extended 's/(\.\. )envvar(::)/\1note\2/;' $? \
		| bin/yaml2rst - "$@" --strip-regex '\s*(:?\[{3}|\]{3})\d?$$' --yaml-strip-regex '^\s{66,67}#\s\]{3}\d?$$'
	## --no-generator does not do the trick on Debian Jessie.

examples/main.html: examples/main.rst examples/demo.css
	rst2html --stylesheet=examples/demo.css "$<" | grep --invert-match --fixed-strings '<meta name="generator"' > "$@"

tests/patternsTest.html: tests/patternsTest.rst examples/demo.css
	rst2html --stylesheet=examples/demo.css "$<" > "$@"

#-- interaction with PyPI

test-upload dist:
	python ./setup.py register -r https://testpypi.python.org/pypi
	python ./setup.py sdist upload -r https://testpypi.python.org/pypi

test-install:
	virtualenv /tmp/test-yaml2rst
	/tmp/test-yaml2rst/bin/pip install -i https://testpypi.python.org/pypi yaml2rst

upload: dist
	python ./setup.py register
	python ./setup.py sdist upload
