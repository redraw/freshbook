# -*- coding: utf-8 -*-
from refreshbooks import api


class Freshbook(object):

    def __init__(self, account, token):
        self.client = api.TokenClient(account, token)

    def get_projects(self):
        response = self.client.project.list()
        return [p for p in response.projects.project]

    def get_tasks(self, project_id):
        response = self.client.task.list(project_id=project_id)
        return [t for t in response.tasks.task]

    def commit(self, project_id, task_id, **kwargs):
        response = self.client.time_entry.create(
            time_entry=dict(
                project_id=project_id,
                task_id=task_id,
                **kwargs
            )
        )
        return response.get('status')

    def list(self, project_id, task_id, date_from=None, date_to=None):
        payload = dict(
            project_id=project_id,
            task_id=task_id,
            date_from=date_from,
            date_to=date_to
        )

        response = self.client.time_entry.list(**payload)
        total = response.time_entries.get('total')

        if int(total) == 0:
            raise StopIteration

        while True:
            for entry in response.time_entries.time_entry:
                yield entry

            page = response.time_entries.get('page')
            pages = response.time_entries.get('pages')

            if int(page) == int(pages):
                raise StopIteration

            payload['page'] = int(page) + 1
            response = self.client.time_entry.list(**payload)
