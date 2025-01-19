# -*- coding: utf-8 -*-
# from odoo import http


# class ReportePdf(http.Controller):
#     @http.route('/reporte_pdf/reporte_pdf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reporte_pdf/reporte_pdf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reporte_pdf.listing', {
#             'root': '/reporte_pdf/reporte_pdf',
#             'objects': http.request.env['reporte_pdf.reporte_pdf'].search([]),
#         })

#     @http.route('/reporte_pdf/reporte_pdf/objects/<model("reporte_pdf.reporte_pdf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reporte_pdf.object', {
#             'object': obj
#         })
