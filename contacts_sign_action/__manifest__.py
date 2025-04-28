{
    'name': 'Contact Signature Wizard',
    'version': '17.0.1.0.0',
    'description': """
    Este módulo agrega un asistente (wizard) en la vista de contactos que permite seleccionar múltiples contactos y enviarles una plantilla de firma digital basada en el módulo de Firmas Electrónicas de Odoo.

    Características:
    - Botón de acción masiva desde la vista de lista de contactos.
    - Selección de plantilla de firma al abrir el wizard.
    - Envío automático de la solicitud de firma por correo electrónico.
    - Campo booleano "Contract to Send" en el contacto, que se reinicia tras el envío.

    Ideal para procesos donde se requiere gestionar contratos o documentos digitales con múltiples destinatarios de forma eficiente.
    """,
    'category': 'Contacts',
    'license': 'OPL-1',
    'author': "Edyma digital company",
    'website': "http://edyma.net",
    'depends': ['base_setup','contacts', 'sign'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/contact_tree_action.xml',
        'views/sign_template_wizard_form.xml',
    ],
    'installable': True,
    'application': False,
}
