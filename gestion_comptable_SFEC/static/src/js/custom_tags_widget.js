odoo.define('gestion_comptable_sfec.custom_tags_widget', function (require) {
    "use strict";

    const AbstractField = require('web.AbstractField');
    const fieldRegistry = require('web.field_registry');

    const CustomTagsWidget = AbstractField.extend({
        template: 'CustomTagsWidget',
        
        init() {
            this._super(...arguments);
            this.tags = [];
        },
        
        willStart() {
            return this._super(...arguments).then(() => {
                if (this.value) {
                    this.tags = this.value.split(',').map(tag => tag.trim());
                }
            });
        },
        
        _render() {
            this.$el.empty();
            const container = $('<div class="o_custom_tags_container"/>');
            
            // Render existing tags
            this.tags.forEach(tag => {
                const tagElement = $(`
                    <span class="o_custom_tag">
                        ${tag}
                        <button type="button" class="o_remove_tag">×</button>
                    </span>
                `);
                tagElement.find('.o_remove_tag').click(() => this._removeTag(tag));
                container.append(tagElement);
            });
            
            // Add input for new tags
            const input = $('<input type="text" class="o_new_tag" placeholder="Ajouter un tag..."/>');
            input.keydown((e) => {
                if (e.key === 'Enter' || e.key === ',') {
                    this._addTag(input.val());
                    input.val('');
                }
            });
            container.append(input);
            
            this.$el.append(container);
        },
        
        _addTag(tag) {
            tag = tag.trim();
            if (tag && !this.tags.includes(tag)) {
                this.tags.push(tag);
                this._render();
                this._setValue(this.tags.join(','));
            }
        },
        
        _removeTag(tag) {
            this.tags = this.tags.filter(t => t !== tag);
            this._render();
            this._setValue(this.tags.join(','));
        },
        
        _setValue(value) {
            this._setValue(value);
        }
    });

    fieldRegistry.add('custom_tags', CustomTagsWidget);

    return CustomTagsWidget;
});
