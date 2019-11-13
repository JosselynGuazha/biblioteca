# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Revista(models.Model):
    _name = 'biblioteca.revista'
    _description = 'Revista'

    editorial = fields.Char('Editorial')


    publicacion_id = fields.Many2one('biblioteca.revista', 'Publicacion')

