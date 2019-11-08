# -*- coding: utf-8 -*-
{
    'name': "Biblioteca",

    'summary': """
        Sistema Bibliotecario del ISTLA""",

    'description': """
        Sistema desarrollado para el Control de la Biblioteca
    """,

    'author': "Josselyn G. y Albert M.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sistema Bibliotecario',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/prestamo_view.xml',
        'views/libro_view.xml',
        'views/informacion_view.xml',
        'views/templates.xml',
        'views/menu_view.xml',

    ],
    # only loaded in demonstration mode
    'installable': True,
    'aplication': True,
    'autoinstall': False,
}
