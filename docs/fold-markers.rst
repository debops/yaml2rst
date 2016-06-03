==========================
Folding marks support
==========================

Folding marks in text editors like Vim can be quite helpful when you are used to
them. One common way to fold different sections of your file is to use a fold
marker. The thing is that you probably don’t want your fold markers ending up
in the rendered documentation.

So to use folds in your files, you basally have two options:

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
      # -------------

      # .. envvar:: example__list
      #
      # Some text describing this list.
      example__list:
        - 'Something'
        - 'Something'

      # .. ]]]

      # Second heading [[[1
      # --------------
      #

Both variants have their pros and cons and both are supported by `yaml2rst`, so
you can choose.

Advantages of using reStructuredText comments for fold markers:

* It works out of the box. You will not need to do anything extra as it only
  depends on reStructuredText comments for the fold markers.
  (For this, the ``--strip-regex`` command line option is not required.)

* Section "overlines" don’t come in the way when moving folds around. This can
  be an advantage when you are already using them.

Advantages of appending your fold markers directly after reStructuredText headings:

* No redundancy. (Don't repeat yourself)

Because the "Don't repeat yourself" argument is actually quantifiable and has
an impact on your ability to maintain your files it should be preferred when
starting freshly. The pro arguments for fold markers in reStructuredText
comments are just style questions.

Which fold marker to use
------------------------

Now a short hash up regarding which fold markers to use.

* ``{{{`` is the Vim default. Has the disadvantage that it might get in the way
  with your syntax highlighting. However, '{{{' is not expected to be usually
  found anywhere else in Ansible/YAML/Jinja.

* ``(((`` is more likely to appear in Ansible/YAML/Jinja.

* ``[[[`` is not expected to appear in Ansible/YAML/Jinja. Current recommendation.
