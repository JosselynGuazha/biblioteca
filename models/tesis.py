# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tesis(models.Model):
    _name = 'biblioteca.tesis'
    _description = 'Tesis'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = '[ Director: ' + record.director + ']'
            result.append((record.id, name))
        return result

    director = fields.Char('Nombre del Director')

    publicacion_id = fields.Many2one('biblioteca.publicacion', 'Publicacion')
