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

## Example

```
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
% bin/pyparts datasheet ATMEGA2560-16AUR save --output .
Downloading datasheet for 'ATMEGA2560-16AUR':
[------------------------------------------------------------------------------------>]
Datasheet file saved as ./ATMEGA2560-16AUR-ATMEGA2560-16AUR-Atmel-datasheet-13399453.pdf.
[------------------------------------------------------------------------------------>]
Datasheet file saved as ./ATMEGA2560-16AUR-ATMEGA2560-16AUR-Atmel-datasheet-5357710.pdf.
% bin/pyparts show ATMEGA2560-16AUR
Opening page for part 'ATMEGA2560-16AUR'.
```

## Author

Bernard `Guyzmo` Pratz <pyparts at m0g dot net>

## License

    Licensed under GPLv3


