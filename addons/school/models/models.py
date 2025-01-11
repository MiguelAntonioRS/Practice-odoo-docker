# -*- coding: utf-8 -*-

from odoo import models, fields


class Profesor(models.Model):
    _name = 'school.profesor'
    _description = 'profesor'

    name = fields.Char()
