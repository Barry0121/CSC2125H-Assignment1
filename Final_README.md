# Assignment 1 - Albumy ML App

This is a ML app based on the open source Albumy Flask web application.

We extended two features:

1. Image caption generation with BLIP-2 pre-trained model.
2. Image keyword search powered by YOLOv7 object detection.

### Cite

- Albumy: https://github.com/greyli/albumy.git.
- BLIP-2 from LAVIS: https://github.com/salesforce/LAVIS.
- YOLOv7: https://github.com/WongKinYiu/yolov7/tree/main.

## Installation

clone:

```
$ git clone https://github.com/Barry0121/CSC2125H-Assignment1.git
$ cd CSC2125H-Assignment1
```

---

create & activate virtual env then install dependency:

with venv/virtualenv + pip:

```
$ python -m venv env

# use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS

$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

or with Pipenv:

```
$ pipenv install --dev
$ pipenv shell
```

**Note**: For users using 3.9 and later version of Python, make sure the dependency `pillow==8.0` or later versions. Otherwise, the installation might fail.

You will also need to install `LAVIS` from salesforce for image captioning. `LAVIS` has some dependency issue with M1 MacOS, so we have to clone the package from GitHub and install it in out environment ourselves.

##### Method 1: Remove dependencies with decord by hand

GitHub link: https://github.com/salesforce/LAVIS.

Credit to this solution: https://github.com/salesforce/LAVIS/issues/15#issuecomment-1435669192.

steps:

1. Clone the repo: `$ git clone https://github.com/salesforce/LAVIS.git`.
2. Remove import and dependency of `decord` in `LAVIS/dataset_card/lavis/datasets/data_utils.py`, and then remove it from `requirements.txt`.
3. Install the package with `pip install -e .`.

- This method will disable some of the features from LAVIS, but BLIP and image captioning should still be functional.

##### Method 2: Install decord

Credit to this solution: https://github.com/salesforce/LAVIS/issues/15#issuecomment-1441359380.

steps:

1. Install ffmpeg@4 (needed for decord): `brew install cmake ffmpeg`.

2. install decord from source code (Check here: https://github.com/dmlc/decord).

3. Install LAVIS from source code (check the LAVIS github readme).

---

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

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
