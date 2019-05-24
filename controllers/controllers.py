# -*- coding: utf-8 -*-
from odoo import http

# class AirlineDb7g(http.Controller):
#     @http.route('/airline_db_7g/airline_db_7g/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/airline_db_7g/airline_db_7g/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('airline_db_7g.listing', {
#             'root': '/airline_db_7g/airline_db_7g',
#             'objects': http.request.env['airline_db_7g.airline_db_7g'].search([]),
#         })

#     @http.route('/airline_db_7g/airline_db_7g/objects/<model("airline_db_7g.airline_db_7g"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('airline_db_7g.object', {
#             'object': obj
#         })