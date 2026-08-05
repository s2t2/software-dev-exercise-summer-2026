# Software Development Exercise

## Setup

Clone the repo to download it from GitHub. Perhaps onto the Desktop.

Navigate to the repo using the command line.

```sh
cd ~/Desktop/software-dev-exercise
```

Create a virtual environment:

```sh
conda create -n software-dev-env python=3.11
```

Activate the virtual environment:

```sh
conda activate software-dev-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
```

## Usage

Run RPS game:

```sh
python -m app.rps
```

Run stocks dashboard:

```sh
# option a) pass in the env var at runtime from the command line:
ALPHAVANTAGE_API_KEY="_____" python -m app.stocks

# option b) after we have set up our env var in the ".env" file, run as is:
python -m app.stocks
```


### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# if we have the FLASK_APP=web_app env var in the ".env" file:
flask run

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

Whenever we make updates to our flask web app, we need to restart the web server. We do that by typing `ctrl+c` to stop and `flask run` again to start.

## Testing

Run tests:

```sh
pytest
```
