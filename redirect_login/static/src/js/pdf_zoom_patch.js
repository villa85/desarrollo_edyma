
odoo.define('slides_pdf_zoom_override.PDFSlidesViewerPatch', function (require) {
    "use strict";

    if (window.PDFSlidesViewer) {
        const OriginalViewer = window.PDFSlidesViewer;

        class ExtendedViewer extends OriginalViewer {
            constructor(...args) {
                super(...args);
                this.pdf_zoom = 3; // Zoom inicial más amigable
                this._setupZoomControls();
                this._setupMouseWheelZoom();
                this._setupKeyboardNav();
            }

            zoomIn() {
                this.pdf_zoom = Math.min(this.pdf_zoom + 0.25, 4);
                this.queueRenderPage(this.pdf_page_current);
            }

            zoomOut() {
                this.pdf_zoom = Math.max(this.pdf_zoom - 0.25, 0.5);
                this.queueRenderPage(this.pdf_page_current);
            }

            _setupMouseWheelZoom() {
                this.canvas.addEventListener('wheel', (e) => {
                    if (e.ctrlKey) {
                        e.preventDefault();
                        e.deltaY < 0 ? this.zoomIn() : this.zoomOut();
                    }
                });
            }

            _setupKeyboardNav() {
                document.addEventListener('keydown', (e) => {
                    switch (e.key) {
                        case '+':
                        case '=':
                            this.zoomIn();
                            break;
                        case '-':
                        case '_':
                            this.zoomOut();
                            break;
                        case 'ArrowRight':
                            this.nextPage();
                            break;
                        case 'ArrowLeft':
                            this.previousPage();
                            break;
                    }
                });
            }

            _setupZoomControls() {
                const zoomInBtn = document.getElementById('pdf-zoom-in');
                const zoomOutBtn = document.getElementById('pdf-zoom-out');
                if (zoomInBtn) zoomInBtn.addEventListener('click', () => this.zoomIn());
                if (zoomOutBtn) zoomOutBtn.addEventListener('click', () => this.zoomOut());
            }

            renderPage(page_number) {
                this.pageRendering = true;
                return this.pdf.getPage(page_number).then((page) => {
                    const scale = this.getScaleToFit(page) * this.pdf_zoom;
                    const outputScale = window.devicePixelRatio || 1;
                    const viewport = page.getViewport({ scale });

                    this.canvas.width = viewport.width * outputScale;
                    this.canvas.height = viewport.height * outputScale;
                    this.canvas.style.width = `${viewport.width}px`;
                    this.canvas.style.height = `${viewport.height}px`;

                    const renderContext = {
                        canvasContext: this.canvas_context,
                        viewport: viewport,
                        transform: outputScale !== 1 ? [outputScale, 0, 0, outputScale, 0, 0] : null,
                    };

                    document.body.classList.add('pdf-loading');
                    return page.render(renderContext).promise.then(() => {
                        document.body.classList.remove('pdf-loading');
                        this.pageRendering = false;
                        if (this.pageNumPending !== null) {
                            this.renderPage(this.pageNumPending);
                            this.pageNumPending = null;
                        }
                        this.pdf_page_current = page_number;
                        return page_number;
                    });
                });
            }
        }

        window.PDFSlidesViewer = ExtendedViewer;
    }
});
