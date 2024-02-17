# simple-nlp-app

The purpose of this repository is to learn more about deploying a machine learning service in a public cloud provider.
I built a simple sentiment analysis app using FastAPI and a HuggingFace basic model.

**1st step** ✅: I got to deploy it in an EC2 instance! Had some trouble as the free t2.micro intance only has 1GB of RAM so we can't use big models and Pytorch has to be installed without caching.
Also configuring gunicorn and nginx to make it available on the public Internet needed a few shots but got it in the end.

Next step:

🔜Learn more ways to serve it in AWS, probably using Lambda :)


## Getting started

The first step is to download this repo

```bash
git clone https://github.com/miedc/simple-nlp-app.git
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

## Acknowledgements
[@alexmolas](https://github.com/alexmolas) for the idea in this blog and providing the code I used as a base: [A search engine in 80 lines](https://www.alexmolas.com/2024/02/05/a-search-engine-in-80-lines.html)

