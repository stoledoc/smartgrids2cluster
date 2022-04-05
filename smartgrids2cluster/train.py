from smartgrids2cluster.datamodels import (
        Result as _Result,
        Metrics as _Metrics
        )
from typing import List as _List
from numpy import ndarray as _ndarray
from sklearn.cluster import KMeans as _KMeans
from sklearn.metrics import silhouette_score as _silhouette_score
from sklearn.metrics import davies_bouldin_score as _davies_bouldin_score

def train_cluster(X: _ndarray, k=4) -> _Result:
    print(f"Training with k={k}")
    estimator = _KMeans(n_clusters=k).fit(X)
    preds = estimator.predict(X)
    metrics = _Metrics(
            silhouette_score=_silhouette_score(X, preds),
            davies_bouldin_score=_davies_bouldin_score(X, preds),
            inertia=estimator.inertia_
            )
    result = _Result(
            n_clusters=k,
            model=estimator,
            metrics=metrics
            )
    return result
