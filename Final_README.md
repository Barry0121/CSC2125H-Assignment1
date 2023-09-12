# Assignment 1 - Albumy ML App

## Installation

clone:

```
$ git clone https://github.com/Barry0121/CSC2125H-Assignment1.git
$ cd CSC2125H-Assignment1
```

create & activate virtual env then install dependency:

with venv/virtualenv + pip:

```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

or with Pipenv:

```
$ pipenv install --dev
$ pipenv shell
```

**Note**: For users using 3.9 and later version of Python, make sure the dependency `pillow==8.0` or later versions. Otherwise, the installation might fail.

generate fake data then run:

```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```

- All generated data is viewable with an SQL interface in the file `data-dev.db`.

Test account:

- email: `admin@helloflask.com`
- password: `helloflask`
