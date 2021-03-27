# midrusnlp

This is MidRusNLP.

## How to run Web part without Docker

Install NPM dependencies:

```bash
cd hseling-web-midrusnlp; npm install .; cd ..
```

Create venv and install Python dependencies for Web part:

```bash
cd hseling-web-midrusnlp
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
cd ..
```

To run Web Application:

```bash
export HSELING_RPC_ENDPOINT=http://localhost:5000/rpc/
export PYTHONPATH=hseling-web-midrusnlp
python3 hseling-web-midrusnlp/hseling_web_midrusnlp/main.py
deactivate
```

## How to run API/RPC part without Docker

Create venv and install Python dependencies for Web part:

```bash
cd hseling-api-midrusnlp
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
cd ..
```

To run RPC server:

```bash
PYTHONPATH=hseling-lib-midrusnlp:hseling-api-midrusnlp python hseling-api-midrusnlp/hseling_api_midrusnlp/main.py
```


## Docker containers



Build and run composed docker environment:

    docker-compose build
    docker-compose up
    
To stop your environment press C-c or:

    docker-compose stop

## Checking your application

Check if your API container started successfully:

    curl http://localhost:5000/healthz

Now you can use curl to check RPC endpoints at localhost:5000:

    curl -XPOST -H "Content-type: application/json" -d '{"id": 1, "method": "list_files", "params": []}' http://localhost:5000/rpc/

You can navigate to main web application using this link:

    open http://localhost:8000/web/

## License

MIT License. See LICENSE file.
