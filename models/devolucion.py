# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Devolucion(models.Model):
    _name = 'biblioteca.devolucion'
    _description = 'Devolucion'

    fecha_inicio = fields.Date('Fecha Inicio')
    fecha_fin = fields.Date('Fecha Fin')
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], "Estado", readonly=True, default="inactivo")

    multa_ids = fields.One2many('biblioteca.multa', 'devolucion_id', string="Multas")
    servicio_id = fields.Many2one('biblioteca.devolucion', 'Devolucion')
