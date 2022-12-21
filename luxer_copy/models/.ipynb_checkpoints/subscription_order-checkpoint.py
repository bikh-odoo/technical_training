# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Subscription(models.Model):
    _inherit = 'account.move'
    
    property_partner = fields.Many2one(comodel_name = 'res.partner', readonly=True)
    