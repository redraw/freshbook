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
        return self.client.time_entry.create(
            time_entry=dict(
                project_id=project_id,
                task_id=task_id,
                **kwargs
            )
        )
