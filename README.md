# outgraph

`outgraph` is a simple outlier detection algorithm for graph datasets. Given a list of graphs, it uses [Mahalanobis distance](https://en.wikipedia.org/wiki/Mahalanobis_distance) detect which graphs are outliers based on either their topology or node attributes.

> Note: `outgraph` only works for datasets where each graph has an equal number of nodes.

## Installation

You can install `outgraph` with `pip`:

```bash
$ pip install outgraph
```

## How it Works

Unlike most approaches to graph outlier detection, `outgraph` does not use machine learning. Instead, each graph is converted into a vector representation using one of three available methods:

1. Averaging the node feature/attribute vectors
2. Flattening the adjacency matrix
3. A concatenation of 1 and 2

Then, the [Mahalanobis distance](https://en.wikipedia.org/wiki/Mahalanobis_distance) between each vector and the distribution of vectors is calculated. Lastly, a [Chi-Squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution) is used to model the distribution of distances and identify the distances outside a cutoff threshold (e.g. p < 0.05).

This approach is based off [this article.](https://towardsdatascience.com/multivariate-outlier-detection-in-python-e946cfc843b3)

## Usage

Each graph in your dataset needs to be an instance of `outgraph.Graph`. This object has two parameters, `node_attrs` and `adjacency_matrix` –– both numpy arrays where the indices correspond to nodes. Example:

```python
import numpy as np
from outgraph import Graph

node_attrs = np.array([[-1], [0], [1]])
adj_matrix = np.array([[1, 1, 0],
                       [1, 1, 1],
                       [0, 1, 1]])
graph = Graph(node_attrs, adj_matrix)
```

<p align="center">
  <img src="example_graph.svg" width="35%" />
  <br />
</p>

Once you have a list of `Graph` objects, simply submit them into `outgraph.detect_outliers`:

```python
from outgraph import Graph, detect_outliers

graphs = [Graph(), ...]
outliers, indices = detect_outliers(graphs, method=1, p_value=0.05)
```

Notice the `method` and `p_value` parameters. The `method` parameter is an integer between 1 and 3 that corresponds to one of the three graph vectorization methods described in the ![How it Works](##How it Works) section. `p_value` is the outlier cutoff threshold.
