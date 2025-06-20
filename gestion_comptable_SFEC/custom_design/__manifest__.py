{
    'name': 'Custom Design',
    'version': '17.0.1.0.0',
    'category': 'Theme/Tools',
    'summary': 'Fonctionnalités de design personnalisées pour Odoo',
    'description': """
        Module de design personnalisé pour Odoo 17 :
        - Sélecteur de couleur personnalisé
        - Widgets de tags interactifs
        - Outils de design responsif
        - Fonctionnalités de filtrage avancé
    """,
    'author': 'SFEC',
    'depends': [
        'web',
        'web_tour',
        'web_responsive',
    ],
    'data': [
        'views/custom_design_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_design/static/src/css/custom_design.css',
            'custom_design/static/src/js/color_picker_widget.js',
            'custom_design/static/src/js/custom_tags_widget.js',
            'custom_design/static/src/js/responsive_utilities.js',
            'web.assets_backend',
        ],
        'web.assets_qweb': [
            'custom_design/static/src/xml/color_picker_template.xml',
            'custom_design/static/src/xml/custom_tags_template.xml',
            'web.assets_qweb',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init',
    'pre_init_hook': 'pre_init',
    'uninstall_hook': 'uninstall',
    'assets_debug': {
        'web.assets_backend': [
            'custom_design/static/src/scss/custom_design.scss',
        ],
    },
}
