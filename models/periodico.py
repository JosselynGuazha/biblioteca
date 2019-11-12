# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Periodico(models.Model):
    _name = 'biblioteca.periodico'
    _description = 'Periodico'

    diario = fields.Char('Nombre del Diario')

    informacion_ids = fields.One2many('biblioteca.informacion', 'periodico_id', string=" Información del Periodico")

    publicacion_id = fields.Many2one('biblioteca.periodico', 'Publicacion')
