# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    editorial = fields.Char('Editorial')
    genero = fields.Char('Género')

    informacion_ids = fields.One2many('biblioteca.informacion', 'libro_id', string=" información del Libro")
