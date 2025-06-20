odoo.define('custom_design.ColorPicker', function (require) {
    "use strict";

    const { Component } = owl;
    const { useRef } = owl.hooks;

    class ColorPicker extends Component {
        setup() {
            this.inputRef = useRef("color-input");
            this.state = { color: this.props.value || '#FFFFFF' };
        }

        _onColorChange(ev) {
            this.state.color = ev.target.value;
            this.trigger('color-changed', this.state.color);
        }
    }

    ColorPicker.template = 'custom_design.ColorPicker';
    ColorPicker.props = { value: { type: String, optional: true } };

    return ColorPicker;
});
