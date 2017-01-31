# -*- coding: utf-8 -*-
# © 2017 Alessio Gerace
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Checkout Amici di Daniela',
    'category': 'eCommerce',
    'description': """
        This module adds some customizations on checkout form
    """,
    'version': '9.0.1.0.0',
    'author': "Alessio Gerace, Amici di Daniela Onlus",
    "license": "AGPL-3",
    'depends': [
        'website_sale',
        'l10n_it_fiscalcode',
        'website_sale_require_legal'
    ],
    'data': [
        'views/templates.xml'
    ],
    'installable': True,
}
