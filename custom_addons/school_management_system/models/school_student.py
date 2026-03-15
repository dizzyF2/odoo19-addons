from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student information'

    name = fields.Char(string='Student Name', required=True)
    age = fields.Integer(string='Age')
    phone_number = fields.Integer(string='Phone Number', required=True)
    address = fields.Text(string='Address')
    active = fields.Boolean(default=True)

    enrollment_ids = fields.One2many("school.enrollment", "student_id", string="Enrollment ID", required=True)
    

    # this one will warn you because you enter invalid data and will not store it in the database
    @api.constrains("age")
    def Check_age(self):
        for rec in self:
            if rec.age < 6 or rec.age > 12:
                raise ValidationError("Age must be between 6 and 12")

    # this one will warn the user but will also store the data in the database
    # @api.onchange("age")
    # def _on_change_age(self):
    #     if self.age < 6 or self.age > 12:
    #         return {
    #             'warning':{
    #                 'title': 'Warning!',
    #                 'message': 'Age must be between 6 and 12'
    #             }
    #         }

    # _sql_constrain = [
    #     # (choose name, operation sql, display message)
    #     ('unique_name','unique(name)','Name is exists'),
    # ]
