# speech-server

## Installation

To set up the environment, follow these steps:

1. Create a virtual environment and install the required packages:

    ```bash
    python3.11 -m venv server
    source server/bin/activate
    pip install -r requirements.txt
    ```

    - If you are using the Nemo-based ASR model, use the following requirements file:

    ```bash
    pip install -r requirements_wx_nemo.txt
    ```

2. Add the following lines to `server/bin/activate` to ensure that the necessary libraries are accessible:

    ```bash
    export LD_LIBRARY_PATH=/path/to/environment/server/lib64/python3.11/site-packages/nvidia/cublas/lib:/path/to/environment/server/lib64/python3.11/site-packages/nvidia/cudnn/lib
    ```

    If you are using the Nemo version, also add the following:

    ```bash
    export CPATH=$HOME/python-dev/include:$CPATH
    ```

3. If Java 11.0 is not installed, set up the Java environment variables. Add the following to `server/bin/activate`:

    ```bash
    export JAVA_HOME=/path/to/java/installation/jdk-11.0.16.1+1
    export PATH=$JAVA_HOME/bin:$PATH
    ```

Make sure to replace `/path/to/environment/` and `/path/to/java/installation/` with the actual paths to your environment and Java installation.

## Files Description

- `whisperx_model.py`: Contains the model definition.
- `whisperx_handler.py`: Handles data input/output operations.
- `archive.sh`: Used to create the `.mar` file for the model in the `model_store` folder.
- `config*.json`: Configuration for corresponding models.

## Model Update Process

To update the model:

1. **Always archive the model first** by running:

    ```bash
    ./archive.sh
    ```

2. After archiving, **start the server** by running:

    ```bash
    ./start_server.sh
    ```

To stop the server, run:

```bash
./stop_server.sh

