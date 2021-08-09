#!/bin/make
SHELL := /bin/bash

APP_ROOT := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

NPM ?= /usr/bin/npm --prefix $(APP_ROOT)


init:: veryclean $(APP_ROOT)/package-lock.json
	$(NPM) ci

start test build::
	$(NPM) run $@

clean::
	- rm -fr $(APP_ROOT)/build

veryclean:: clean
	- rm -fr $(APP_ROOT)/node_modules


.EXPORT_ALL_VARIABLES:
.ONESHELL:
.PHONY: init start test build clean veryclean
