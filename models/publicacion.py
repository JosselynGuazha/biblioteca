# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Publicacion(models.Model):
    _name = 'biblioteca.publicacion'
    _description = 'Publicación'

    fecha_ingreso = fields.Date('Fecha de Ingreso')
    referencia = fields.Char('Referencia')
    titulo = fields.Char('Título')
    nro_paginas = fields.Integer('Número de páginas')
    fecha_publicacion = fields.Date('Fecha de Publicación')
    campo = fields.Char('Campo')

    tesis_ids = fields.One2many('biblioteca.tesis', 'publicacion_id', string=" Información del tesis")
    libro_ids = fields.One2many('biblioteca.libro', 'publicacion_id', string=" Información del Libro")
    periodico_ids = fields.One2many('biblioteca.periodico', 'publicacion_id', string=" Información del Periodico")
    revista_ids = fields.One2many('biblioteca.revista', 'publicacion_id', string=" Información de la Revista")
    libro_cd_ids = fields.One2many('biblioteca.libro_cd', 'publicacion_id', string=" Información del Libro CDs")
    autor_ids = fields.One2many('biblioteca.autor', 'publicacion_id', string=" Información del Autor")

    servicio_id = fields.Many2one('biblioteca.publicacion', 'Servicio')
