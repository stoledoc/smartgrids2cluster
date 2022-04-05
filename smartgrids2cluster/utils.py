from smartgrids2cluster.datamodels import EnvironmentVariables as _EnvironmentVariables
import os as _os

def get_env_vars() -> _EnvironmentVariables:
    return _EnvironmentVariables(
            data_path=_os.environ["DATA_PATH"],
            save_name=_os.environ["SAVE_NAME"],
            query=_os.environ["QUERY"]
            )
