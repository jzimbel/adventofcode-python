# Advent of Code solutions

This project holds my solutions + utilities for **[Advent of Code](https://adventofcode.com/)** puzzles over the years.

## Run it

To run solutions and utilities, first you must install dependencies. I highly recommend using a virtual environment for this. I've been using `pipenv` for that lately.
```sh
pipenv install
```
Once that's done, you can run solutions (while your virtualenv is activate) like so:
```sh
python -m adventofcode run [-y <year>] <day>
```

---

To set up solution and test directories for a new year of puzzles, run
```sh
python -m adventofcode init [-y <year>]
```
The year param is optional in both of the `adventofcode` commands, and if not specified the latest year listed in the solutions directory (or latest year + 1 for `init`) is used.  
Note: this command's output will be nicer if you have the `tree` shell command installed!

## Test it

Assuming you've installed dependencies as described above, you can run tests with the following:
```sh
# run all tests
PYTHONPATH=$(pwd) py.test
# run a specific test
PYTHONPATH=$(pwd) py.test path/to/test.py
```

If you like the setup I've got here, feel free to use it yourself. Or let me know if it's garbage! This is my first time making a proper Python project from scratch, so I'm sure it's not perfect. ¯\\\_(ツ)\_/¯
