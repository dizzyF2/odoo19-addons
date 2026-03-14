# -*- coding: utf-8 -*-
from odoo import fields, models


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'

    name = fields.Char(string='Name')
    date = fields.Date(string="Date")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
