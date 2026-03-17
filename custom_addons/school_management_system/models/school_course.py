# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'Course Information'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string="Course Description")
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ("draft","Draft"),
        ("scheduled","Scheduled"),
        ("start","In Progress"),
        ("done","Completed"),
        ("cancelled","Cancelled"),
    ], default="draft")

    enrollment_ids = fields.One2many("school.enrollment", "course_id", string="Enrollment ID", required=True)

    def action_schechuled(self):
        for rec in self:
            rec.state = "scheduled"
    
    def action_start(self):
        for rec in self:
            rec.state = "start"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancelled"
