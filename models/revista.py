# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Revista(models.Model):
    _name = 'biblioteca.revista'
    _description = 'Revista'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = '[ Editorial: ' + record.editorial +  ']'
            result.append((record.id, name))
        return result

    editorial = fields.Char('Editorial')

    publicacion_id = fields.Many2one('biblioteca.revista', 'Publicacion')
