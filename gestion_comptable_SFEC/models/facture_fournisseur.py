from odoo import models, fields
from datetime import date

class FactureFournisseur(models.Model):
    _name = 'custom_accounting.facture_fournisseur'
    _description = "Facture Fournisseur"

    fournisseur_id = fields.Many2one('custom_accounting.fournisseur', string="Fournisseur", required=True)
    date_facture = fields.Date(string="Date de la facture", default=date.today)
    montant_total = fields.Float(string="Montant total", compute="_compute_total", store=True)
    ligne_facture_ids = fields.One2many('custom_accounting.ligne_facture_fournisseur', 'facture_id', string="Lignes de facture")
    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('payee', 'Payée'),
    ], string="Statut", default='brouillon')

    @fields.depends('ligne_facture_ids.montant_total')
    def _compute_total(self):
        for rec in self:
            rec.montant_total = sum(line.montant_total for line in rec.ligne_facture_ids)
