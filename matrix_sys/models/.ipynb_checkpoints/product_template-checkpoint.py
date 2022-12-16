# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = ''
    
    product_group = fields.Many2one(comodel_name='matrix.group',
                                   string='Product Group',
                                   ondelete='set null')
    
    @api.onchange('product_group')
    def _onchange_product_group(self):
        product_group_name = self.product_group.name
        self.barcode = self.product_group.name[:2] + '.' + self.env['ir.sequence'].next_by_code('product.group.sequence')
    
