# Tako Server

## Requirements
* Python 2.7> or Python 3.3 >
* Docker
Docker is needed for running a nginx proxy server which handles the https connections.
```
wget -qO- https://get.docker.com/ | sh
```
* Pip requirements
```
pip install -r ./src/requirements.txt
```

## Running
To run the server:
```
python ./src/app.py
```
