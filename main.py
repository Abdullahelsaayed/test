from odoo import http
from odoo.http import request


class Register(http.Controller):
    @http.route('/register', type="http", auth="public", website=True)
    def register_attendee(self, **kw):
        # events = request.env['ev'].search([])
        #
        # values = {
        #
        #     'products': products
        #
        # }
        return http.request.render('event_custom.register_form', {})

    @http.route('/create/attendee', type="http", auth="public", website=True)
    def create_attendee(self, **kw):
        print('sdffffff')
        request.env['event.registration'].sudo().create(kw)
        return request.render('event_custom.create_attendee', {})
