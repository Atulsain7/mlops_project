from pathlib import Path
from random import random
import os

import mlflow


def main():
    mlflow.set_tracking_uri("http://mlflow-server:5000")
    experiment_name = "playground"

    try:
        mlflow.create_experiment(experiment_name)
    except mlflow.exceptions.RestException:  # type: ignore
        pass

    mlflow.set_experiment(experiment_name)
    gcs_artifact_uri = os.getenv("MLFLOW_DEFAULT_ARTIFACT_ROOT")
    with mlflow.start_run() as run:
        mlflow.log_param("test", 13)

        mlflow.log_metric("foo", random())
        mlflow.log_metric("foo", random() + 1)
        mlflow.log_metric("foo", random() + 2)

        # Define the name of the artifact file
        artifact_filename = "tmp.txt"

        # Construct the full path within the 'mlflow/artifacts' directory
        artifact_path = gcs_artifact_uri
        # artifact_path = os.path.join("mlflow/artifacts", artifact_filename)

        # Write content to the artifact file
        with open('/tmp/example.txt', 'w') as file:
            # Write content to the file
            file.write('Hello, this is a simple text file.\n')
            file.write('Here is another line of text.\n')

        # Log the artifact to MLflow
        mlflow.log_artifact("/tmp/example.txt")


if __name__ == "__main__":
    main()