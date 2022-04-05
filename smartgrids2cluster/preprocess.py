import numpy as _np
from numpy import ndarray as _ndarray
from pandas import DataFrame as _DataFrame

def l2_norm(
        X: _ndarray,
        eps: float = 1e-8
        ) -> _ndarray:
    norms = _np.linalg.norm(X, axis=1)
    return X / (norms.reshape(-1, 1) + eps)

def get_obs_matrix(
        df: _DataFrame
        ) -> _ndarray:
    return df[[f"{i}" for i in range(24)]].values

def filter(
        df: _DataFrame,
        expr: str
        ):
    if expr == "all":
        return df
    return df.query(expr)
