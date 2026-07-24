# -*- coding: utf-8 -*-
from odoo import api,fields,models

class TodoManagement(models.Model):
    _name = 'todo.task'
    _description = 'Todo Management'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char(string="Task Name")
    description = fields.Text(string="Description")
    assign_to = fields.Many2one(comodel_name="res.partner", string="Assign To", tracking=True) #relation field with res.partner
    due_date = fields.Datetime(string="Due Date")
    status = fields.Selection([
        ("new","New"),
        ("in_progress","In Progress"),
        ("completed","Completed")
    ])



    