# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    
    _inherit = 'product.template'
    _description = ''
    
    pair_per_case = fields.Integer(string='Pair Per Case', help='this is a helper', default=0)
    price_per_case = fields.Monetary(string='Price Per Pair', default=0.00)
    
    
    @api.onchange('pair_per_case', 'price_per_case')
    def _onchange_sales_price(self):
        if self.pair_per_case < 0:
            raise UserError('Pair per case cannot be less than 0')
        if self.price_per_case < 0.00:
            raise UserError('Price cannot be less than $0.00')
            
        self.list_price = self.price_per_case * self.pair_per_case
        
    
        