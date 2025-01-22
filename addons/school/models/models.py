# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
    signature = fields.Many2many(comodel_name="school.signature", relation_name="schools_signatures",
                                 column1="school_id", column2="signature_id",)
    
class Student(models.Model):
    _name = 'school.student'
    _description = 'student'

    name = fields.Char(required=True)
    profesor = fields.Many2one("school.profesor")
    notes_id = fields.One2many("school.note", "student_id")
    
class Signature(models.Model):
    _name = 'school.signature'
    _description = 'signature'

    name = fields.Char(required=True)
    profesor = fields.Many2many(comodel_name="school.profesor", relation_name="schools_signatures",
                                 column1="signature_id", column2="school_id",)
    notes_ids = fields.One2many("school.note", "signature_id", string="Notes")
    students_ids = fields.Many2many("school.student", string="Students", compute="_compute_student_id")
    
    @api.depends("notes_ids", "notes_ids.student_id")
    def _compute_student_id(self):
        for signature in self:
            signature.students_ids = signature.notes_ids.mapped("student_id")
    
class Note(models.Model):
    _name = 'school.note'
    _description = 'Note'

    student_id = fields.Many2one("school.student", string="Student", required=True)
    signature_id = fields.Many2one("school.signature", string="Signature", required=True)
    note = fields.Float(string="Note")
    status = fields.Char(string="Status", compute="_compute_status")
    
    @api.depends("note")
    def _compute_status(self):
        for record in self:
            if record.note >= 6.0:
                record.status = "Won"
            else:
                record.status = "Loss"    