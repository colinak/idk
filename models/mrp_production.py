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
        ref_order = self.env['mrp.production'].search([
            ('name', '=', self.origin)    
        ])
        if order_ref.client_order_ref != False:
            self.order_ref = order_ref.client_order_ref
        elif ref_order != False:
            self.order_ref = ref_order.order_ref



    @api.depends('name', 'origin')
    def _compute_root_origin(self):
        origin = self.env['sale.order'].search([
            ('name', '=', self.origin)    
        ])
        order = self.env['mrp.production'].search([
            ('name', '=', self.origin)    
        ])
        if origin.name:
            self.root_origin = self.name
        elif not origin.name and order != False:
            root = False
            derivation = order.origin
            origin = None
            while root == False:
                order_production = self.env['mrp.production'].search(
                    [('name', '=', derivation)]
                )
                if order_production.name == False:
                    if origin:
                        self.root_origin = origin
                    else:
                        self.root_origin = self.origin
                    root = True
                else:
                    origin = order_production.name
                    derivation = order_production.origin


        
    order_ref = fields.Char(
        string="Referencia de Cliete",
        compute="_compute_order_ref",
        store=True,
        readonly=False,
        help="N° de Referencia del Cliente"
    )
    root_origin = fields.Char(
        string=u"Origen Raíz",
        compute="_compute_root_origin",
        store=True,
    )
