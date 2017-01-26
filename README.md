# Pyparts

Utility to get information about parts from agregators.

You'll find the sources of the project on https://github.com/guyzmo/pyparts

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

## Example

Below you'll find a few example usage of the tool

### Lookup a part

    % bin/pyparts lookup 'atmega 2560'
    Searched for: 'atmega 2560'
     → ATMEGA2560-16AU                Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 5v 100-pin tqfp
     → ATMEGA2560V8AU                 Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 2.5v/3.3v/5v 100
     → ATMEGA1284P-PU                 Atmel                          mcu, 8bit, <strong>atmega</strong>, 20mhz, dip-40... atmel <strong>atmega</strong>-avr- pdip-40
     → ATSTK600                       Atmel                          ers a quick start into the world of <strong>atmegas</strong> xmegas and design of new application
     → ATMEGA2560V-8CU                Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 2.5v/3.3v/5v 100
     → ATMEGA2560-16AUR               Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 5v 100-pin tqfp 
     → ATMEGA2560V-8AUR               Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 2.5v/3.3v/5v 100
     → ATMEGA2560-16CU                Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 5v 100-pin cbga 
     → ATMEGA2560-16AI                Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560V-8CUR               Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 2.5v/3.3v/5v 100
     → ATMEGA2560V-8AI                Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560-16AU                Adesto Technologies            8bit mcu, 256k flash, 5v, smd, <strong>2560</strong>; timers, no. of:6; bits, no. of:8; fre
     → ATMEGA2560-16CUR               Atmel                          mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 5v 100-pin cbga
     → ATMEGA2560R231-AU              Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560R212-AU              Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560R212-CU              Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560R231-CU              Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560V-8AU                Adesto Technologies            mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 2.5v/3.3v/5v 100
     → ATMEGA256016AU                 Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560V-8CU                Adesto Technologies            mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 2.5v/3.3v/5v 100
     → ATMEGA2560-16CU                Adesto Technologies            mcu 8-bit <strong>atmega</strong> avr risc 256kb flash 5v 100-pin cbga 
     → ATSTK600-ATMEGA2560            Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560                     Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560V-8AU-RET            Atmel                          manufacturer alias: <strong>atmega</strong>
     → D2560AJ                        Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATTD2560AD                     Atmel                          manufacturer alias: <strong>atmega</strong>
     → 2560R03510D                    Atmel                          manufacturer alias: <strong>atmega</strong>
     → MCU CARD ATMEGA2560            mikroElektronika               Board: multiadapter; ATMEGA2560; In the set: prototype
     → 2560-16AU                      Atmel                          manufacturer alias: <strong>atmega</strong>
     → 2560V-8AU                      Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560V-W 11               Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560V-8AI                TE Connectivity                None
     → ATMEGA2560-16AI                TE Connectivity                None
     → ATMEGA2560V-8CUR               TE Connectivity                None
     → ATMEGA2560V-8AUR               TE Connectivity                None
     → ATMEGA2560R212-AU              TE Connectivity                None
     → ATMEGA2560-16CUR               TE Connectivity                None
     → ATMEGA2560R212-CU              TE Connectivity                None
     → ATMEGA2560R231-AU              TE Connectivity                None
     → ATMEGA2560R231-CU              TE Connectivity                None
     → ATMEGA2560-16AUR               TE Connectivity                None
     → ATMEGA2560-16AU SL383          Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATMEGA2560V-8AU SL383          Atmel                          manufacturer alias: <strong>atmega</strong>
     → ATSTK600-ATMEGA2560            TE Connectivity                None

### Get specification for a given part's product name

    % bin/pyparts specs ATMEGA2560-16AUR
    Showing specs for 'ATMEGA2560-16AUR':
     → Manufacturer:      Atmel
      → Specifications:   
        → Number of Pins      : 100
        → Supply Voltage (DC) : (V) min: 4.5
        → Clock Speed         : 16000000.0 (Hz)
        → RoHS                : Compliant
        → RAM Memory Size     : 8192 (byte)
     → URI:               http://octopart.com/atmega2560-16aur-atmel-18611869
      → Datasheets        
        → URL:      http://datasheet.octopart.com/ATMEGA2560-16AUR-Atmel-datasheet-13399453.pdf
          → Updated:  2012-10-04T12:50:24Z
          → Nb Pages: 447
        → URL:      http://datasheet.octopart.com/ATMEGA2560-16AUR-Atmel-datasheet-5357710.pdf
          → Updated:  2007-08-23T10:58:35Z
          → Nb Pages: 448

### Download datasheets for a given part's product name

    % bin/pyparts datasheet ATMEGA2560-16AUR save --output .
    Downloading datasheet for 'ATMEGA2560-16AUR':
    [------------------------------------------------------------------------------------>]
    Datasheet file saved as ./ATMEGA2560-16AUR-ATMEGA2560-16AUR-Atmel-datasheet-13399453.pdf.
    [------------------------------------------------------------------------------------>]
    Datasheet file saved as ./ATMEGA2560-16AUR-ATMEGA2560-16AUR-Atmel-datasheet-5357710.pdf.

### Open the part's webpage in your browser

    % bin/pyparts show ATMEGA2560-16AUR
    Opening page for part 'ATMEGA2560-16AUR'.

## Install

That utility is only compatible with Python3!

just do:

    python3 setup.py install

and it'll be available as a shell command:

    % pyparts -h

when the tool will be considered stable enough, I'll upload it to [pipy](https://pypi.python.org/pypi/pyparts):

    % pip install pyparts

## Configuration

To use the tool you need to get an API key from Octopart for this to work. To do so,
you need to create an account and connect to the [Application registration page](https://octopart.com/api/dashboard) 
at Octopart and register an app (choose whatever name and url you want). From there 
you can copy the API key, e.g. 'ab12cd45' and use it the following way:

    % pyparts -k ab12cd45 lookup 'NE555'

or store it in a config file, to avoid putting the key at each invocation of the tool,
default location being `~/.config/pyparts.cfg`. This file should be an INI
file, with the key stored as the 'apikey' value in the [general] section:

    [general]
    apikey = ab12cd45

or if you want to store your config file elsewhere, you can:

    % pyparts -c ~/.pyparts.cfg lookup 'LM317'

## Development

if you just want to develop, you can do:

    % buildout

which will download dependencies and deploy the CLI tool in `bin`:

    % bin/pyparts

You can run regression tests using:

    % bin/test

## Roadmap

 * [ ] Other aggregator support
 * [ ] Bills of material support
 * [ ] Offers/pricing support
 * [ ] Add tests
 * [x] Configuration file support
 * [x] Octopart support
 * [x] Definition of basic CLI API

## Author

Bernard `Guyzmo` Pratz <pyparts at m0g dot net>

## License

![Under the GPLv3 License](https://www.gnu.org/graphics/gplv3-127x51.png)

    Pyparts, Python utility to lookup and browse parts from commandline
    Copyright (C)2015, Bernard `Guyzmo` Pratz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

