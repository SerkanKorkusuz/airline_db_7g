# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AirlineAlliance(models.Model):
    _name = 'aline_db.alliance'
    description = "Airline Alliance"
    name = fields.Char(string="Name", required=True)
    website = fields.Char(string="Website")
