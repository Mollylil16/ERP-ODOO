from odoo import models, fields, api

class CustomClient(models.Model):
    _name = 'custom.accounting.client'
    _description = 'Client de l’entreprise'

    name = fields.Char(string="Nom complet", required=True)
    lcc_number = fields.Char(string="Numéro LCC")
    phone = fields.Char(string="Téléphone")
    email = fields.Char(string="Email")
    address = fields.Text(string="Adresse")
    company_name = fields.Char(string="Entreprise liée")
    entreprise_id = fields.Many2one('custom_accounting.entreprise', string="Entreprise liée")

    # Statistiques de paiement
    total_paiements = fields.Float(string="Montant total payé", compute="_compute_total_paiements", store=True)
    nombre_paiements = fields.Integer(string="Nombre de paiements", compute="_compute_total_paiements", store=True)

    @api.depends('id')
    def _compute_total_paiements(self):
        for client in self:
            paiements = self.env['custom_accounting.paiement_client'].search([('client_id', '=', client.id)])
            client.total_paiements = sum(p.montant for p in paiements)
            client.nombre_paiements = len(paiements)
