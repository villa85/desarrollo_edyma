# models/slide_slide.py
from odoo import models, fields

class SlideSlide(models.Model):
    _inherit = "slide.slide"

    watermark_enabled = fields.Boolean(string="Watermark")
