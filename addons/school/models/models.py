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
    signature = fields.Many2many(model_name="school.signature", relation_name="schools.signatures"
                                 column1="school_id", column2="signature_id")
    
class Student(models.Model):
    _name = 'school.student'
    _description = 'student'

    name = fields.Char(required=True)
    profesor = fields.Many2one("school.profesor")
    
class Signature(models.Model):
    _name = 'school.signature'
    _description = 'signature'

    name = fields.Char(required=True)