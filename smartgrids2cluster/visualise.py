import matplotlib.pyplot as _plt
import numpy as _np
from matplotlib.pyplot import Figure as _Figure
from typing import List as _List
from smartgrids2cluster.datamodels import Result as _Result
_plt.style.use("ggplot")

def metrics_plot(results: _List[_Result]) -> _Figure:
    fig, ax = _plt.subplots(1, 3, figsize=(15, 10))
    X = _np.array([
        (res.n_clusters, res.metrics.silhouette_score, res.metrics.davies_bouldin_score, res.metrics.inertia)
        for res in results
        ])
    ax[0].plot(X[:, 0], X[:, 1])
    ax[0].set_xlabel("Número de clusters")
    ax[0].set_ylabel("Coeficiente de Silueta")
    ax[1].plot(X[:, 0], X[:, 2])
    ax[1].set_xlabel("Número de clusters")
    ax[1].set_ylabel("Davies Bouldin")
    ax[2].plot(X[:, 0], X[:, 3])
    ax[2].set_xlabel("Número de clusters")
    ax[2].set_ylabel("Inercia")

    fig.tight_layout()
    return fig
