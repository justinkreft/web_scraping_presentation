define PROJECT_HELP_MSG

Usage:
    make help                   -- show this message    \n
    make clean                  -- remove intermediate files (see CLEANUP)    \n
    make ${VENV}                -- make a virtualenv in the base directory (see VENV)    \n
    make python-reqs            -- install python packages in requirements.pip    \n
    make build                  -- build models / containers    \n
    make git-config             -- set local git configuration    \n
    make setup                  -- make python-reqs build git-config   \n
    make start-notebook          -- launch a jupyter server from the local virtualenv    \n
endef
export PROJECT_HELP_MSG

help:
	echo $$PROJECT_HELP_MSG | less

git-config:
	git init
	git config --local core.page 'less -x4'

VENV = .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}
${VENV}:
	python3 -m venv $@

python-reqs: requirements.pip | ${VENV}
	pip install --upgrade -r requirements.pip

build:
	python -m spacy download en_core_web_md

setup: python-reqs git-config build | ${VENV}

start-notebook:
	jupyter notebook --config=jupyter_notebook_config.py

CLEANUP = *.pyc

clean:
	rm -rf ${CLEANUP}

.PHONY: help git-config start-jupter python-reqs setup clean
