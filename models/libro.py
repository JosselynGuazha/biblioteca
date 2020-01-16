# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = 'Editorial: ' + record.editorial + ', Imprenta: ' + record.imprenta
            result.append((record.id, name))
        return result

    editorial = fields.Char('Editorial')
    imprenta = fields.Char('Imprenta')


    #publicacion_id = fields.Many2one('biblioteca.libro', 'Publicacion')
