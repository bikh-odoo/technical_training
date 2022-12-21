# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit='sale.order'
    
    project_manager = fields.Char(string="Project Manager")
    project_name = fields.Char(string="Project Name")
    
    
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['project_manager'] = self.project_manager
        invoice_vals['project_name'] = self.project_name
        return invoice_vals