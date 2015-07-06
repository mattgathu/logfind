#! /usr/bin/python
"""
logfind is a simple commandline tool that allows log files scanning without
having to explicitly declare every file on the command line.

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June-July 2015


"""
# ============================================================================
# necessary imports
# ============================================================================
import os
import re
import sys
import argparse
from errno import EACCES, ENOENT

# ============================================================================
# useful constants
# ============================================================================
DEFAULT_LOG_DIR = '/var/log'
DESCRIPTION = """logfind is a simple commandline tool that allows log files
scanning without having to explicitly declare every file on the command line."""
EPILOG = 'Created by Matt Gathu <mattgathu@gmail>'

try:
    PREF_FILES = [exp.strip() for exp in open(os.path.expanduser("~/.logfind"), 'r')]
except OSError as err:
    if err.errno == ENOENT:
        PREF_FILES = None
    else:
        raise err


# ============================================================================
# utility functions
# ============================================================================
def cli_parser():
    """Command Line Arguments parser

    """
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)

    parser.add_argument('term', nargs='+', metavar='SEARCH_TERM', help='search term(s)')
    parser.add_argument('-o', action='store_true',
                        help='use OR logic in finding search terms')

    args = vars(parser.parse_args())

    return args


# ============================================================================
# core functions
# ============================================================================
def term_in_content(term, content, or_flag=False):
    """Filter file line

    """
    if or_flag:
        term = r'|'.join(term)
    else:
        term = '(?=.*' + ')(?=.*'.join(term) + ')'
    regex = re.compile(term, re.IGNORECASE | re.M)
    if regex.search(content):
        return True
    return False


def gen_contents(fnames):
    """Generate file contents

    """
    for name in fnames:
        try:
            yield name, open(name, 'r').read()
        except UnicodeDecodeError:
            continue
        except IOError as err:
            if err.errno == EACCES:
                continue
            else:
                raise err


def gen_log_files():
    """Generate log files"""
    for root, _, files in os.walk(DEFAULT_LOG_DIR):
        for name in files:
            if is_pref_file(name):
                yield os.path.join(root, name)


def is_pref_file(name):
    """Check if filename is a preffered file name

    """
    if not PREF_FILES:
        return True

    for regexp in PREF_FILES:
        if re.search(regexp, name, re.I):
            return True

    return False


def main():
    """logfind main func

    """
    try:
        args = cli_parser()
        term = args['term']
        or_flag = args['o']

        for fname, content in gen_contents(gen_log_files()):
            if term_in_content(term, content, or_flag):
                print(fname)

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
# ============================================================================
# EOF
# ============================================================================
