# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tesis(models.Model):
    _name = 'biblioteca.tesis'
    _description = 'Tesis'

    director = fields.Char('Nombre del Director')
    area = fields.Char('Area perteneciente de la Tesis')
