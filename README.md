aliyun no captcha
==================================================

## install virtualenv

```shell
$ pip install virtualenv
$ virtualenv -p `which python3` ~/py3env
```

## active your virtual environment

```shell
$ source ~/py3env/bin/activate
```

The presence of the environment name (py3env) in the prompt:

```
(py3env) ➜  ~
```

## test

set up environments

see .envrc_template

```shell
$ make install

fill up event.json

$ python local.py
```

## To exit from the virtual environment

```shell
$ deactivate
```
