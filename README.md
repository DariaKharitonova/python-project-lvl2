#  Generator of Difference
___
The training project on the Python Software Development course on [Hexlet.io](https://ru.hexlet.io/professions/python)

[![Github Actions Status](https://github.com/DariaKharitonova/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/DariaKharitonova/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0ff4b228a29585c0b927/maintainability)](https://codeclimate.com/github/DariaKharitonova/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0ff4b228a29585c0b927/test_coverage)](https://codeclimate.com/github/DariaKharitonova/python-project-lvl2/test_coverage)
[![Actions Status](https://github.com/DariaKharitonova/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/DariaKharitonova/python-project-lvl2/actions)
___

Gendiff is a CLI-utility defining the difference between two files.
___
#### Install package
For install:
```bash
pip3 install git+https://github.com/DariaKharitonova/python-project-lvl-2
```
#### Run to help
You can run package and to see parameters as:
```bash
gendiff - h
```
```bash
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
[![asciicast](https://asciinema.org/a/1jEhdNSpplOpD6YI8sH3VP9Rp.svg)](https://asciinema.org/a/1jEhdNSpplOpD6YI8sH3VP9Rp)
#### Run diff
For compare simple or recursive files YAML and JSON formats:
```bash
gendiff first_file second_file
```
[![asciicast](https://asciinema.org/a/lEmLD1AlaaaTEYMCnm7JzIy9R.svg)](https://asciinema.org/a/lEmLD1AlaaaTEYMCnm7JzIy9R)
#### Output format
You can also choose flat or json format to represent the result:
```bash
gendiff first_file second_file --format=plain
```
[![asciicast](https://asciinema.org/a/Q8LOIoSKzqzrmhJyKYrSisHs2.svg)](https://asciinema.org/a/Q8LOIoSKzqzrmhJyKYrSisHs2)
```bash
gendiff first_file second_file --format=json
```
[![asciicast](https://asciinema.org/a/qv8H6gzHrawiOeUcXfVerOHWB.svg)](https://asciinema.org/a/qv8H6gzHrawiOeUcXfVerOHWB)
#### Tests
For run tests, enter:
```bash
make test
```
