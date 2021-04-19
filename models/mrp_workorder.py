# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'
    _description = 'Ordenes de Trabajo'


    # Asignar Orden de Regerencia y Orden de Produccion
    def action_origin(self):
        if self.production_id:
            root = False
            derivation = self.production_id.origin
            origin = None
            while root == False:
                order_production = self.env['mrp.production'].search(
                    [('name', '=', derivation)]
                )
                if order_production.name == False:
                    if origin:
                        self.origin = origin
                        
                        ref_order = self.env['sale.order'].search(
                            [('name', '=', derivation)]
                        )
                        self.order_ref = ref_order.client_order_ref

                        root = True
                    else:
                        self.origin = self.production_id.name

                        ref_order = self.env['sale.order'].search(
                            [('name', '=', derivation)]
                        )
                        self.order_ref = ref_order.client_order_ref

                        root = True
                else:
                    origin = order_production.name
                    derivation = order_production.origin
                    _logger.info("Ori: " + str(origin))


    @api.depends('origin')
    def _compute_order_ref(self):
        if self.origin:
            order_ref = self.env['sale.order'].search([
                ('name', '=', self.origin)    
            ])
            self.order_ref = order_ref.client_order_ref


    # root_origin = fields.Char(
        # string=u"Origen Raíz",

    # )

    origin = fields.Char(
        string="Orden de Producción",
        # compute=_compute_origin,
        help="Referencia al documento principal que genero esta orden de trabajo."
    )
    order_ref = fields.Char(
        string="Referencia Interna",
        # related="production_id.order_ref",
        help="Referencia Interna de la Orden de la Orden de Venta del Cliente"
    )

