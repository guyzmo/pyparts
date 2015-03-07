# Pyparts

Utility to get information about parts from agregators.

## Usage

    Usage:
      pyparts.py [-k <apikey>] [-t <target>] [-c <config>] [--help] [--version] [--verbose] <command> [<args>...]

    Options:
      -k <apikey>          Gives apikey
      -t <target>          Selects agregator. [default: octopart]
      -c --config <conf>   Use configuration file. [default: ~/.config/pyparts.cfg]
      -h --help            Show this screen.
      --version            Show version.
      --verbose            Show more details.

    Commands:
      lookup         Search part
      specs          Get specs for a part
      datasheet      Download part's datasheet
      open           Open part's page in browser
      help           Give help for a command

    See `pyparts.py help <command>` to get more information on a command

## Install

just do:

    python3 setup.py install

and it'll be available as a shell command:

    % pyparts -h

when the tool will be considered stable enough, I'll upload it to [pipy](https://pypi.python.org/pypi/pyparts):

    % pip install pyparts

## Development

if you just want to develop, you can do:

    % buildout

which will download dependencies and deploy the CLI tool in `bin`:

    % bin/pyparts

You can run regression tests using:

    % bin/test

## Author

Bernard `Guyzmo` Pratz <pyparts at m0g dot net>

## License

    Licensed under GPLv3


