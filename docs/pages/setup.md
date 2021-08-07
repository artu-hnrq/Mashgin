# Project Setup
Let's get this app running!

[-0]: https://github.com/artu-hnrq/mishmash_kitchen "Project Repo"


## Getting started
### Requirements
It will be necessary to have `Git` and `Python` installed
```shell
$ git --version
git version 2.25.1
$ python --version
Python 3.8.5
```

Additionally, `Bash` and `Make` will allow you to get further
```shell
$ echo $BASH_VERSION
5.0.17(1)-release
$ make --version
GNU Make 4.2.1
```

### Installation
First of all, clone [this repo][-0] locally
```shell
$ git clone git@github.com:artu-hnrq/mishmash_kitchen.git
```

### Development environment
Then, to set up development environment, go inside the downloaded folder and run
```shell
$ make init
$ . venv/bin/activate
``` 
