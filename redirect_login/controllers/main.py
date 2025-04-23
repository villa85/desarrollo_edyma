from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
from werkzeug.utils import redirect as werkzeug_redirect  # ← renombramos solo la función

class CustomLoginRedirect(Home):

    @http.route('/web/login', type='http', auth="public", website=True, sitemap=False)
    def web_login(self, redirect=None, **kw):  # ← mantenemos firma original
        response = super().web_login(redirect=redirect, **kw)  # ← usamos el nombre del parámetro correctamente

        if request.session.uid:
            return werkzeug_redirect("https://escuela.inversor.in/")  # ← sin conflicto de nombres

        return response





