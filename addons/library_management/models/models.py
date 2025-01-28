from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', 'The ISBN must be unique!')
    ]

    name = fields.Char(string='Book Name', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    author = fields.Char(string='Author')
    publication_date = fields.Date(string='Publication Date')
