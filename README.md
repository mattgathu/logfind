## LOGFIND

---
A simple python-based command-line tool that allows log files scanning without having to
explicitly declare every file on the command line.


### Introduction

---
The logfind tool is designed to find all the log files that have at
least one instance of some text by just typing this:

`$ logfind sometext`

The results of this will be a list of all files that have one instance of the
text in them, which can then be passed to another tool if needed.

#### features

+ specifying important files in a ~/.logfind file, using regular expressions.
+ logfind takes any number of arguments as strings to find in those files, and
    assumes you mean AND. So looking for `al has blue eyes` means files
    that have `al AND has AND blue AND eyes` in it.
+ you can pass in one argument, -o (dash oh) and the default is then OR logic instead.


### Installation

---
+ clone this repository.
+ run `python setup.py install`


### License

---
Logfind is distributed under the [MIT license](http://www.opensource.org/licenses/mit-license.php)


### Contributor

---
[Matt Gathu](http://mattgathu.github.io/)
