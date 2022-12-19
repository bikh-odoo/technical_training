# -*- coding: utf-8 -*-
 

from odoo import models, fields, api

class Subscription(models.Model):
    _inherit = 'account.move'
    _description = ''
    
    
    property_partner_sale_order = fields.Many2one(comodel_name='sale.order',
                                                 string="Propery Partner Inherit",
                                                 ondelete='set null')
    print("this is prooperty partner ", property_partner_sale_order)
    
    
    
    property_partner = fields.Many2one(related='property_partner_sale_order.partner_id', string="Ppty Partner", readonly=False)
    
    
    
    # @api.onchange('property_partner')
    # def _onchange_property_partner(self):
    #     print("inside the onchange ", self.property_partner)