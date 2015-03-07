#!/usr/bin/env python3

'''\
Pyparts: command line tool to search for parts

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
'''

import sys
import shutil
import logging
import requests
import tempfile
import webbrowser
import subprocess

from docopt import docopt
from os.path import expanduser
from configparser import ConfigParser

from pyoctopart.octopart import Octopart
from pyoctopart.exceptions import OctopartException

def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])

term_size = getTerminalSize()[1]
draw_pbar = lambda seen, size: sys.stdout.write('[{}>{}]\r'.format('-'*int((seen/size)*term_size), ' '*(term_size-int((seen/size)*term_size))))

def download_file(url, filename=None):
    if filename is None:
        filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    size = int(r.headers['Content-Length'].strip())
    seen = 0
    draw_pbar(0, size)
    seen = 1024
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            seen += 1024
            draw_pbar(seen, size)
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return filename

class PyParts:
    def __init__(self, apikey, verbose=False):
        self._e = Octopart(apikey=apikey, verbose=verbose)

    def part_search(self, parts):
        limit = 100
        results = self._e.parts_search(q=parts,
                                       limit=limit)
        start = 0
        hits = results[0]['hits']
        if hits == 0:
            print("No result")
            sys.exit(1)
        print("Searched for: '{}'".format(results[0]['request']['q']))
        def show_result(r):
            print(' → {:30} {:30} {}'.format(
                r['item']['mpn'], r['item']['manufacturer']['name'], r['snippet']
            ))

        for r in results[1]:
            show_result(r)
        while hits - limit > limit:
            start += limit
            hits -= limit
            results = self._e.parts_search(q=parts, limit=limit,
                                            start=start)
            for r in results[1]:
                show_result(r)
        if hits-limit > 0:
            start += limit
            hits -= limit
            results = self._e.parts_search(q=parts,
                                            limit=hits,
                                            start=start)
            for r in results[1]:
                show_result(r)



    def part_specs(self, part):
        result = self._e.parts_match(
            queries=[{'mpn_or_sku': part}],
            exact_only=True,
            show_mpn=True,
            show_manufacturer=True,
            show_octopart_url=True,
            show_short_description=True,
            show_specs=True,
            show_category_uids=True,
            show_external_links=True,
            show_reference_designs=True,
            show_cad_models=True,
            show_datasheets=True,
            include_specs=True,
            include_category_uids=True,
            include_external_links=True,
            include_reference_designs=True,
            include_cad_models=True,
            include_datasheets=True
        )
        if result[1][0]['hits'] == 0:
            print("No result")
            sys.exit(1)
        result = result[1][0]['items'][0]
        print("Showing specs for '{}':".format(result['mpn']))
        print(" → Manufacturer:      {}".format(result['manufacturer']['name']))
        print("  → Specifications:    ")
        for k,v in result['specs'].items():
            name = v['metadata']['name'] if v['metadata']['name'] else k
            min_value = v['min_value'] if v['min_value'] else ''
            max_value = v['max_value'] if v['max_value'] else ''
            unit = ' ({})'.format(v['metadata']['unit']['name']) if v['metadata']['unit'] else ''
            value = ','.join(v['value']) if len(v['value']) > 0 else ''

            if value and not (min_value or max_value):
                print("    → {:20}: {}{}".format(name, value, unit))
            elif value and min_value and max_value:
                print("    → {:20}: {}{} (min: {}, max: {})".format(name, value, unit, min_value, max_value))
            elif not value and min_value and max_value:
                print("    → {:20}:{} min: {}, max: {}".format(name, unit, min_value, max_value))
            elif not value and min_value and not max_value:
                print("    → {:20}:{} min: {}".format(name, unit, min_value))
            elif not value and not min_value and max_value:
                print("    → {:20}:{} max: {}".format(name, unit, max_value))

        print(" → URI:               {}".format(result['octopart_url']))
        if result['external_links']['evalkit_url'] \
                or result['external_links']['freesample_url'] \
                or result['external_links']['product_url']:
            print("  → External Links")
            if result['external_links']['evalkit_url']:
                print("    → Evaluation kit: {}".format(result['external_links']['evalkit_url']))
            if result['external_links']['freesample_url']:
                print("    → Free Sample: {}".format(result['external_links']['freesample_url']))
            if result['external_links']['product_url']:
                print("    → Product URI: {}".format(result['external_links']['product_url']))
        if len(result['datasheets']) > 0:
            print("  → Datasheets")
            for datasheet in result['datasheets']:
                print("    → URL:      {}".format(datasheet['url']))
                if datasheet['metadata']:
                    print("      → Updated:  {}".format(datasheet['metadata']['last_updated']))
                    print("      → Nb Pages: {}".format(datasheet['metadata']['num_pages']))
        if len(result['reference_designs']) > 0:
            print("  → Reference designs: ")
        if len(result['cad_models']) > 0:
            print("  → CAD Models:        ")

    def part_datasheet(self, part, command=None, path=None):
        result = self._e.parts_match(
            queries=[{'mpn_or_sku': part}],
            exact_only=True,
            show_mpn=True,
            show_datasheets=True,
            include_datasheets=True
        )
        if result[1][0]['hits'] == 0:
            print("No result")
            sys.exit(1)
        result = result[1][0]['items'][0]
        print("Downloading datasheet for '{}':".format(result['mpn']))
        try:
            if len(result['datasheets']) > 0:
                for datasheet in result['datasheets']:
                    if not path:
                        path = tempfile.mkdtemp()
                    out = path+'/'+result['mpn']+'-'+datasheet['url'].split('/')[-1]
                    download_file(datasheet['url'], out)
                    print('Datasheet file saved as {}.'.format(out))
                    if command:
                        subprocess.call([command, out])
        finally:
            if not path:
                shutil.rmtree(path)

    def part_show(self, part, printout=False):

        result = self._e.parts_match(
            queries=[{'mpn_or_sku': part}],
            exact_only=True,
            show_mpn=True,
            show_octopart_url=True
        )
        if result[1][0]['hits'] == 0:
            print("No result")
            sys.exit(1)
        result = result[1][0]['items'][0]
        if not printout:
            print("Opening page for part '{}'.".format(result['mpn']))
            webbrowser.open(result['octopart_url'], 2)
        else:
            print("Webpage for part '{}':".format(result['mpn']))
            print("    → URL:      {}".format(result['octopart_url']))

def main():
    args = CLI.parse_args(__doc__)
    args = Config(args['--config']).parse_config(args)

    if args['--verbose']:
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG)

    engine = PyParts(args['-k'], verbose=args['--verbose'])
    try:
        if 'lookup' in args or 'search' in args:
            engine.part_search(args['<part>'])
        elif 'specs' in args:
            engine.part_specs(args['<part>'])
        elif 'datasheet' in args:
            if args['<action>'] == 'open':
                if args['--output']:
                    engine.part_datasheet(args['<part>'], command=args['--command'], path=args['--output'])
                else:
                    engine.part_datasheet(args['<part>'], command=args['--command'])
            elif args['<action>'] == 'save':
                engine.part_datasheet(args['<part>'], path=args['--output'])
        elif 'show' in args:
            engine.part_show(args['<part>'], printout=args['--print'])
    except OctopartException as err:
        print(err)


class Config:
    def __init__(self, config="~/.config/pyparts.cfg"):
        self._conf = ConfigParser()
        self._conf.read(expanduser(config))

    def parse_config(self, args):
        if not args['-k']:
            args['-k'] = '92bdca1b'
        return args


class CLI:
    lookup = """\
Usage: pyparts.py lookup [options] <part>

Options:

    --limit <n>                 Limit number of results
    --show_offers               Show offers
    --show_unauthorized_offers  Show unauthorized offers

"""
    search = lookup.replace('lookup', 'search')
    specs = """\
Usage: pyparts.py specs [options] <part>

Options:
    TODO

"""
    datasheet = """\
Usage: pyparts.py datasheet <part> <action> [options]

Actions:
    open    Open datasheet, but don't save it
    save    Save datasheet

Options:
    --command <cmd>  Command to use for opening. [default: open]
    --output <path>  Path to save the datasheet to. [default: .]

"""
    show = """\
Usage: pyparts.py show [options] <part>

Options:
    --print          Do not open, just printout URL.

"""
    help = __doc__

    @classmethod
    def parse_args(self, doc):
        args = docopt(doc,
                      version='v0.0',
                      options_first=True)
        argv = [args['<command>']] + args['<args>']
        commands = list(filter(lambda x: not x.startswith('_'), dir(CLI)))
        if args['<command>'] in commands:
            arguments = docopt(getattr(CLI, args['<command>']), argv=argv)
            del args['<command>']
            del args['<args>']
            arguments.update(args)
            if args['--verbose']:
                print(arguments)
            return arguments


if __name__ == "__main__":
    main()
