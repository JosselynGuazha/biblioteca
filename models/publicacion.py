# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Publicacion(models.Model):
    _name = 'biblioteca.publicacion'
    _description = 'Publicación'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = record.titulo + " de " + record.autor_ids[0].nombres + " " + record.autor_ids[0].apellidos
            result.append((record.id, name))
        return result

    @api.one
    def _compute_is_bibliotecario(self):
        self.is_bibliotecario = self.env['res.users'].has_group('biblioteca.group_biblioteca_bibliotecario')
    @api.one
    def _compute_is_administrador(self):
        self.is_administrador = self.env['res.users'].has_group('biblioteca.group_biblioteca_manager')

    is_bibliotecario = fields.Boolean(
        string='Es bibliotecario',
        compute="_compute_is_bibliotecario",
        default=True
    )

    is_administrador = fields.Boolean(
        string='Es adminitrador',
        compute="_compute_is_administrador",
        default=True
    )

    imagen = fields.Binary()
    fecha_ingreso = fields.Date('Fecha de Ingreso', default=fields.Date.context_today, readonly=True)
    referencia = fields.Char('Referencia')
    titulo = fields.Char('Título')
    nro_paginas = fields.Integer('Número de páginas')
    fecha_publicacion = fields.Date('Fecha de Publicación')
    campo = fields.Char('Campo')
    tipo_publicacion = fields.Selection([('libro', 'Libro'), ('periodico', 'Periódico'), ('revista', 'Revista'), ('tesis', 'Tesis'),('libro_cd', 'Libro CD')],
    string='Seleccione el tipo de publicación', required=True, track_visibility='onchange')
    estado = fields.Char('Estado', readonly=True, default='disponible')


    libro_id = fields.Many2one('biblioteca.libro', 'Ingrese información adicional para el libro')
    tesis_id = fields.Many2one('biblioteca.tesis', 'Ingrese información adicional para la tesis')
    periodico_id = fields.Many2one('biblioteca.periodico', 'Ingrese información adicional para el periódico')
    revista_id = fields.Many2one('biblioteca.revista', 'Ingrese información adicional para la revista')
    libro_cd_id = fields.Many2one('biblioteca.libro_cd', 'Ingrese información adicional para el CD-Libro')
    autor_ids = fields.One2many('biblioteca.autor', 'publicacion_id', string=" Información del Autor")





    #tesis_ids = fields.One2many('biblioteca.tesis', 'publicacion_id', string=" Información del tesis")
    #libro_ids = fields.One2many('biblioteca.libro', 'publicacion_id', string=" Información del Libro")
    #periodico_ids = fields.One2many('biblioteca.periodico', 'publicacion_id', string=" Información del Periodico")
    #revista_ids = fields.One2many('biblioteca.revista', 'publicacion_id', string=" Información de la Revista")
    #libro_cd_ids = fields.One2many('biblioteca.libro_cd', 'publicacion_id', string=" Información del Libro CDs")
