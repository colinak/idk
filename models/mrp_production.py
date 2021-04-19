# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    _description = 'Ordenes de Produccion'

    @api.depends('origin')
    def _compute_order_ref(self):
        order_ref = self.env['sale.order'].search([
            ('name', '=', self.origin)    
        ])
        _logger.info("Order: " + str(order_ref))
        ref_order = self.env['mrp.production'].search([
            ('name', '=', self.origin)    
        ])
        _logger.info("REF: " + str(ref_order))
        if order_ref.client_order_ref != False:
            _logger.info("IF: " + str(order_ref))
            self.order_ref = order_ref.client_order_ref
        elif ref_order != False:
            _logger.info("ELIF: " + str(ref_order))
            self.order_ref = ref_order.order_ref

    
    order_ref = fields.Char(
        string="Referencia de Cliete",
        compute="_compute_order_ref",
        store=True,
        readonly=False,
        help="N° de Referencia del Cliente"
    )
