import joblib
import numpy as np
from smartgrids2cluster.io import load_data, export_results
from smartgrids2cluster.preprocess import l2_norm, get_obs_matrix, filter
from smartgrids2cluster.train import train_cluster
from smartgrids2cluster.utils import get_env_vars

if __name__ == "__main__":
    np.random.seed(0)
    env_vars = get_env_vars()
    df = load_data(env_vars.data_path)
    df = filter(df, env_vars.query)
    X = get_obs_matrix(df)
    X = l2_norm(X)
    results = joblib.Parallel(n_jobs=-1)(
            joblib.delayed(train_cluster)(X, k)
            for k in range(20, 50)
            )

    export_results(results, env_vars.save_name)
