# speech-server
## Installation

To set up the environment, follow these steps:

1. Create a virtual environment and install the required packages:

    ```bash
    python3.11 -m venv server
    source server/bin/activate
    pip install -r requirements.txt
    ```

2. Add the following line to `server/bin/activate` to ensure that the necessary libraries are accessible:

    ```bash
    export LD_LIBRARY_PATH=/path/to/environment/server/lib64/python3.11/site-packages/nvidia/cublas/lib:/path/to/environment/server/lib64/python3.11/site-packages/nvidia/cudnn/lib
    ```

3. If Java 11.0 is not installed, set up the Java environment variables. Add the following to `server/bin/activate`:

    ```bash
    export JAVA_HOME=/path/to/java/installation/jdk-11.0.16.1+1
    export PATH=$JAVA_HOME/bin:$PATH
    ```

Make sure to replace `/path/to/environment/` and `/path/to/java/installation/` with the actual paths to your environment and Java installation.
