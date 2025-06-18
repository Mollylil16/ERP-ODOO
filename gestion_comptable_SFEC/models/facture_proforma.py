from odoo import models, fields, api

class FactureProforma(models.Model):
    _name = 'custom_accounting.facture_proforma'
    _description = "Facture Proforma"

    client_id = fields.Many2one('custom_accounting.client', string="Client", required=True)
    bon_commande_id = fields.Many2one('custom_accounting.bon_commande_client', string="Bon de commande lié")
    date_proforma = fields.Date(string="Date de la facture proforma", default=fields.Date.context_today)
    montant_total = fields.Float(string="Montant total", required=True)
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('envoyee', 'Envoyée'),
        ('acceptee', 'Acceptée'),
    ], string="État", default='brouillon')
    commentaire = fields.Text(string="Commentaire")

    @api.model
    def create(self, vals):
        # Générer un numéro unique pour chaque proforma
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].next_by_code('custom_accounting.facture_proforma')
        return super().create(vals)

    name = fields.Char(string="Référence", required=True, copy=False, readonly=True, default='Nouveau')
