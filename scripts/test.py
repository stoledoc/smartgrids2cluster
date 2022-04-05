from smartgrids2cluster.utils import get_env_vars
from smartgrids2cluster.io import load_results, export_df_clusters, load_data
from smartgrids2cluster.preprocess import get_obs_matrix, l2_norm 
from smartgrids2cluster.visualise import metrics_plot

if __name__ == "__main__":
    env_vars = get_env_vars()

    # loading results
    results = load_results(env_vars.save_name)

    # create results plot
    fig = metrics_plot(results)
    save_path = env_vars.save_name.split(".")[0]
    fig.savefig(f"{save_path}.png")

    # export df with clusters
    df = load_data(env_vars.data_path)
    X = get_obs_matrix(df)
    X = l2_norm(X)
    df.loc[:, map(str, range(24))] = X
    model = min(results, key=lambda x: x.metrics.davies_bouldin_score).model
    name = save_path.split("/")[-1]
    export_df_clusters(
            df, model,
            X, f"{save_path}.parquet",
            name
            )
