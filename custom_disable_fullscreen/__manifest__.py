{
    'name': 'Disable Fullscreen eLearning',
    'version': '17.0',
    'category': 'Website',
    'summary': 'Evita que los cursos se abran en pantalla completa por defecto',
    'author': "Edyma digital company",
    'website': "http://edyma.net",
    'depends': ['website_slides'],
    'assets': {
        'web.assets_frontend': [
            'custom_disable_fullscreen/static/src/js/slides_course_slides_list.js',
        ],
    },
    'installable': True,
    'application': False,
}
