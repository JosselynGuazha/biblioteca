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
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/usuarios_view.xml',
        'views/prestamo_view.xml',
        'views/prestamo_bibliotecario_view.xml',
        'views/libro_view.xml',
        'views/publicacion_view.xml',
        'views/tesis_view.xml',
        'views/periodico_view.xml',
        'views/revista_view.xml',
        'views/libro_cd_view.xml',
        'views/autor_view.xml',
        'views/lector_view.xml',
        'views/sancion_view.xml',
        'views/templates.xml',
        'views/menu_view.xml',

    ],
    # only loaded in demonstration mode
    'installable': True,
    'aplication': True,
    'autoinstall': False,
}
