# -*- coding: utf-8 -*-
# © 2017 Alessio Gerace
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).
from openerp import models, api


class Website(models.Model):
    _inherit = 'website'

    @api.multi
    def sale_get_order(self, force_create=False, code=None,
                       update_pricelist=None, context=None):
        res = super(Website, self).sale_get_order(
            force_create=force_create, code=code,
            update_pricelist=update_pricelist, context=context)
        return res if res is not None else self.env['sale.order']
