# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Multa(models.Model):
    _name = 'biblioteca.multa'
    _description = 'Multa'

    total_dias = fields.Integer('Fecha Inicio ')
    valor = fields.Float('Valor a Pagar de la Multa', (3, 2))