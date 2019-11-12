# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Informacion(models.Model):
    _name = 'biblioteca.informacion'
    _description = 'Informacion'


    referencia = fields.Char('Referencia')
    titulo = fields.Char('Título')
    nro_paginas = fields.Integer('Número de páginas')
    fecha_publicacion = fields.Date('Fecha de Publicación')
    campo = fields.Char('Campo')

    libro_id = fields.Many2one('biblioteca.libro', 'Libro')
    libroCd_id = fields.Many2one('biblioteca.libro_cd', 'Libro CDs')
    tesis_id = fields.Many2one('biblioteca.tesis', 'Tesis')
    periodico_id = fields.Many2one('biblioteca.periodico', 'Periodico')
    revista_id = fields.Many2one('biblioteca.revista', 'Revista')
