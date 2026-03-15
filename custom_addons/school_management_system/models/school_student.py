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
    

    @api.constrains("age")
    def Check_age(self):
        for rec in self:
            if rec.age < 6 or rec.age > 12:
                raise ValidationError("Age must be between 6 and 12")
