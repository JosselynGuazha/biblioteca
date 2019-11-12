# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tesis(models.Model):
    _name = 'biblioteca.tesis'
    _description = 'Tesis'

    director = fields.Char('Nombre del Director')

    informacion_ids = fields.One2many('biblioteca.informacion', 'tesis_id', string=" Información de la Tesis")

    publicacion_id = fields.Many2one('biblioteca.publicacion', 'Publicacion')

