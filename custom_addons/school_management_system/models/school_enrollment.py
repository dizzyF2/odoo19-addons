# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolCourse(models.Model):
    _name = 'school.enrollment'
    _description = 'Enrollment Information'

    enrollment_date = fields.Date(string='enrollment Date', default=fields.Date.today())
    grade = fields.Float(string='Grade')
    active = fields.Boolean(default=True)

    student_id = fields.Many2one("school.student", string="Student ID", required=True)
    course_id = fields.Many2one("school.course", string="Course ID", required=True)
