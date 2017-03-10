#!/usr/bin/env python

"""
Freshbooks logger tool.

Usage:
  freshbook init
  freshbook commit [-d DATE] [--hours HOURS] [-m MESSAGE]
  freshbook list [--since SINCE] [--until UNTIL]
  freshbook -h | --help

Commands:
  list                          List time entries. (defaults today)
  commit                        Commit a new time entry.

Options:
  -h --help                     Show this screen.
  -d DATE --date DATE           Date in ISO format, i.e. 2015-09-10 (defaults today)
  -m MESSAGE --message=MESSAGE  Message to attach on the time entry.
  --hours HOURS                 Hours spend on the task (defaults to config task hours)
  --since SINCE                 Since date in ISO format
  --until UNTIL                 Until date in ISO format
"""

from __future__ import print_function
from docopt import docopt

import os
import sys
import json
from datetime import date
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
        status = freshbook.commit(
            project_id=config['project']['id'],
            task_id=config['project']['task']['id'],
            hours=args['--hours'] or config['project']['task']['hours'],
            date=args['--date'] or date.today().isoformat(),
            notes=args['--message'],
        )
        print(status)

    if args['list']:
        entries = freshbook.list(
            project_id=config['project']['id'],
            task_id=config['project']['task']['id'],
            date_from=args['--since'] or date.today().isoformat(),
            date_to=args['--until'] or date.today().isoformat()
        )
        for entry in entries:
            print("[%s]" % entry.date)
            print(entry.notes)
            print(flush=True)


if __name__ == '__main__':
    main()