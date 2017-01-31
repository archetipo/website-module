# -*- coding: utf-8 -*-
# © 2017 Alessio Gerace
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.http import request
from openerp.addons.website_event_sale.controllers.main \
    import website_event
# from openerp.addons.website_event_sale.controllers.main import website_event


class WebsiteEventAdd(website_event):

    def _process_tickets_details(self, data):
        ticket_post = {}
        for key, value in data.iteritems():
            if not key.startswith('nb_register') or '-' not in key:
                continue
            items = key.split('-')
            if len(items) < 2:
                continue
            ticket_post[int(items[1])] = int(value)
        tickets = request.registry['event.event.ticket'].browse(
            request.cr, request.uid, ticket_post.keys(), request.context)
        return [
            {
                'id': ticket.id,
                'single_registrant': ticket.single_registrant,
                'code_card_desc': ticket.code_card,
                'use_code_card': ticket.use_code_card,
                'name': ticket.name,
                'quantity': ticket_post[ticket.id],
                'price': ticket.price,
                'message': ticket.event_id.message_on_ticket or ''
            } for ticket in tickets if ticket_post[ticket.id]]
