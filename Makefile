export DATA_PATH=data/all.parquet

train-all:
	export SAVE_NAME="results/all.joblib" &&\
		export QUERY="all" &&\
		python scripts/train.py

test-all:
	export SAVE_NAME="results/all.joblib" &&\
		export QUERY="all" &&\
		python scripts/test.py

train-antioquia:
	export SAVE_NAME="results/area_antioquia.joblib" &&\
		export QUERY="zona == 'area_antioquia'" &&\
		python scripts/train.py

test-antioquia:
	export SAVE_NAME="results/area_antioquia.joblib" &&\
		export QUERY="zona == 'area_antioquia'" &&\
		python scripts/test.py

train-caribe:
	export SAVE_NAME="results/area_caribe.joblib" &&\
		export QUERY="zona == 'area_caribe'" &&\
		python scripts/train.py

test-caribe:
	export SAVE_NAME="results/area_caribe.joblib" &&\
		export QUERY="zona == 'area_caribe'" &&\
		python scripts/test.py

train-nordeste:
	export SAVE_NAME="results/area_nordeste.joblib" &&\
		export QUERY="zona == 'area_nordeste'" &&\
		python scripts/train.py

test-nordeste:
	export SAVE_NAME="results/area_nordeste.joblib" &&\
		export QUERY="zona == 'area_nordeste'" &&\
		python scripts/test.py

train-oriental:
	export SAVE_NAME="results/area_oriental.joblib" &&\
		export QUERY="zona == 'area_oriental'" &&\
		python scripts/train.py

test-oriental:
	export SAVE_NAME="results/area_oriental.joblib" &&\
		export QUERY="zona == 'area_oriental'" &&\
		python scripts/test.py

train-suroccidental:
	export SAVE_NAME="results/area_suroccidental.joblib" &&\
		export QUERY="zona == 'area_suroccidental'" &&\
		python scripts/train.py

test-suroccidental:
	export SAVE_NAME="results/area_suroccidental.joblib" &&\
		export QUERY="zona == 'area_suroccidental'" &&\
		python scripts/test.py

train-cens:
	export SAVE_NAME="results/cens.joblib" &&\
		export QUERY="operador == 'cens'" &&\
		python scripts/train.py

test-cens:
	export SAVE_NAME="results/cens.joblib" &&\
		export QUERY="operador == 'cens'" &&\
		python scripts/test.py

train-ceo:
	export SAVE_NAME="results/ceo.joblib" &&\
		export QUERY="operador == 'ceo'" &&\
		python scripts/train.py

test-ceo:
	export SAVE_NAME="results/ceo.joblib" &&\
		export QUERY="operador == 'ceo'" &&\
		python scripts/test.py

train-xm:
	export SAVE_NAME="results/xm.joblib" &&\
		export QUERY="operador == 'xm'" &&\
		python scripts/train.py

test-xm:
	export SAVE_NAME="results/xm.joblib" &&\
		export QUERY="operador == 'xm'" &&\
		python scripts/test.py

train-celsia:
	export SAVE_NAME="results/celsia.joblib" &&\
		export QUERY="operador == 'celsia'" &&\
		python scripts/train.py

test-celsia:
	export SAVE_NAME="results/celsia.joblib" &&\
		export QUERY="operador == 'celsia'" &&\
		python scripts/test.py

train-codensa:
	export SAVE_NAME="results/codensa.joblib" &&\
		export QUERY="operador == 'codensa'" &&\
		python scripts/train.py

test-codensa:
	export SAVE_NAME="results/codensa.joblib" &&\
		export QUERY="operador == 'codensa'" &&\
		python scripts/test.py
