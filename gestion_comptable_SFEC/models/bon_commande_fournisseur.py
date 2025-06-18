from odoo import models, fields, api
from datetime import date

class BonCommandeFournisseur(models.Model):
    _name = 'custom_accounting.bon_commande_fournisseur'
    _description = "Bon de commande fournisseur"
    _order = "date_commande desc"

    fournisseur_id = fields.Many2one('custom_accounting.fournisseur', string="Fournisseur", required=True)
    date_commande = fields.Date(string="Date de commande", default=date.today)
    reference = fields.Char(string="Référence commande", required=True)
    ligne_commande_ids = fields.One2many('custom_accounting.ligne_commande_fournisseur', 'bon_commande_id', string="Lignes de commande")
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('confirme', 'Confirmé'),
        ('recu', 'Réceptionné')
    ], default='brouillon', string="État")
