import publicWidget from 'web.public.widget';

publicWidget.registry.websiteSlidesList = publicWidget.Widget.extend({
    selector: '.o_wslides_js_slides_list',
    events: {},

    start: function () {
        this._updateHref();
        return this._super.apply(this, arguments);
    },

    _updateHref: function () {
        this.$(".o_wslides_js_slides_list_slide_link").each(function () {
            let href = $(this).attr('href');
            let operator = href.indexOf('?') !== -1 ? '&' : '?';

            // Opción A: quitar fullscreen
            href = href.replace(/fullscreen=1/, 'fullscreen=0');

            // Opción B: simplemente NO añadir fullscreen
            $(this).attr('href', href);  // esto no añade nada

        });
    },
});
