# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConfirmRfq(models.Model):
    _name = "mindesa_cron.confirm_rfq"
    
    def _confirm_rfq(self):
        purchase_orders = self.env['purchase.order'].search([['partner_id','=',1],['create_uid','=',1]])
        for purchase_order in purchase_orders:
            purchase_order.button_confirm()
            