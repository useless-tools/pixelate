pixelate
========

.. figure:: https://travis-ci.org/useless-tools/pixelate.svg?branch=master


Make your photos even worse. But it's like pixel art.

Works with Python ≥ 3.2. Use version 0.4 for Python 2.* projects.

Installation
------------

.. code:: bash

    pip install pixelate

Usage
-----

From CLI:

.. code:: bash

    pixelate --input=img/bps.jpg --output=img/bps.png --pixel-size=10


`pixelate` arguments:

- `--input` – string – path to input image.
- `--output` – string – path to output image.
- `--pixel-size` – integer – pixel size.

From Python code:

.. code:: python

    from pixelate import pixelate
    
    pixelate('img/bps.jpg', 'img/bps.png', 10)

Args:

- input_file_path: the path to the source image file to be processed.
- output_file_path: the path to the result file.
- pixel_size: pixel size.

From this:

.. image:: ./img/bps.jpg
  :alt: original bps

To this:

.. image:: ./img/bps.png
  :alt: pixeated bps

