from odoo import models, fields, api

class LigneCommandeFournisseur(models.Model):
    _name = 'custom_accounting.ligne_commande_fournisseur'
    _description = "Ligne de commande fournisseur"

    bon_commande_id = fields.Many2one('custom_accounting.bon_commande_fournisseur', string="Bon de commande", ondelete='cascade')
    article_id = fields.Many2one('custom_accounting.article', string="Article", required=True)
    quantite = fields.Float(string="Quantité", required=True)
    prix_unitaire = fields.Float(string="Prix unitaire", required=True)
    total = fields.Float(string="Total", compute="_compute_total", store=True)

    @api.depends('quantite', 'prix_unitaire')
    def _compute_total(self):
        for ligne in self:
            ligne.total = ligne.quantite * ligne.prix_unitaire
