# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    analytical_concept_id = fields.Many2one('analytical.concept', string='Analytical concept')

