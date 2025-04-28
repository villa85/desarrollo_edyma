from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    contract_to_send = fields.Boolean(
        string='Contract to Send',
        default=False,
        help='Indicates whether this contact has a contract to send.'
    )
