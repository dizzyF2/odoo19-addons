# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'Course Information'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string="Course Description")
    active = fields.Boolean(default=True)

    enrollment_ids = fields.One2many("school.enrollment", "course_id", string="Enrollment ID", required=True)
