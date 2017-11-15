# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class invoice_header_inherit(models.Model):
#     _name = 'invoice_header_inherit.invoice_header_inherit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100