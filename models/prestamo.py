# -*- coding: utf-8 -*-
import pdb
from odoo import models, fields, api


class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Prestamo'

    #def _obtener_usuario(self):
    #    self.valor = self.env.context.get('uid')

    """ @api.model
    def prestamo_libro(self):
        #pdb.set_trace()
        lista = self.env['biblioteca.publicacion']
        lista2 = self.env['biblioteca.prestamo']
        lista3 = []

        for prestamo in lista2:
            for publicacion in lista:
                if publicacion.id != prestamo.publicacion_id:
                    lista3.append(publicacion.id)
        return lista3 """
        #return publicacion_id = lista3


    @api.multi
    def name_get(self):
        result = []
        #pdb.set_trace()
        for record in self:
            name = record.publicacion_id.titulo + " prestado a " + record.user_id.name
            result.append((record.id, name))
        return result

    fecha_inicio = fields.Date('Fecha Inicio', default=fields.Date.context_today, readonly=True)
    fecha_fin = fields.Date('Fecha Fin')
    estado = fields.Selection([('solicitado', 'Solicitado'),
                              ('prestado', 'Prestado'),
                              ('disponible', 'Disponible')],
                              string='Estado', required=True, default="disponible",
                              track_visibility='onchange')
    #estado solicitado, prestado devuelto
    #valor = fields.Char(compute='_obtener_usuario')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Solicitante',
        default=lambda self: self.env.user.id
    )
    publicacion_id = fields.Many2one('biblioteca.publicacion', 'Seleccione la publicacion')

    @api.multi
    def set_to_solicitado(self):
        #pdb.set_trace()
        '''Method to change state to draft'''
        self.write({'estado': 'solicitado'})
        self.publicacion_id.write({'estado': 'solicitado'})

    @api.multi
    def set_to_prestado(self):
        '''Method to change state to draft'''
        self.write({'estado': 'prestado'})
        self.publicacion_id.write({'estado': 'prestado'})


    @api.multi
    def set_to_disponible(self):
        '''Method to change state to draft'''
        self.write({'estado': 'disponible'})
        self.publicacion_id.write({'estado': 'disponible'})
