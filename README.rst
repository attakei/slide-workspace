slides-workstation
==================

Workspace for attakei's presentations

Includes
--------

* ``Sphinx`` core
* ``sphinx-revealjs`` and misc extensions.
* sass builder
* Git
* Zsh
* Support tool application

Basic usage
-----------

#. Pull image
#. Initialize your space
#. Write presentation in workspace

.. code-block:: bash

    $ docker pull attakei/slides-worpspace
    $ mkdir your-slide
    $ docker run --rm -v `pwd`/your-slide:/data slide.init
