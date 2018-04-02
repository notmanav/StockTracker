#!/usr/local/bin/python2.7
# encoding: utf-8
'''
EntryPoint -- shortdesc

EntryPoint is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2018 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from StocksValueFetcher import StockPrice

__all__ = []
__version__ = 0.1
__date__ = '2018-03-29'
__updated__ = '2018-03-29'


def main(argv=None): # IGNORE:C0111
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)


    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_name, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        parser.add_argument("-s", "--stocks", dest="stocks", help="set comma or space separated list of stocks")
        parser.add_argument('-V', '--version', action='version', version=program_version_message)

        # Process arguments
        args = parser.parse_args()
        stocks=None
        if args.stocks:
            stocks=args.stocks
        StockPrice().fetchStocks(stocks)
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2



if __name__ == "__main__":
    sys.exit(main())