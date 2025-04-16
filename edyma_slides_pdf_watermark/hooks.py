def check_pdf_dependencies(cr):
    try:
        import PyPDF2
        import reportlab
    except ImportError:
        raise ImportError(
            "\n[slides_pdf_watermark] Faltan dependencias de Python.\n"
            "Por favor ejecutá:\n\n    pip install PyPDF2 reportlab\n"
        )
