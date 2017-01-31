# -*- coding: utf-8 -*-
# © 2017 Alessio Gerace
# License GPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, fields


class EventTicket(models.Model):
    _inherit = 'event.event.ticket'

    code_card = fields.Char(string='Code Card Label')
    use_code_card = fields.Boolean(
        string='Code card required')
    single_registrant = fields.Boolean(
        string='Allow single registrant', dafault=False)
