#CS 235 project utilities

This are tools for build, testing, and submitting CS 235 assignments. There is one directory for each assignment.

The supported targets are:
* `all`: compile
* `clean`: erase built and zipped files
* `memcheck`: run with Valgrind
* `quality`: check code-complexity
* `run`: compile and run
* `submit`: submit code and tests to CS 235 submission site
* `test`: compile and run tests
* `zip`: zip code and tests


##Setup

###Python (only necessary for submission)

```
$ sudo pip install mechanize
```

or without admin rights (e.g. CS open labs)

```
$ echo "export PYTHONPATH=/users/guest/j/johnsmith/lib" >> ~/.bashrc
$ sh .bashrc
$ easy_install --install-dir $PYTHONPATH mechanize
```
