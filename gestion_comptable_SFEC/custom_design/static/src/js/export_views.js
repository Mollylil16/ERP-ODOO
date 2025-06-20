odoo.define('custom_design.ExportViews', function (require) {
    "use strict";

    var core = require('web.core');
    var _t = core._t;
    var ActionManager = require('web.ActionManager');

    var ExportViews = {
        init: function () {
            this._setupExportButtons();
        },

        _setupExportButtons: function () {
            ActionManager.include({
                _exportData: function (params) {
                    var self = this;
                    return this._rpc({
                        route: '/web/export/xlsx',
                        params: params,
                    }).then(function (content) {
                        var blob = new Blob([content], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                        var url = window.URL.createObjectURL(blob);
                        var a = document.createElement('a');
                        a.href = url;
                        a.download = params.filename || 'export.xlsx';
                        a.click();
                        window.URL.revokeObjectURL(url);
                    });
                },

                _renderExportButton: function (view, options) {
                    var $button = $('<button>', {
                        class: 'btn btn-primary o_custom_export_button',
                        text: _t('Export'),
                        click: function () {
                            self._exportData({
                                model: view.model,
                                fields: view.fields,
                                domain: view.domain,
                                context: view.context,
                                filename: view.model + '.xlsx',
                            });
                        }
                    });
                    return $button;
                },
            });
        },

        // Export Bon de Commande
        exportPurchaseOrder() {
            return {
                content: [
                    ['Réf', 'Fournisseur', 'Date', 'Total HT'],
                    ...this._getOrderLines()
                ],
                styles: {
                    header: {fill: {patternType: 'solid', fgColor: {rgb: 'FFCC00'}}}
                }
            }
        },

        // Export Suivi Bancaire
        exportBankTracking() {
            return {
                content: [
                    ['Date', 'Libellé', 'Débit', 'Crédit', 'Solde'],
                    ...this._getBankMovements()
                ],
                formats: ['dd/mm/yyyy', '@', '#,##0.00', '#,##0.00', '#,##0.00']
            }
        },

        // Export Recaps
        exportSalesSummary() {
            return {
                content: {
                    achats: this._getPurchaseData(),
                    ventes: this._getSalesData()
                },
                sheets: ['Récap Achats', 'Récap Ventes']
            }
        },

        // Export Clients
        exportClients() {
            return {
                content: [
                    ['Nom', 'LCC', 'Entreprise mère', 'Contact', 'Email'],
                    ...this._getClients().map(c => [c.name, c.lcc_number, c.parent_id?.name, c.phone, c.email])
                ],
                formats: ['@', '@', '@', '@', '@']
            }
        }
    };

    $(document).ready(function () {
        ExportViews.init();
    });

    return ExportViews;
});
