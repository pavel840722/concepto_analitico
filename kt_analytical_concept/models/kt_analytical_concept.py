# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AnalyticalConcept(models.Model):
    _name = 'analytical.concept'

    name = fields.Char('Name')
    code = fields.Char('Code')

