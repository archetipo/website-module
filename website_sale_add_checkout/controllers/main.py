# -*- coding: utf-8 -*-
# © 2017 Alessio Gerace
# License GPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp import _
from openerp.addons.website_sale.controllers.main import website_sale

import werkzeug
from openerp import http

website_sale.mandatory_billing_fields = [
    "name", "phone", "email", "street", "city", "country_id"]
website_sale.optional_billing_fields = [
    "street2", "state_id", "vat", "zip", "fiscalcode", "checkout_company_name"]


class WebsiteSale(website_sale):

    @http.route('/web/get_province', type='http', auth='public', website=True)
    def get_province(self, *args, **kw):
        qcontext = request.params.copy()
        if not qcontext.get('token'):
            raise werkzeug.exceptions.NotFound()
        states = self._get_states(int(qcontext.get('country_id')))
        if states:
            qcontext['states'] = states
            return request.render(
                'website_sale_add_checkout.signup_province', qcontext)
        else:
            return ''

    def _get_states(self, country_id):
        orm_state = request.registry['res.country.state']
        state_ids = orm_state.search(
            request.cr, SUPERUSER_ID, [('country_id', '=', country_id)])
        return orm_state.browse(request.cr, SUPERUSER_ID, state_ids)

    def checkout_form_validate(self, data):
        error, error_message = super(
            WebsiteSale, self).checkout_form_validate(data=data)
        partner_id = request.website.sale_get_order(
            context=request.context).partner_id
        if data['fiscalcode'] == '' and data['vat'] == '':
            error['fiscalcode'] = 'missing'
            error['vat'] = 'missing'
            error_message = error_message.append(
                _(
                    'Un elemento tra Partita IVA e '
                    'Codice Fiscale deve essere presente'
                )
            )
        if request.params['partner_type'] == 'individual':
            if error.get('vat') == 'missing':
                error.pop('vat', None)
            partner_id.write(
                {'company_type': 'person', 'is_company': False})
        elif request.params['partner_type'] == 'company':
            partner_id.write(
                {'company_type': 'company', 'is_company': True})
        elif request.params['partner_type'] == 'association':
            if error.get('vat') == 'missing':
                error.pop('vat', None)
            partner_id.write(
                {'company_type': 'association', 'association': True})
        if request.params['partner_type'] == 'select':
            error["partner_type"] = 'missing'
            error_message.append(_('Please select Partner Type'))
        return error, error_message

    def checkout_values(self, data=None):
        res = super(WebsiteSale, self).checkout_values(
            data=data)
        partner = request.env[
            'res.users'].sudo().browse(request.uid).partner_id
        if partner.company_type == "company":
            res['checkout']['partner_type'] = "company"
        elif partner.company_type == "person":
            res['checkout']['partner_type'] = "individual"
        elif partner.company_type == "association":
            res['checkout']['partner_type'] = "association"
        if data and 'fiscalcode' in data:
            res['checkout']['fiscalcode'] = data['fiscalcode']
        else:
            res['checkout']['fiscalcode'] = partner.fiscalcode
        return res

    def checkout_form_save(self, checkout):
        super(WebsiteSale, self).checkout_form_save(
            checkout=checkout)
        partner_id = request.website.sale_get_order(
            context=request.context).partner_id
        if request.params['partner_type'] == 'individual':
            partner_id.write(
                {'company_type': 'person', 'is_company': False})
        elif request.params['partner_type'] == 'company':
            partner_id.write(
                {'company_type': 'company', 'is_company': True})
        elif request.params['partner_type'] == 'association':
            partner_id.write(
                {'company_type': 'association', 'association': True})
        partner_dict = {'fiscalcode': request.params['fiscalcode']}
        partner_id.write(partner_dict)
