# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Periodico(models.Model):
    _name = 'biblioteca.periodico'
    _description = 'Periodico'

    diario = fields.Char('Nombre del Diario')


    publicacion_id = fields.Many2one('biblioteca.periodico', 'Publicacion')
