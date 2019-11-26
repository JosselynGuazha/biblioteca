# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sancion(models.Model):
    _name = 'biblioteca.sancion'
    _description = 'Sancion'

    fecha_sancion = fields.Date('Fecha')
    observacion = fields.Text('Observación')

    prestamo_id = fields.Many2one('biblioteca.prestamo', 'Prestamo')
