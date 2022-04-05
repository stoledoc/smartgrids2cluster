from pydantic import BaseModel as _BaseModel
from sklearn.cluster import KMeans as _KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score

class Metrics(_BaseModel):
    silhouette_score: float
    davies_bouldin_score: float
    inertia: float

class Result(_BaseModel):
    n_clusters: int
    model: _KMeans
    metrics: Metrics
    class Config:
        arbitrary_types_allowed = True

class EnvironmentVariables(_BaseModel):
    data_path: str
    save_name: str
    query: str
