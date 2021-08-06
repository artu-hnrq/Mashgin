#!/bin/make
SHELL := /bin/bash
GNUMAKEFLAGS += --no-print-directory

REPO_ROOT := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

PROJECT_NAME ?= $(lastword $(subst /, ,$(REPO_ROOT)))

-include .env
-include */Makefile
ifneq (,$(wildcard ./.makerc))
	include .makerc
endif


%: # Treat unrecognized targets
	@ echo "$(PROJECT_NAME): No rule to '$(*)'."
	echo "Use 'make help' to check available ones."

help: ## Show this help
	@ echo "Available targets in $(PROJECT_NAME):"
	egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[37;1m%-20s\033[0m %s\n", $$1, $$2}'

init:: veryclean ## Configure environment
	@ if [[ ! -f .env ]] && [[ -f .env.example ]]; then \
    	cp --no-target-directory .env.example .env; \
    fi
	touch .env

clean:: ## Delete all generated files

veryclean:: ## Uninstall environment completely
	rm -f .env


require_env = [[ -z "$($1)" ]] \
	&& echo "$1 environment variable must to be set" && exit 1 \
	|| echo "$1 = $($1)";


.EXPORT_ALL_VARIABLES:
.ONESHELL:
.PHONY: help init clean veryclean
