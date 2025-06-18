from odoo import models, fields

class LigneReceptionFournisseur(models.Model):
    _name = 'custom_accounting.ligne_reception_fournisseur'
    _description = "Ligne de réception fournisseur"

    reception_id = fields.Many2one('custom_accounting.reception_fournisseur', string="Réception", ondelete='cascade')
    article_id = fields.Many2one('custom_accounting.article', string="Article", required=True)
    quantite_recue = fields.Float(string="Quantité reçue", required=True)
