# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Libro_CD(models.Model):
    _name = 'biblioteca.libro_cd'
    _description = 'Libro CDs'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = '[' + record.nro_discos + ' discos' ']'
            result.append((record.id, name))
        return result

    nro_discos = fields.Integer('Nro. de Disco que contiene el Libro')

    publicacion_id = fields.Many2one('biblioteca.libro_cd', 'Publicacion')
