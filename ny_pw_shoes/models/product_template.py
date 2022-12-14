# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    
    _inherit = 'product.template'
    _description = ''
    
    pair_per_case = fields.Integer(string='Pair Per Case', default=0)
    price_per_case = fields.Monetary(string='Price Per Pair', default=0.00)