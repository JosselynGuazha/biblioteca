# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Informacion(models.Model):
    _name = 'biblioteca.informacion'
    _description = 'Informacion'

    titulo = fields.Char('Título')
    nro_paginas = fields.Integer('Número de páginas')
    fecha_publicacion = fields.Date('Fecha de Publicación')
