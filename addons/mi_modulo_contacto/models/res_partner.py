from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def generate_contact_pdf(self):
        """
        Method to generate a PDF report for the contact.
        """
        return self.env.ref('contact_pdf_report.contact_pdf_action').report_action(self)