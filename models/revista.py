# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Revista(models.Model):
    _name = 'biblioteca.revista'
    _description = 'Revista'

    editorial = fields.Char('Editorial')


    informacion_ids = fields.One2many('biblioteca.informacion', 'revista_id', string=" información del Libro")
    publicacion_id = fields.Many2one('biblioteca.revista', 'Publicacion')

