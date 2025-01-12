# -*- coding: utf-8 -*-

from odoo import models,fields


class Profesor(models.Model):
    _name = 'school.profesor'
    _description = 'profesor'

    name = fields.Char(required=True)
    description = fields.Text()
    age = fields.Integer(required=True)
    bornDate = fields.Date(string="Birthdate")
    salary = fields.Float()
    status = fields.Boolean()