#!/bin/make
SHELL := /bin/bash

API_ROOT := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

DJANGO_ADMIN ?= $(PYTHON) $(API_ROOT)/manage.py

# If supplied `PYTHON` variable does not correspond to
# an executable script, set it to use virtual environment
ifeq (1,$(shell [[ -x "$(PYTHON)" ]] && echo 0 || echo 1))
	VENV_ROOT ?= venv
	PYTHON = $(VENV_ROOT)/bin/python3
endif


init:: veryclean $(API_ROOT)/requirements.txt
	[[ -n "$(VENV_ROOT)" ]] && [[ ! -d "$(VENV_ROOT)" ]] && python3 -m venv $(VENV_ROOT)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r $(API_ROOT)/requirements.txt
	$(PYTHON) -m pip freeze

run:: compile prepare ## Run backend services
	$(DJANGO_ADMIN) runserver 0:8000

prepare:: ## Prepare database to execution
	$(DJANGO_ADMIN) migrate

compile:: ## Process source code into an executable program
	$(DJANGO_ADMIN) collectstatic --no-input
	$(DJANGO_ADMIN) makemigrations

test:: ## Test application
	$(DJANGO_ADMIN) test

clean:: reset_migrations
	- rm -fr $(API_ROOT)/static
	- rm -f $(API_ROOT)/db.sqlite3

reset_migrations:: ## Delete all Django apps' migrations
	find $(API_ROOT) -path "**/migrations/*.py" -not -name "__init__.py" -delete
	find $(API_ROOT) -path "**/migrations/*.pyc"  -delete

veryclean:: clean
	- rm -fr $(VENV_ROOT)
	find $(API_ROOT) -iname "*.pyc" -iname "*.pyo" -delete
	find $(API_ROOT) -name "__pycache__" -type d -exec rm -rf {} +


.EXPORT_ALL_VARIABLES:
.ONESHELL:
.PHONY: init run prepare compile test clean reset_migrations veryclean
