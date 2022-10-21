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

### MYSQL/Open Dental:
Open Dental is the dental practice management software we are pulling from in order to get our patient data. There is a web app trial version of Open Dental that you can dowload here:
https://www.opendental.com/trial.html

Once downloadeed you should be able to get into your MySQL schemas with:
```
mysql -u ADMINUSER -p
PASSWORD

use demo;

select * from patient limit 1;
```

NOTE: 'ADMINUSER' is always 'root' and PASSWORD is always 'root' when you download the mysql scripts inside the trial version of Open Dental developer download.
If the above commands do NOT work for you, you will have to back up all your schemas inside of your mysql user, then delete mysql entirely, then redownload Open Dental Trial Version.

### IPFS:
IPFS Command Line Interface (CLI) must be installed locally for this application to run. Here is where you can download it:
https://docs.ipfs.tech/install/command-line/#official-distributions
After installing IPFS locally, run:
```
ipfs daemon
```
NOTE: You <b>MUST</b> run `ipfs daemon` everytime before running the local server.

### Python virtual environment
Make sure you have Python `pipenv` installed before running the virtual environment!!! If you would like to download this python virtual environment: 
https://pipenv.pypa.io/en/latest/install/

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

## TODO:
Add the password section to the user schema.
