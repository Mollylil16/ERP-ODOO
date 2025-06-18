from odoo import models, fields

class LigneFactureProforma(models.Model):
    _name = 'custom_accounting.ligne_facture_proforma'
    _description = 'Ligne de facture proforma'

    facture_id = fields.Many2one('custom_accounting.facture_proforma', string="Facture")
    article_id = fields.Many2one('custom_accounting.article', string="Article", required=True)
    quantite = fields.Float(string="Quantité", required=True)
    prix_unitaire = fields.Float(string="Prix unitaire", required=True)
