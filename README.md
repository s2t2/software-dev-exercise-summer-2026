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

## Testing

Run tests:

```sh
pytest
```
