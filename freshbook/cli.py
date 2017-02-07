#!/usr/bin/env python

"""
Freshbooks logger tool.

Usage:
  freshbook init
  freshbook commit [-d DATE] [--hours HOURS] [-m MESSAGE]
  freshbook -h | --help

Options:
  -h --help                     Show this screen.
  --hours HOURS                 Hours spend on the task (defaults to config task hours)
  -d DATE --date DATE           Date in ISO format, i.e. 2015-09-10 (defaults today)
  -m MESSAGE --message=MESSAGE  Message to attach on the time entry.
"""

from __future__ import print_function
from docopt import docopt

import os
import sys
import datetime
import json
from six.moves import input

from . import Freshbook
from .utils import SetupConfig


def main():
    args = docopt(__doc__)

    if args['init']:
        SetupConfig().run()
        sys.exit(0)

    if not os.path.exists(SetupConfig.PATH):
        sys.exit("Run `freshbook init` first.")

    with open(SetupConfig.PATH) as f:
        config = json.load(f)

    freshbook = Freshbook(config['account']['url'], config['account']['token'])

    if args['commit']:

        freshbook.commit(
            project_id=config['project']['id'],
            task_id=config['project']['task']['id'],
            hours=args['--hours'] or config['project']['task']['hours'],
            date=args['--date'] or datetime.date.today().isoformat(),
            notes=args['--message'],
        )


if __name__ == '__main__':
    main()