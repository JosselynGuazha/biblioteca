# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Libro_CD(models.Model):
    _name = 'biblioteca.libro_cd'
    _description = 'Libro CDs'

    nro_discos = fields.Integer('Nro. de Disco que contiene el Libro')

    informacion_ids = fields.One2many('biblioteca.informacion', 'libroCd_id', string=" Información del Libro CDs")
    publicacion_id = fields.Many2one('biblioteca.libro_cd', 'Publicacion')

