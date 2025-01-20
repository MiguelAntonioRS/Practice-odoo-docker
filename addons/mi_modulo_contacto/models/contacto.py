from odoo import models, fields, api

class Contacto(models.Model):
    _inherit = 'res.partner'

    pdf_generated = fields.Boolean(string="PDF Generado", default=False)

    def action_generate_pdf(self):

        self.ensure_one()
        return self.env.ref('mi_modulo_contacto.contacto_pdf_report').report_action(self)
