==========================
Folding marks support
==========================

Folding marks in text editors like Vim can be quite helpful when you are used to
them. One common way to fold different sections of your file is to use a fold
marker. The thing is that you probably don’t want your fold markers ending up
in the rendered documentation.

So to use folds in your files, you basally have three options:

#. Use reStructuredText comments for fold markers. Example:

   .. code:: yaml

      ---
      # .. vim: foldmarker=[[[,]]]:foldmethod=marker

      # .. contents:: Sections
      #    :local:

      # .. First heading [[[
      #
      # -----------------
      #   First heading
      # -----------------

      # .. envvar:: example__list
      #
      # Some text describing this list.
      example__list:
        - 'Something'
        - 'Something'

      # .. ]]]

      # .. Second heading [[[1
      #
      # ------------------
      #   Second heading
      # ------------------

#. Append your fold markers directly after reStructuredText headings. Example:

   .. code:: yaml

      ---
      # .. vim: foldmarker=[[[,]]]:foldmethod=marker

      # .. contents:: Sections
      #    :local:

      # First heading [[[
      # -----------------

      # .. envvar:: example__list
      #
      # Some text describing this list.
      example__list:
        - 'Something'
        - 'Something'

      # .. ]]]

      # Second heading [[[1
      # -------------------
      #

#. Extend your editor by writing a function to recognize the fold levels automatically.

Three variants have their pros and cons and both are supported by `yaml2rst`, so
you can choose.

Advantages of using reStructuredText comments for fold markers:

* It works out of the box. You will not need to do anything extra as it only
  depends on reStructuredText comments for the fold markers.
  (For this, the ``--strip-regex`` command line option is not required.)

* Section "overlines" don’t come in the way when moving folds around. This can
  be an advantage when you are already using them.

Advantages of appending your fold markers directly after reStructuredText headings:

* The whole section line can be used as folding comment in other files as well.
  In the context of Ansible, you can copy a section from the
  `defaults/main.yml` file and use it as is for the implementation in a `tasks`
  file.

* No redundancy. (Don't repeat yourself)

  Because the "Don't repeat yourself" argument is actually quantifiable and has
  an impact on your ability to maintain your files it should be preferred when
  starting freshly. The pro arguments for fold markers in reStructuredText
  comments are just style questions.

Advantages for doing folds with a custom function:

* No changes to the files needed
* People who don’t want folds don’t see any extra wired character sequences in the files.

Disadvantages for doing folds with a custom function:

* Is not as flexible (additional folds can not easily be added)
* Editor dependent (fold markers are expected to be a somewhat common features of editors)

Which fold marker to use
------------------------

Now a short hash up regarding which fold markers to use.

* ``{{{`` is the Vim default. Has the disadvantage that it might get in the way
  with your syntax highlighting. However, '{{{' is not expected to be usually
  found anywhere else in Ansible/YAML/Jinja.

* ``(((`` is more likely to appear in Ansible/YAML/Jinja.

* ``[[[`` is not expected to appear in Ansible/YAML/Jinja. Current recommendation.

Folding format of the DebOps project
------------------------------------

Consider this example which is a result of the thoughts from above:

.. Redundant block of information also included in:
   * ../examples/fold-markers-debops.yml
   (Reason: https://github.com/github/markup/issues/172)

.. code:: yaml

   ---
   # .. vim: foldmarker=[[[,]]]:foldmethod=marker

   # debops.example default variables [[[
   # ====================================

   # .. contents:: Sections
   #    :local:


   # Main configuration [[[
   # ----------------------

   # .. envvar:: example__enabled [[[
   #
   # Some text describing this boolean.
   example__enabled: True

                                                                      # ]]]
   # .. envvar:: example__packages [[[
   #
   # List of additional APT packages which will be installed by the role.
   example__packages: []
                                                                      # ]]]
                                                                      # ]]]
   # Something [[[
   # -------------

   # .. envvar:: example__something [[[
   #
   # Some text describing this list.
   example__periodic: []

                                                                      # ]]]
                                                                      # ]]]
                                                                      # ]]]

Features:

* Closing markers for ``envvar`` folds are indented so that they match a 72
  character long line. This makes it easier to see where a ``envvar`` block
  ends and the next once begins when you look on the left part of the line.

* Does not explicitly set the fold marker level to allow the file to be
  combined into one larger file if needed.

Possible problems:

* When using a YAML block literals, the indented ``# ]]]`` will be part of the
  variable. Example:

  .. code:: yaml

     # .. envvar:: example__packages [[[
     #
     # List of additional APT packages which will be installed by the role.
     example__text: |
       Example text
                                                                      # ]]]

  To avoid this, use:

  .. code:: yaml

     # .. envvar:: example__packages [[[
     #
     # List of additional APT packages which will be installed by the role.
     example__text: |
       Example text
     # ]]]

  In this one case.

* Editors with auto indention might start at the ``# ]]]`` indention level when
  adding a newline after it.
