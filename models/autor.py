# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'Autor'

    nombres = fields.Char('Nombres del Autor')
    apellidos = fields.Char('Apellidos del Autor')

    publicacion_id = fields.Many2one('biblioteca.autor', 'Publicacion')
