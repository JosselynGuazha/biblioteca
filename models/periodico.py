# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Periodico(models.Model):
    _name = 'biblioteca.periodico'
    _description = 'Periodico'

    diario = fields.Char('Nombre del Diario')
