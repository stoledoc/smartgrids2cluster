import numpy as _np
import pandas as _pd
import os as _os
import joblib as _joblib
from numpy import ndarray as _ndarray
from pandas import DataFrame as _DataFrame
from sklearn.cluster import KMeans as _KMeans
from typing import List as _List
from smartgrids2cluster.datamodels import Result as _Result

def load_data(path: str) -> _DataFrame:
    return _pd.read_parquet(path)

def export_results(
        results: _List[_Result],
        save_path: str
        ):
    _joblib.dump(
            results,
            save_path
            )

def load_results(
        path: str
        ) -> _List[_Result]:
    return _joblib.load(path)

def export_df_clusters(
        df: _DataFrame,
        model: _KMeans,
        X: _ndarray,
        save_path: str,
        name: str
        ):
    df[name] = model.predict(X)
    df.to_parquet(save_path)
