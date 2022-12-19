# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    property_partner = fields.Many2one(comodel_name = 'res.partner',
                                      string="Property Partner", tracking=1
                                      )
    test_num = fields.Char(string="Test", store=True, default="hello")
