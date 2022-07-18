# outgraph

`outgraph` is an outlier detection algorithm for graph datasets. Given a list of graphs, it will use [Mahalanobis distance](https://en.wikipedia.org/wiki/Mahalanobis_distance) detect which graphs are outliers based on either their topology or node attributes.

> Note: `outgraph` only works for datasets where each graph has an equal number of nodes.

## Installation

TODO: Upload package to PyPi

## How it Works

`outgraph` is _not_ a machine learning approach. Instead, each graph is converted into a vector representation using one of three methods available to you:

1. Averaging the node feature/attribute vectors
2. Flattening the adjacency matrix
3. A concatenation of 1 and 2

Then, the [Mahalanobis distance](https://en.wikipedia.org/wiki/Mahalanobis_distance) between each vector and the distribution of vectors is calculated. Lastly, a [Chi-Squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution) is used to identify graphs with distances outside a cutoff threshold (e.g. p < 0.05).

## Usage

Each graph in your dataset needs to be an instance of `outgraph.Graph`. This object has two parameters, `node_attrs` and `adjacency_matrix`, both numpy arrays where the indices correspond to nodes:

```python
import numpy as np
from outgraph import Graph

graph = Graph(
  node_attrs=np.array([[0, 0, 1],
                       [0, 1, 0],
                       [1, 0, 0]]),
  adjacency_matrix=np.array([[1, 1, 0],
                             [1, 1, 1],
                             [0, 1, 1]])
)
```

Once you have a list of `Graph` objects, simply submit them into `outgraph.detect_outliers`:

```python
from outgraph import Graph, detect_outliers

graphs = [Graph(), ...]
outliers, indices = detect_outliers(graphs, method=1, p_value=0.05)
```

Note that the `method` parameter is an integer corresponding to one of the three available vectorization methods described in [How it Works](##How it Works). And `p_value` is the outlier cutoff value used in the Chi-squared distribution.
