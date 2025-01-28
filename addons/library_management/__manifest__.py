{
    'name': 'Library Management',
    'version': '16.0.1.0.0',
    'summary': 'Basic library management module',
    'description': 'A module to manage books for a library system.',
    'author': 'Miguel',
    'company': 'Grupo Hernández S.U.R.L',
    'category': 'Education',
    'website': 'https://www.grupohernandez.cu',
    'license': 'OPL-1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'data/library_book_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
