from odoo import models, fields, _
from odoo.exceptions import ValidationError
from odoo.fields import Command

class SignContactWizard(models.TransientModel):
    _name = 'sign.contact.wizard'
    _description = 'Wizard to select signature template'

    contact_ids = fields.Many2many('res.partner', string="Contacts")
    template_id = fields.Many2one('sign.template', string="Signature Template", required=True)


    def action_send_for_signature(self):
        self.ensure_one()

        if not self.template_id.sign_item_ids:
            raise ValidationError(_("La plantilla seleccionada no contiene campos para firmar."))

        # Obtener los roles únicos requeridos por la plantilla
        roles = self.template_id.sign_item_ids.mapped('responsible_id')

        if not roles:
            raise ValidationError(_("La plantilla debe tener al menos un rol definido."))

        if len(roles) > 1:
            raise ValidationError(_("La plantilla tiene múltiples roles, y este asistente solo soporta uno por ahora."))

        role = roles[0]

        for partner in self.contact_ids:
            if not partner.email:
                continue

            sign_request = self.env['sign.request'].create({
                'template_id': self.template_id.id,
                'reference': f"Firma para {partner.name}",
                'request_item_ids': [Command.create({
                    'partner_id': partner.id,
                    'role_id': role.id,
                })]
            })

            partner.contract_to_send = False
            
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _("Firmas enviadas"),
                'message': _("Se han enviado documentos a los contactos seleccionados."),
                'type': 'success',
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'}
            }
        }









