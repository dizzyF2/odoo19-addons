from odoo import fields, models


class Timesheet(models.Model):
    _name = 'todo.task.timesheet'

    description = fields.Char()
    hours = fields.Float()
    date = fields.Date()

    task_id = fields.Many2one('todo.task', required=True)

