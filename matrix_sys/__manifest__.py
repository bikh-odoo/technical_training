# -*- coding: utf-8 -*-

{
    'name': 'Matrix System', 
    'summary': """""", 
    'description': """
    """, 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'version': '0.1', 
    'depends': ['sale'], 
    'data': [
        'security/matrix_security.xml',
        'security/ir.model.access.csv',
        'views/matrix_group.xml',
        'views/matrix_menuitems.xml',
        'views/product_view_inherit.xml',
        'views/product_sequence.xml',
    ], 
    'demo': [
        'demo/matrix_demo.xml',
    ],
    'license': 'OPL-1'
}