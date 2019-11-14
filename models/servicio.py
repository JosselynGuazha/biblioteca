# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Servicio(models.Model):
    _name = 'biblioteca.servicio'
    _description = 'Servicio'


    publicacion_ids = fields.One2many('biblioteca.publicacion', 'servicio_id', string="Seleccionar Publicacion")
    prestamo_ids = fields.One2many('biblioteca.prestamo', 'servicio_id', string="Prestamo")
    devolucion_ids = fields.One2many('biblioteca.devolucion', 'servicio_id', string="Devolucion")
    lector_ids = fields.One2many('biblioteca.lector', 'servicio_id', string="Lector")
