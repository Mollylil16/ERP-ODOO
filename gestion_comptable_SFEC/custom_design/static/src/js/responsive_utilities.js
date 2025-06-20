odoo.define('custom_design.ResponsiveUtilities', function (require) {
    "use strict";

    const core = require('web.core');
    const _t = core._t;
    const Widget = require('web.Widget');

    class ResponsiveUtilities extends Widget {
        static template = 'ResponsiveUtilities';

        constructor(parent) {
            super(parent);
            this._setupResponsiveTables();
            this._setupResponsiveForms();
        }

        _setupResponsiveTables() {
            this.$('.o_list_view table').addClass('o_custom_responsive_table');
        }

        _setupResponsiveForms() {
            this.$('.o_form_view').addClass('o_custom_responsive_form');
        }

        async willStart() {
            await super.willStart();
            this.$el.addClass('o_custom_responsive_container');
        }

        async start() {
            await super.start();
            this._setupResponsiveTables();
            this._setupResponsiveForms();
        }

        async destroy() {
            await super.destroy();
            this.$('.o_list_view table').removeClass('o_custom_responsive_table');
            this.$('.o_form_view').removeClass('o_custom_responsive_form');
        }
    }

    core.action_registry.add('responsive_utilities', ResponsiveUtilities);
    return ResponsiveUtilities;
});
