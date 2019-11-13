# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tesis(models.Model):
    _name = 'biblioteca.tesis'
    _description = 'Tesis'

    director = fields.Char('Nombre del Director')

    publicacion_id = fields.Many2one('biblioteca.publicacion', 'Publicacion')

