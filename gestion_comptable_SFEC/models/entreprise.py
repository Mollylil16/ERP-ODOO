from odoo import models, fields

class Entreprise(models.Model):
    _name = 'custom_accounting.entreprise'
    _description = "Entreprise des clients"

    name = fields.Char(string="Nom de l'entreprise", required=True)
    adresse = fields.Char(string="Adresse")
    contact = fields.Char(string="Téléphone")
    email = fields.Char(string="Email")
    clients_ids = fields.One2many('custom_accounting.client', 'entreprise_id', string="Clients associés")
