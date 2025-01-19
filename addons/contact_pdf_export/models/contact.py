from odoo import models, fields
from odoo.http import request
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Contact(models.Model):
    _name = 'contact.record'
    _description = 'Contact Record'

    # Campos del modelo
    name = fields.Char(string='Name', required=True)
    contact_type = fields.Selection(
        [('personal', 'Personal'), ('business', 'Business')],
        string='Contact Type',
        required=True
    )
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    tax_id = fields.Char(string='Tax ID')

    # Método para generar el PDF
    def generate_pdf(self):
        # Crear un buffer para almacenar el PDF
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        
        # Agregar datos al PDF
        pdf.drawString(100, 750, f"Contact Name: {self.name}")
        pdf.drawString(100, 730, f"Contact Type: {self.contact_type}")
        pdf.drawString(100, 710, f"Address: {self.address}")
        pdf.drawString(100, 690, f"Phone: {self.phone}")
        pdf.drawString(100, 670, f"Tax ID: {self.tax_id}")
        
        # Guardar y cerrar el PDF
        pdf.save()
        buffer.seek(0)

        # Retornar el archivo como respuesta para descarga
        return request.make_response(
            buffer.getvalue(),
            headers=[
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'attachment; filename={self.name}_contact.pdf')
            ]
        )
