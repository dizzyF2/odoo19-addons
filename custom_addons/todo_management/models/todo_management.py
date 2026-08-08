from odoo import fields,models, api
from odoo.exceptions import ValidationError

class TodoManagement(models.Model):
    _name = 'todo.task'
    _description = 'Todo Management'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char(string="Task Name")
    description = fields.Text(string="Description")
    assign_to = fields.Many2one(comodel_name="res.partner", string="Assign To", tracking=True) #relation field with res.partner
    due_date = fields.Datetime(string="Due Date")
    is_overdue = fields.Boolean(
        string="Overdue",
        compute="_compute_is_overdue",
        store=True,
    )
    status = fields.Selection([
        ("new","New"),
        ("in_progress","In Progress"),
        ("completed","Completed"),
        ("closed","Closed")
    ], default="new")
    estimated_time = fields.Float(string="Estimated Time (hours)")
    active = fields.Boolean(default=True)

    timesheet_line_ids = fields.One2many('todo.task.timesheet', 'task_id', string='Timesheets')



    def action_new(self):
        for rec in self:
            rec.status = "new"

    def action_in_progress(self):
            for rec in self:
                rec.status = "in_progress"

    def action_completed(self):
            for rec in self:
                rec.status = "completed"

    def action_closed(self):
            for rec in self:
                rec.status = "closed"

    def _cron_check_overdue(self):
        tasks = self.search([])
        tasks._compute_is_overdue()

    @api.depends("due_date", "status")
    def _compute_is_overdue(self):
        now = fields.Datetime.now()
        for rec in self:
            rec.is_overdue = (
                bool(rec.due_date)
                and rec.due_date < now
                and rec.status not in ("completed", "closed")
            )

    @api.constrains('timesheet_line_ids', 'estimated_time')
    def _check_total_time(self):
        for rec in self:
            total = sum(rec.timesheet_line_ids.mapped("hours"))
            if total > rec.estimated_time:
                raise ValidationError(
                    "Total timesheet hours cannot exceed the estimated time."
                    )