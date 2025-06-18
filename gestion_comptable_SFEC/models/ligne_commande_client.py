from odoo import models, fields

class LigneCommandeClient(models.Model):
    _name = 'custom_accounting.ligne_commande_client'
    _description = 'Ligne de commande client'

    commande_id = fields.Many2one('custom_accounting.bon_commande_client', string="Bon de commande")
    article_id = fields.Many2one('custom_accounting.article', string="Article", required=True)
    quantite = fields.Float(string="Quantité", required=True)
    prix_unitaire = fields.Float(string="Prix unitaire", required=True)
