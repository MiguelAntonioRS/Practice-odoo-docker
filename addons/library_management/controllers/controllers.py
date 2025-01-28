# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryManagement(http.Controller):
#     @http.route('/library_management/library_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_management/library_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_management.listing', {
#             'root': '/library_management/library_management',
#             'objects': http.request.env['library_management.library_management'].search([]),
#         })

#     @http.route('/library_management/library_management/objects/<model("library_management.library_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_management.object', {
#             'object': obj
#         })
