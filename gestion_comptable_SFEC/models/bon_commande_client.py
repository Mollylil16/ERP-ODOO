from odoo import models, fields, api

class BonCommandeClient(models.Model):
    _name = 'custom_accounting.bon_commande_client'
    _description = "Bon de commande client"

    client_id = fields.Many2one('custom_accounting.client', string="Client", required=True)
    date_commande = fields.Date(string="Date de commande", default=fields.Date.context_today)
    reference = fields.Char(string="Référence", required=True)
    article_ids = fields.Many2many('custom_accounting.article', string="Articles commandés")
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('envoye', 'Envoyé'),
        ('valide', 'Validé')
    ], string="État", default='brouillon')
    notes = fields.Text(string="Notes")

    @api.model
    def create(self, vals):
        if not vals.get('reference'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('custom_accounting.bon_commande_client')
        return super().create(vals)
