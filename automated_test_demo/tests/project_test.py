# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import odoo.tests


class ProjectTest():

    def test_project_creation(self):
        # Create a new project with the test
        test_project = self.env['project.project'].sudo().create({
            'name': 'TestProject'
        })

        # Add a test task to the project
        test_project_task = self.env['project.task'].sudo().create({
            'name': 'ExampleTask',
            'project_id': test_project.id
        })

        # Check if everything is fine
        self.assertEqual(test_project.name, 'TestProject')
        self.assertEqual(test_project_task.name, 'ExampleTask')
        self.assertEqual(test_project_task.project_id, test_project_task.id)
        print('This is a succes')