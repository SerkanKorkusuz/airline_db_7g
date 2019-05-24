# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Airline(models.Model):
    _name = 'aline_db.airline'
    description = "Airline"
    name = fields.Char(string="Name", required=True)
    airline_id = fields.Many2One('res.partner', string="Airline", required=True)
    country_id = fields.Many2One(string="Country", related='airline_id.country_id', readonly=True, store=True)
    iata_member = fields.Boolean(string="IATA Membership")
    alliance = fields.Many2One('aline_db.alliance', string="Alliance")
    service_type = fields.Selection(string="Service Type", selection=[('a', 'Low Cost'),
                                                                      ('b', 'Premium Charter'),
                                                                      ('c', 'Standard'),
                                                                      ('d', 'Domestic'),
                                                                      ('e', 'Charter')])
    flag_carrier = fields.Boolean(string="Flag Carrier")
    aircraft_no = fields.Integer(string="Number of Aircraft")
    revenue_total = fields.Float(string="Total Revenue")
    revenue_ancillary = fields.Float(string="Ancillary Revenue")

    # airline_id değişiminde country_id güncellemesi
    @api.onchange('airline_id')
    def _onchange_country_id(self):
        self.country_id = self.airline_id.country_id
        """return {
            'warning': {
                'title': "Wait",
                'message': "Wait",
            }
        }"""
