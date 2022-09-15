# Python Patient IPFS uploader

## Requirements

### Python:
``` BASH
[packages]
flask = "*"
pymysql = "*"
python-dotenv = "*"
flask-bcrypt = "*"
requests = "*"
flask-dotenv = "*"
ipfshttpclient = "==0.8.0a1"
[requires]
python_version = "3.10"
```
NOTE: You <b>MUST</b> use <i>ipfahttpclient</i> version 0.8.0a1 for python code to work!

### IPFS:
IPFS Command Line Interface (CLI) must be installed locally for this application to run. Here is where you can download it:
https://docs.ipfs.tech/install/command-line/#official-distributions
After installing IPFS locally, run:
```
ipfs daemon
```
NOTE: You <b>MUST</b> run `ipfs daemon` everytime before running the local server.

### Python virtual environment
Make sure you have Python `pipenv` installed before running the virtual environment!!! If you would like to download this python virtual environment: https://pipenv.pypa.io/en/latest/install/
NOTE: If `pip install` does not work (it means pip is not in your PATH), try replacing this with `python -m pip install` or `python3 -m pip install`.
Within the project root directory, run:
```
python -m pipenv install flask, pymysql, python-dotenv, flask-bcrypt, requests, flask-dotenv, ipfshttpclient==0.8.0a1

python -m pipenv shell

python server.py
```

PS. I know there are different ways to run a virtual environment. If you are confortable with another way, do that instead.

NOTE: if `python -m` does not work, check your python version: `python --version`.
MAC: if you use a Mac, and `python -m` gives an error, try replacing with: `python3 -m`.
