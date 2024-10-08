# Imporoved Albumy - Automatic Caption Generation with BLIP-2 and DETR

This is a ML app based on the open source Albumy Flask web application.

We extended two features:

1. Image caption generation with BLIP-2 pre-trained model.
2. Image keyword search powered by HuggingFace/Facebook's DETR object detection API.

### Source

- Albumy: https://github.com/greyli/albumy.git.
- BLIP-2 from LAVIS: https://github.com/salesforce/LAVIS.
- DETR (ResNet50) from Facebook hosted by HuggingFace: https://huggingface.co/facebook/detr-resnet-50.

## Installation

clone:

```
$ git clone https://github.com/Barry0121/albumy-autocaption.git
$ cd albumy-autocaption
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

---

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

Change the following package to their desired versions:

1. transformers==4.25.0
2. opencv-python==4.8.0.74

After LAVIS is installed, I recommend downloading the pretrained weight yourself (link here: https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_capfilt_large.pth), then change the `model.pretrained` argument in the file `LAVIS/lavis/configs/models/blip_caption_base_coco.yaml` to the relative path to your downloaded weight.

- For example pretrained: "my-path-to/model_base_capfilt_large.pth"

Now your model should load from the local file, instead of downloading.

---

HuggingFace API for Object Detection

Create a file `api-key.key` at the home directory with your HuggingFace API key in it, like this:

```
{
    "key": "[your key]"
}
```

- You can find this key on the model page on HuggingFace (https://huggingface.co/facebook/detr-resnet-50). Click `Deploy` -> `Inference API`, and your key is copiable there.

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
