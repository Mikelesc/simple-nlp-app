# simple-nlp-app

The purpose of this repository is to learn more about deploying a machine learning service in a public cloud provider.
I built a simple sentiment analysis app using FastAPI and Jinja2. Actually most of the code comes from this repo: https://github.com/alexmolas/microsearch
I just adapted it to use a HuggingFace model on the input.

NEXT STEP:

Learn how to deploy it using AWS. I know there are EC2 instances, Lambda functions, Kubernetes... I want to test them all!


## Getting started

The first step is to download this repo

```bash
git clone https://github.com/Mikelesc/simple-nlp-app.git
```

Then, I recommend you install everything in a virtual environment. I use the included manager that comes with most Python versions: “venv”.

```bash
py -3.10 -m venv .venv
```

activate the environment

```bash
.venv\Scripts\activate
```

and install the package and the dependencies

```bash
pip install -r requirements.txt
```

## Launch app

Run


```bash
python -m app
```

and if you navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) you'll be able write a sentence.

