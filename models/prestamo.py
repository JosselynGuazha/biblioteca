# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Prestamo'

    fecha_inicio = fields.Date('Fecha Inicio ')
    fecha_fin = fields.Date('Fecha Fin')

    servicio_id = fields.Many2one('biblioteca.prestamo', 'Prestamo')
