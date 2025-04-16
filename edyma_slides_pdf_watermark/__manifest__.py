{
    'name': 'Slides PDF Watermark',
    'version': '17.0',
    "license": "OPL-1",
    'summary': 'Marca de agua con nombre del usuario al descargar PDFs en eLearning',
    'author': 'Edyma',
    'category': 'eLearning',
    'pre_init_hook': 'check_pdf_dependencies',
    'depends': ['website_slides'],
    'data': [
        'views/slide_resource_downloadable.xml',
        'views/slide_course_template_download_button.xml',
        'views/embed_slide_download_override.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
