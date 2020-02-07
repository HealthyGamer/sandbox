|build-status|

Installing
----------

Windows ::

    py -m pip install git+https://github.com/HealthyGamer/sandbox.git

Linux & Mac ::

  pip3 install git+https://github.com/HealthyGamer/sandbox.git

Note
----

This is a namespace-like package, which means its contents must be imported
explicitly to avoid loading unwanted submodules.

.. code-block:: py

  import sandbox.game as game

  game.run()

Links
-----

- `Explanations <https://healthygamer.readthedocs.io>`_

.. |build-status| image::https://github.com/HealthyGamer/sandbox/workflows/Python%20application/badge.svg
