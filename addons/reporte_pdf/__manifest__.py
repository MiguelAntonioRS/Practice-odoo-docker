{
    'name': 'Contact PDF Export',
    'version': '1.0',
    'summary': 'Store contact details and export them to PDF',
    'author': 'Miguel',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/contact_views.xml',
        'report/contact_report.xml',
    ],
    'installable': True,
    'application': True,
}
