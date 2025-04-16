{
    'name': 'POS Receipt Style Customizer',
    'version': '17.0.1.0',
    "license": "OPL-1",
    'category': 'Sales/Point of Sale',
    'author': 'Edyma',
    'website': 'https://edyma.net/',
    'summary': 'Customize font and size of the POS ticket receipt.',
    'description': (
        'This module modifies the appearance of the Point of Sale receipt by changing '
        'its font type and size for improved readability and branding.'
    ),
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'edyma_custom_pos_ticket/static/src/**/*',
        ],
    },
    'images': [],
    'installable': True,
}
