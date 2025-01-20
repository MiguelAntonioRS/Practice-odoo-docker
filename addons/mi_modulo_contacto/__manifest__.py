{
    'name': 'Módulo de Contacto PDF',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Generar PDF desde los contactos',
    'author': 'Miguel',
    'depends': ['base', 'contacts', 'report'],
    'data': [
        'views/contacto_views.xml',
        'reports/contacto_report.xml',
    ],
    'installable': True,
    'application': True,
}
