# Jam

Jam is an experimental programming language that tries to combine the advantages of dynamic, interpreted programming languages with those of static, compiled ones. Jam is based on Ruby and Python and tries to provide the same concepts that make those languages great, but supported by a powerful type system to allow the language to compile to native code. Jam compiles to an executable intermediate format called Lekvar, meaning Jam can also be interpreted in much the same way as python.

Currently the compiler is being written in python in the form of a library. The plan is to bootstrap the compiler once the language is capable and then have the compiler become part of the standard library.

## Requirements

### Compiler

The compiler currently requires python3 and the llvm-3.6 shared library

Ubuntu:
```bash
sudo apt-get install python3 llvm-3.6-dev
```

### Tests

In order to run the automated tests for the compiler, the py.test framework is required.

Ubuntu:
```bash
sudo apt-get install python3-pytest
```

### Documentation

For documentation Jam uses Sphinx and thereby requires Sphinx.

Ubuntu:
```bash
sudo apt-get install python3-sphinx
```

## Usage

The compiler is currently built as a python library, however the compiler can also be directly run through the `jam.py` script:

```bash
./jam.py FILE
```

For further help run:

```bash
./jam.py --help
```

## Tests

To run the tests, simply execute py.test

```bash
py.test-3
```

By default the tests are run with a logging level set at `WARNING`. The logging level is bound to the verbosity option. Simply passing in a verbosity of 1 (`-v`) enables `INFO` and 2 (`-vv`) enables `DEBUG`.

```bash
py.test-3 -vv
```

