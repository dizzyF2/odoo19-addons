from odoo import models, fields


class Patient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    phone = fields.Integer(string="Phone Number")
    