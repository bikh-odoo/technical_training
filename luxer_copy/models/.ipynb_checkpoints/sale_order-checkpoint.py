# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = ''
    
    property_partner = fields.Many2one(comodel_name = 'res.partner',
                                      string="Property Partner",
                                      ondelete='set null')