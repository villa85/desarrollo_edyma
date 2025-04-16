# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import io
import base64
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import grey

class SlideWatermarkController(http.Controller):

    @http.route('/my/slide/download/<int:slide_id>', type='http', auth='user', website=True)
    def download_watermarked_slide(self, slide_id, **kwargs):
        slide = request.env['slide.slide'].sudo().browse(slide_id)

        if not slide.exists() or not slide.slide_category == 'document' or not slide.document_binary_content:
            return request.not_found()

        user_name = request.env.user.name

        original_pdf = base64.b64decode(slide.document_binary_content)
        pdf_reader = PdfReader(io.BytesIO(original_pdf))

        filename = f"{slide.name}_by_{user_name.replace(' ', '_')}.pdf"

        if not slide.watermark_enabled:
            return request.make_response(
                original_pdf,
                headers=[
                    ('Content-Type', 'application/pdf'),
                    ('Content-Disposition', f'attachment; filename="{filename}"')
                ]
            )

        # -------------------------
        # CREAR MARCA DE AGUA DIAGONAL (nombre + NIF cruzando la hoja)
        # -------------------------
        watermark_buffer = io.BytesIO()
        can = canvas.Canvas(watermark_buffer, pagesize=letter)
        can.setFont("Helvetica-Bold", 100)
        can.setFillColor(grey)

        # Aplicar transparencia (0.1 = muy tenue, 0.3 = más visible)
        if hasattr(can, "setFillAlpha"):  # Solo si está disponible
            can.setFillAlpha(0.3)

        # Obtener datos del usuario
        user_name = request.env.user.name or ""
        user_vat = request.env.user.vat or ""

        # Construir texto según disponibilidad del NIF
        if user_vat:
            watermark_text = f"{user_name}\nNIF: {user_vat}"
        else:
            watermark_text = f"{user_name}"

        # Mover el origen al centro de la página
        can.translate(306, 396)  # la mitad de letter (612x792)

        # Girar coordenadas 45 grados
        can.rotate(45)

        # Dibujar cada línea centrada
        lines = watermark_text.split('\n')
        line_height = 80
        start_y = (len(lines) - 1) * line_height / 2
        for i, line in enumerate(lines):
            y_offset = start_y - i * line_height
            can.drawCentredString(0, y_offset, line)

        can.save()
        watermark_buffer.seek(0)
        # -------------------------

        watermark_reader = PdfReader(watermark_buffer)
        watermark_page = watermark_reader.pages[0]

        # Fusionar marca con PDF original
        output_pdf = PdfWriter()
        for page in pdf_reader.pages:
            page.merge_page(watermark_page)
            output_pdf.add_page(page)

        output_stream = io.BytesIO()
        output_pdf.write(output_stream)
        output_stream.seek(0)

        filename = f"{slide.name}_by_{user_name.replace(' ', '_')}.pdf"

        return request.make_response(
            output_stream.read(),
            headers=[
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'attachment; filename="{filename}"')
            ]
        )
