# -*- coding: utf-8 -*-

from odoo import models, fields

class AccountInvoice(models.Model):
    _inherit='account.move'
    
    project_manager = fields.Char(string="Project Manager", readonly=True)
    project_name = fields.Char(string="Project Name", readonly=True)
    
    ship_date = fields.Date(string="Ship Date")
    shipping_method = fields.Selection([('option1','Way 1'),('option2', 'Way 2'),('option 3', 'Way 3')])
    
    