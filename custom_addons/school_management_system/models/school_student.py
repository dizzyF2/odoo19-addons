from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student information'

    name = fields.Char(string='Student Name', required=True)
    phone_number = fields.Integer(string='Phone Number', required=True)
    date_of_birth = fields.Date(string='Birthday')
    address = fields.Text(string='Address')
    active = fields.Boolean(default=True)

    enrollment_ids = fields.One2many("school.enrollment", "student_id", string="Enrollment ID", required=True)