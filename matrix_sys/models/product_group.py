# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Group(models.Model):
    _name = 'matrix.group'
    _description = 'Groups Info'
    
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')