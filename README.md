# Vlab Bailer

This is a command line tool that allows Fly (Virtual Lab) users to push users into a new form manually, by reading from a CSV file.

## Installation

Please make sure you have Python 3 and pipx installed.

Install vlab_bailer with:

``` shell
pipx install git+https://github.com/vlab-research/vlab-bailer.git
```

After which you should have the command `vlab_bailer` globally available on your command line.


## Usage

The CSV file must have the following format:

| column name | column type |
|-------------|-------------|
| user        | string      |
| page        | string      |
| shortcode   | string      |


vlab_bailer takes the following arguments:

`-p` which should be the path to your CSV file
`-s` which is the integer row number of your CSV that it should start at (starts from 0)
`-l` which is the last row of your CSV that it should run up to (starts from 0, this row is not included)

In other words, the bailer will run for [s, l) rows.

For example, this runs the entire CSV:

``` shell
vlab_bailer -p myfile.csv
```

This runs the first 10 rows:

``` shell
vlab_bailer -p myfile.csv -l 10
```

This runs all rows after the first ten rows:

``` shell
vlab_bailer -p myfile.csv -s 10
```
