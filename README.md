# Advent of Code solutions

This project holds my solutions + utilities for **[Advent of Code](https://adventofcode.com/)** puzzles over the years.

## Run it

To run solutions and utilities, first you must install dependencies. I highly recommend using a virtual environment for this. I've been using `pipenv` for that lately.
```sh
pipenv install
# start a new shell within the virtualenv. The shell (and virtualenv) can be exited normally, with `exit` or Ctrl-D.
pipenv shell
```
Once that's done, you can run solutions like so:
```sh
python -m adventofcode run [-y <year>] <day>
```
If the input for the solution you're trying to run hasn't already been saved in the `inputs` directory, the program will try to download it from the Advent of Code site first. If this is your first time downloading an input, you'll be asked to provide your unique session id. It's held in a cookie named `session` saved by the site--you can view it using your browser's dev tools or a number of cookie-viewing browser extensions.

---

To set up input, solution, and test directories for a new year of puzzles, run
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

## Copy it

If you like the setup I've got here, feel free to use it yourself. Or let me know if it's garbage! This is my first time making a proper Python project from scratch, so I'm sure it's not perfect. ¯\\\_(ツ)\_/¯
