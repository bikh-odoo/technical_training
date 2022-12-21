# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    property_partner = fields.Many2one(comodel_name = 'res.partner')
    def _create_invoices(self): 
        so = super(SaleOrder, self)._create_invoices()
        so['property_partner'] = self.property_partner
        
        # _logger.info(a.search_read([]))
        # _logger.info(type(a))
        return so
    
    
    
    
    
    @api.onchange('property_partner')
    def _onchange_property_partner(self):
        if self.property_partner:
            self.partner_shipping_id = self.property_partner
        else:
            self.partner_shipping_id = self.partner_id