# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    analytical_concept_id = fields.Many2one('analytical.concept', string='Analytical concept')

    def _prepare_account_move_line(self, move=False):
        res = super(PurchaseOrderLine, self)._prepare_account_move_line()
        res['analytical_concept_id'] = self.analytical_concept_id.id
        return res

