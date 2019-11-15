# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Servicio(models.Model):
    _name = 'biblioteca.servicio'
    _description = 'Servicio'

    @api.multi
    def name_get(self):
        result=[]
        for record in self:
            name = '['+ record.nombre+']'
            result.append((record.id, name))
        return result

    publicacion_id = fields.Many2one('biblioteca.publicacion', 'Publicacion')
    prestamo_ids = fields.One2many('biblioteca.prestamo', 'servicio_id', string="Prestamo")
    devolucion_ids = fields.One2many('biblioteca.devolucion', 'servicio_id', string="Devolucion")
    lector_ids = fields.One2many('biblioteca.lector', 'servicio_id', string="Lector")
