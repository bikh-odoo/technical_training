# -*- coding: utf-8 -*-

{
    'name': 'Air Flow', 
    'summary': """""", 
    'description': """""", 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'version': '0.1', 
    'depends': ['sale'], 
    'data': [
        'report/sale_report_inherit.xml',
        'views/sale_order_view_inherit.xml',
        'views/account_move_view_inherit.xml',
    ], 
    'license': 'OPL-1'
}