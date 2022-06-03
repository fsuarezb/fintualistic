Fintualistic
===============
This project is intended to solve a basic problem for fintualees: plotting. With this library a python programmer will be able to plot their charts with a fintualistic style, perfect for fintualist articles, presentations and Twitter threads.

Installing
============

    pip install fintualistic

Usage
=====

.. code-block:: bash

    >>> import fintualistic as fl
    >>> import pandas as pd
    >>> series = pd.Series([100, 105, 103, 107, 115, 120])
    >>> fl.plot_series(series)

Plotting functions implemented

- **plot_series**

- **plot_bar**

- **plot_combo_series**

- **plot_pie**

- **plot_scatter**

- **plot_dist**

- **plot_area**