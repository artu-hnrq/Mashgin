#!/bin/make
SHELL := /bin/bash

DOCS_ROOT := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
DIST_ROOT ?= $(DOCS_ROOT)/_docs

MKDOCS_FLAGS += --config-file $(DOCS_ROOT)/mkdocs.yml

# If supplied `PYTHON` variable does not correspond to
# an executable script, set it to use virtual environment
ifeq (1,$(shell [[ -x "$(PYTHON)" ]] && echo 0 || echo 1))
	VENV_ROOT ?= venv
	PYTHON = $(VENV_ROOT)/bin/python3
endif


init:: veryclean $(DOCS_ROOT)/requirements.txt
	[[ -n "$(VENV_ROOT)" ]] && [[ ! -d "$(VENV_ROOT)" ]] && python3 -m venv $(VENV_ROOT)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install --requirement $(DOCS_ROOT)/requirements.txt
	$(PYTHON) -m pip freeze

docs:: ## Build documentation
	mkdocs build $(MKDOCS_FLAGS)

read:: ## Serve documentation
	mkdocs serve $(MKDOCS_FLAGS) --dev-addr 0.0.0.0:1111

publish:: ## Publish documentation into Github Pages
	mkdocs gh-deploy $(MKDOCS_FLAGS) --force --message "Update documentation"

clean::
	- rm -rf $(DIST_ROOT)

veryclean:: clean
	- rm -fr $(VENV_ROOT)


.EXPORT_ALL_VARIABLES:
.ONESHELL:
.PHONY: init docs read publish clean veryclean
