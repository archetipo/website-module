# -*- coding: utf-8 -*-
# © 2017 Alessio Gerace
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).
from openerp import models, api, fields
from openerp import tools


class Event(models.Model):
    _inherit = 'event.event'

    image = fields.Binary(
        "Image", attachment=True,
        help="This field holds the image used as image for "
             "the event, limited to 1024x1024px."
    )
    image_medium = fields.Binary(
        "Medium-sized image", attachment=True,
        help="Medium-sized image of the event. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")

    image_small = fields.Binary(
        "Small-sized image", attachment=True,
        help="Small-sized image of the event. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")

    allow_single_registrant = fields.Boolean(
        string='Allow single registrant')

    message_on_ticket = fields.Html(
        string='Message on ticket confirm')

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(Event, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(Event, self).write(vals)


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    ticket_code = fields.Char(string='Tiket Code')
    code_card = fields.Char(string='Code Card')
    single_registrant = fields.Boolean(string='single registrant')

    @api.model
    def create(self, vals):
        vals['ticket_code'] = self.env[
            'ir.sequence'].next_by_code('registration.code')
        return super(EventRegistration, self).create(vals)
