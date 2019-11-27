# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lector(models.Model):
    _name = 'biblioteca.lector'
    _description = 'Lector'

    nombres = fields.Char('Nombres del Lector')
    apellidos = fields.Char('Apellidos del Lector')
    telefono = fields.Char('Numero de Telefono')
    direccion = fields.Char('Direccion')

    #servicio_id = fields.Many2one('biblioteca.lector', 'Lector')
