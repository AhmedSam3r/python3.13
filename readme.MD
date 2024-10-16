# Release notes

[What’s New In Python 3.13](https://docs.python.org/3/whatsnew/3.13.html)

# Installation Requirements
1. python 3.13
2. pyenv
3. python3.13t
4. pypy3 

# Instalation process on ubuntu 22

## Python 3.13
sudo apt install python3.13

## pyenv
- `sudo apt update`
- `sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git`
- `git clone https://github.com/pyenv/pyenv.git ~/.pyenv`
- add the following in `~/.bashrc,`
    ```
    # Add pyenv to PATH
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"

    # Initialize pyenv
    eval "$(pyenv init --path)"
    ```
- `source ~/.bashrc`
## python 3.13-dev free threading enabled
- pyenv install --list | grep 3.13
- pyenv install 3.13-dev

## pypy
- sudo apt install pypy3
- pypy3 -m venv venv_pypy
- source venv_pypy/bin/activate  # On Windows, use `venv_pypy\Scripts\activate`
- pypy3 your_script.py


# Acknowledgement 

[Special thanks to Arjan for The New Python 3.13 Is FINALLY Here!
](https://www.youtube.com/watch?v=eUDGlxu_-ic)
