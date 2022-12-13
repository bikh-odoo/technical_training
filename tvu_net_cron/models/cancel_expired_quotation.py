# -*- coding: utf-8 -*-

from odoo import models, fields, api 
from datetime import date


class cancelExpiredQuotation(models.Model):
    _name = "cancel_expired_quotation"
    _description = ""
    
    def _cancel_expired_quotations(self):
        quotations = self.env['sale.order'].search([['state','=','draft'],
                                                   ['validity_date','!=',False],
                                                   ['validity_date','<',date.today()]])
        for quotation in quotations:
            quotation.action_cancel()