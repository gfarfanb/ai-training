
# Hugging Face NPL Course

## Installation

Install Ubuntu packages for Python Virtual Environments
```sh
sudo apt install python3-venv
```

[Install Node.js on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04)

Create Virtual Environment (**venv**)
```sh
cd ~/courses
# Create course directory
mkdir huggingface
# Create 'venv'
python -m venv .env
# Activate 'venv'
source .env/bin/activate
# Confirm if 'venv' is active
which python
# /home/<USER>/courses/huggingface/.env/bin/python
```

Install python dependencies
```sh
pip install transformers
```

Activate **venv**
```sh
cd ~/courses/huggingface
source .env/bin/activate
```

Once **venv** is activated you can deactivate it by typing in the terminal
```sh
deactivate
```

# Practical Deep Learning for Coders

## Installation

Install python dependencies
```sh
pip install fastai
pip install jupyterlab
pip install ipywidgets
pip install notebook
pip install voila
```


## Run JupyterLab

Once **venv** is activated you can run
```sh
jupyter-lab
# Open http://127.0.0.1:8888/lab?token=...
```

## References

[Practical Deep Learning for Coders](https://fastai.github.io/fastbook2e/)