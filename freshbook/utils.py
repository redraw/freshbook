from __future__ import print_function

import json
from six.moves import input
from collections import namedtuple

from . import Freshbook


Option = namedtuple('Option', 'id name')


class SetupConfig(object):

    PATH = '.freshbook'

    def __init__(self):
        self.account = input('> Account URL: ')
        self.token = input('> Token: ')

        self.fb = Freshbook(self.account, self.token)

    def select_project(self):
        options = [Option(p.project_id, p.name) for p in self.fb.get_projects()]

        print('-- Projects --')
        option = self._select(options)

        return options[option]

    def select_task(self, project_id):
        options = [Option(t.task_id, t.name) for t in self.fb.get_tasks(project_id)]

        print('-- Tasks --')
        option = self._select(options)

        return options[option]

    @staticmethod
    def _select(options):
        for i, option in enumerate(options):
            print('['+str(i)+']', option.name)

        while True:
            value = input('> Select: ') or -1
            idx = int(value)

            if 0 <= idx <= len(options) - 1:
                break
            else:
                print('Wrong option')

        return idx

    def run(self):
        project = self.select_project()
        task = self.select_task(project.id)

        task_hours = input('> %s default hours: ' % task.name)

        # Create config file
        with open(self.PATH, 'w+') as f:
            data = {
                'account': {
                    'url': self.account,
                    'token': self.token
                },
                'project': {
                    'id': str(project.id),
                    'name': str(project.name),
                    'task': {
                        'name': str(task.name),
                        'id': str(task.id),
                        'hours': task_hours
                    }
                }
            }
            json.dump(data, f, indent=4)

        print('Configuration file created.')
