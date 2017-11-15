# -*- coding: utf-8 -*-
from odoo import http

# class InvoiceHeaderInherit(http.Controller):
#     @http.route('/invoice_header_inherit/invoice_header_inherit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_header_inherit/invoice_header_inherit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_header_inherit.listing', {
#             'root': '/invoice_header_inherit/invoice_header_inherit',
#             'objects': http.request.env['invoice_header_inherit.invoice_header_inherit'].search([]),
#         })

#     @http.route('/invoice_header_inherit/invoice_header_inherit/objects/<model("invoice_header_inherit.invoice_header_inherit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_header_inherit.object', {
#             'object': obj
#         })