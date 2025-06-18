# Gestion Comptable SFEC

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/SFEC/gestion_comptable_sfec/actions)
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/SFEC/gestion_comptable_sfec/actions)

## Description

Le module Gestion Comptable SFEC est une solution complète pour la gestion comptable d'entreprise, spécialement conçue pour gérer les flux financiers, les commandes, et les relations avec les fournisseurs. Ce module inclut des fonctionnalités avancées pour les partenariats exclusifs avec SPIRAX SARCO et APPROTECH.

## Fonctionnalités Principales

### 1. Gestion des Flux Commerciaux
- **Client-Entreprise**
  - Gestion des bons de commande
  - Factures proforma
  - Accusés de réception
  - Factures finales
  - Paiements clients

- **Entreprise-Fournisseurs**
  - Demandes d'achat
  - Factures fournisseurs
  - Commandes fournisseurs
  - Paiements fournisseurs
  - Suivi des livraisons

### 2. Gestion des Partenariats Exclusifs
- Gestion des partenariats avec SPIRAX SARCO et APPROTECH
- Validation automatique des commandes
- Suivi des performances
- Statistiques détaillées

### 3. Tableau de Bord
- Indicateurs de performance clés
- Graphiques d'évolution
- Alertes en temps réel
- Statistiques des stocks
- Suivi des paiements

### 4. Gestion des Stocks
- Entrées et sorties de stock
- Alertes stock bas
- Suivi des mouvements
- Réapprovisionnement automatique

### 5. Interface Utilisateur
- Design néomorphique moderne
- Animations fluides
- Interface responsive
- Validation en temps réel
- Messages de statut clairs

## Installation

1. Assurez-vous d'avoir les dépendances nécessaires installées :
   ```bash
   pip install odoo
   ```

2. Ajoutez le module à votre liste de modules Odoo :
   ```bash
   addons_path=/path/to/your/addons,/path/to/gestion_comptable_sfec
   ```

3. Mettez à jour la liste des modules :
   ```bash
   python -m odoo -c /path/to/odoo.conf -u all
   ```

4. Installez le module via l'interface web d'Odoo :
   - Allez dans le menu "Apps"
   - Recherchez "Gestion Comptable SFEC"
   - Cliquez sur "Installer"

## Configuration

1. Configuration des Partenariats Exclusifs :
   - Allez dans "Gestion Comptable > Partenariats Exclusifs"
   - Configurez les partenariats avec SPIRAX SARCO et APPROTECH
   - Définissez les conditions particulières

2. Configuration des Alertes :
   - Allez dans "Gestion Comptable > Configuration > Alertes"
   - Configurez les seuils de stock
   - Définissez les relances automatiques

## Dépendances

- Odoo >= 16.0
- Python >= 3.8
- PostgreSQL >= 13
- Les modules Odoo suivants :
  - sale
  - purchase
  - stock
  - account
  - contacts
  - mail
  - base_automation
  - report_xlsx
  - web_tour
  - web_responsive
  - web_widget_colorpicker
  - web_widget_one2many_tags

## Support

Pour obtenir du support ou signaler des bugs :

- Email : support@sfec.com
- Site web : https://sfec.com
- GitHub : https://github.com/SFEC/gestion_comptable_sfec/issues

## Contributing

1. Fork le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/amazing-feature`)
3. Commit vos changements (`git commit -m 'Add some amazing feature'`)
4. Push vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrez une Pull Request

## Licence

Ce module est sous licence LGPL-3. Consultez le fichier LICENSE pour plus de détails.

## Version

1.0.0 - Version initiale complète avec toutes les fonctionnalités principales
