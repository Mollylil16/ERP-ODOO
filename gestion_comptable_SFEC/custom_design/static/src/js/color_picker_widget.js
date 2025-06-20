odoo.define('custom_design.ColorPickerWidget', function (require) {
    "use strict";

    const AbstractField = require('web.AbstractField');
    const fieldRegistry = require('web.field_registry');
    const core = require('web.core');
    const _t = core._t;

    class ColorPickerWidget extends AbstractField {
        constructor() {
            super(...arguments);
            this.template = 'ColorPickerWidget';
        }

        static template = 'ColorPickerWidget';

        setup() {
            super.setup();
            this.events = {
                ...AbstractField.prototype.events,
                'change input': this._onColorChange,
            };
        }

        async _render() {
            await super._render();
            if (this.value) {
                this.el.querySelector('input[type="color"]').value = this.value;
            }
        }

        _onColorChange(ev) {
            const color = ev.currentTarget.value;
            this._setValue(color);
        }
    }

    fieldRegistry.add('color_picker', ColorPickerWidget);
    return ColorPickerWidget;
});
