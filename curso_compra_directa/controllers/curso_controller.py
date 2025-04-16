from odoo import http
from odoo.http import request

class CursoShopController(http.Controller):

    @http.route(['/curso/compra-directa'], type='http', auth='public', website=True)
    def compra_directa(self, product_id=0, **kw):
        try:
            product_id = int(product_id)

            # Buscar si el ID corresponde a una variante directa
            product = request.env['product.product'].sudo().search([('id', '=', product_id)], limit=1)

            # Si no existe, buscar como plantilla y obtener primera variante
            if not product:
                template = request.env['product.template'].sudo().search([('id', '=', product_id)], limit=1)
                if template and template.product_variant_ids:
                    product = template.product_variant_ids[0]

            # Si aún así no se encuentra nada válido
            if not product:
                return request.redirect('/shop')

            # Crear o recuperar el carrito
            order = request.website.sale_get_order(force_create=True)
            order._cart_update(product_id=product.id, add_qty=1)

            return request.redirect('/shop/address')

        except Exception as e:
            return request.redirect('/shop')
        
        # http://localhost:10016/curso/compra-directa?product_id=38
        # http://escuela.inversor.in/curso/compra-directa?product_id=6