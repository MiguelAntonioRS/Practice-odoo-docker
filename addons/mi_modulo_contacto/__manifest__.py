{
    'name': 'Contact PDF Report',
    'version': '16.0.1.0.0',
    'summary': 'Extends the Contacts module to generate PDF reports.',
    'author': 'Miguel',
    'category': 'Tools',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
        'reports/contact_report_templates.xml',
        'reports/contact_report_action.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}