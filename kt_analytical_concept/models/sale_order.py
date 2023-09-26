# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    analytical_concept_id = fields.Many2one('analytical.concept', string='Analytical concept')

    def _prepare_invoice_line(self, move=False):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['analytical_concept_id'] = self.analytical_concept_id.id
        return res
