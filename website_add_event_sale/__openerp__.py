# -*- coding: utf-8 -*-
# © 2017 Alessio Gerace
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Event Sale Customizations by Amici di Daniela Onlus",
    "version": "9.0.1.0.0",
    "author": "Alessio Gerace, Amici di Daniela Onlus",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "Customize events",
    "depends": [
        'website_event_sale',
        'website_add_event',
    ],
    "data": [
        'views/templates.xml',
        'views/event_view.xml',
    ],
    "auto_install": False,
    'installable': True,
}
