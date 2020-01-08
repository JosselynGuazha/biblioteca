# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Periodico(models.Model):
    _name = 'biblioteca.periodico'
    _description = 'Periodico'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = '[ Diario: ' + record.diario + ']'
            result.append((record.id, name))
        return result

    diario = fields.Char('Nombre del Diario')

    publicacion_id = fields.Many2one('biblioteca.periodico', 'Publicacion')
