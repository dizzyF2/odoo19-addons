from odoo import fields,models

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
    ], default="new")


    def action_new(self):
        for rec in self:
            rec.status = "new"

    def action_in_progress(self):
            for rec in self:
                rec.status = "in_progress"

    def action_completed(self):
            for rec in self:
                rec.status = "completed"