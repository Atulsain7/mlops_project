# MLOPS-LOCAL-SETUP-TEMPLATE

A simple template to perform machine learning experiments in local setup with gcp remote setup.
- Keep logs of experiments in postgres database (local setup - in own container).
- Runs Mlflow server in separate container (local setup - in own container)
- Makes Experiment portable (local setup - in own container)
- Stores and version data with DVC.  (GCP Storage)
- Stores Artifacts with Mlflow. (GCP Storage)
