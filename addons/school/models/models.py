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
    grade = fields.Selection(
        [
            ('universidad','Universidad'),
            ('maestria','Maestria'),            
        ],
        default="universidad",
        required=True,
    )
    student = fields.One2many("school.student", inverse_name="profesor", string="Student")
    
class Student(models.Model):
    _name = 'school.student'
    _description = 'student'

    name = fields.Char(required=True)
    profesor = fields.Many2one("school.profesor")