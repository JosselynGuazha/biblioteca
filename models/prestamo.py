# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Prestamo'

    fecha_inicio = fields.Date('Fecha Inicio', default=fields.Date.context_today, readonly=True)
    fecha_fin = fields.Date('Fecha Fin')
    estado = fields.Selection([('solicitado', 'Solicitado'),
                              ('prestado', 'Prestado'),
                              ('devuelto', 'Devuelto')],
                              string='Estado', required=True, default="solicitado",
                              track_visibility='onchange')
    #estado solicitado, prestado devuelto
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Solicitante',
        default=lambda self: self.env.user.id,
        readonly=True
    )

    publicacion_id = fields.Many2one('biblioteca.publicacion', 'Seleccione la publicacion')
