# -*- coding: utf-8 -*-
{
    'name': 'Gestion Comptable SFEC',
    'version': '1.0.0',
    'category': 'Accounting',
    'summary': "Automatisation complète des processus comptables pour l'entreprise",
    'description': """
Module Odoo personnalisé pour gérer :
- les interactions client-entreprise (bon de commande, facture proforma, facture finale),
- les achats auprès des fournisseurs (demande, bon de commande, facture),
- la gestion de stock (entrée/sortie),
- le volet financier (paiements par caisse, banque, crédit),
- la traçabilité des clients et entreprises partenaires.
""",
    'author': 'SFEC',
    'website': 'https://SFEC.com',
    'support': 'support@sfec.com',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': [
        'sale',
        'purchase',
        'stock',
        'account',
        'contacts',
        'mail',
        'base_automation',
        'report_xlsx',
        'web_tour',
        'web_responsive',
        'web_widget_colorpicker',
        'base_import',
        'web_export_view'
    ],
    'assets': {
        'web.assets_backend': [
            'gestion_comptable_sfec/static/src/css/neumorphic.css',
            'gestion_comptable_sfec/static/src/css/form_styles.css',
            'gestion_comptable_sfec/static/src/css/drag_drop.css',
            'gestion_comptable_sfec/static/src/css/custom_tags.css',
            'gestion_comptable_sfec/static/src/js/neumorphic.js',
            'gestion_comptable_sfec/static/src/js/form_interactions.js',
            'gestion_comptable_sfec/static/src/js/drag_drop_widget.js',
            'gestion_comptable_sfec/static/src/js/advanced_filters.js',
            'gestion_comptable_sfec/static/src/js/custom_tags_widget.js'
        ],
        'web.assets_qweb': [
            'gestion_comptable_sfec/static/src/xml/drag_drop_template.xml',
            'gestion_comptable_sfec/static/src/xml/custom_tags_template.xml'
        ]
    },
    'data': [
        # Sécurité
        'security/ir.model.access.csv',
        'security/groups.xml',

        # Partenariats exclusifs
        'views/partenariat_exclusif_view.xml',
        'data/partenariat_exclusif_data.xml',

        # Workflows et États
        'data/workflow_data.xml',
        'data/states_data.xml',

        # Templates d'emails
        'data/mail_template_data.xml',

        # Séquences
        'data/sequence_data.xml',
        'data/sequence.xml',

        # Tableau de bord
        'views/dashboard_view.xml',

        # Rapports de Trésorerie
        'report/tresorerie_report.xml',
        'report/templates/tresorerie_report_template.xml',

        # Optimisations
        'data/indexes.xml',
        'data/constraints.xml',
        'data/sql_queries.xml',
        'data/cleanup_scripts.xml',
        'data/optimization_scripts.xml',

        # Spécificités SFEC
        'data/sfec_specifics.xml',

        # Tests
        'tests/test_models.py',
        'tests/test_workflows.py',

        # Déploiement
        'data/deployment_procedures.xml',
        'data/deployment_guide.md',

        # Sauvegarde
        'models/backup.py',

        # Vues CLIENTS - ENTREPRISES
        'views/client_views.xml',
        'views/entreprise_view.xml',
        'views/bon_commande_client_view.xml',
        'views/ligne_commande_client_view.xml',
        'views/facture_proforma_view.xml',
        'views/ligne_facture_proforma_view.xml',
        'views/accuse_reception_view.xml',
        'views/facture_finale_view.xml',
        'views/paiement_client_view.xml',

        # Vues FOURNISSEURS
        'views/fournisseur_view.xml',
        'views/bon_commande_fournisseur_view.xml',
        'views/facture_fournisseur_view.xml',
        'views/paiement_fournisseur_view.xml',
        'views/ligne_livraison_article_fournisseur_view.xml',

        # Vues STOCK
        'views/article_view.xml',
        'views/stock_mouvement_view.xml',

        # Import/Export
        'views/drag_drop_view.xml',
        'data/import_data.xml',

        # Rapports
        'views/report_views.xml',
        'report/report_templates.xml',
        'report/report_actions.xml',
        'report/facture_finale_report.xml',
        'report/facture_finale_report_template.xml',
        'report/paiement_client_report.xml',
        'report/paiement_client_report_template.xml',

        # Statistiques
        'views/statistique_paiement_view.xml',

        # Menus
        'views/menu.xml'
    ],
    'demo': [
        'data/demo.xml'
    ],
    'test': [
        'tests/test_partenariat.py'
    ],
    'images': [
        'static/description/icon.png'
    ],
    'post_init_hook': 'init_import_data'
}
