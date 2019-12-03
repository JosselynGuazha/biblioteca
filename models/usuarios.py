# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions
import time
import base64
from datetime import date, datetime
from odoo import models, fields, api, tools, _
from odoo.tools.translate import _
from odoo.modules import get_module_resource
from odoo.exceptions import except_orm
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

try:
    from odoo.tools import image_colorize, image_resize_image_big
except:
    image_colorize = False
    image_resize_image_big = False


class Usuarios(models.Model):
    _name = 'biblioteca.usuarios'
    _description = 'Información de usuarios'
    #_inherit = ['mail.thread']
    # inherit = 'res.users'

    @api.multi
    def name_get(self):
        """metodo para presentar el nombre y el codigo"""
        return [(rec.id, ' ' + rec.usuario_name + ' ' + rec.apellidos) for rec in self]


    @api.depends('fecha_nacimiento')
    def _compute_student_age(self):
        """Metodo para calcular los años del usuarios"""
        current_dt = datetime.today()
        for rec in self:
            if rec.fecha_nacimiento:
                start = datetime.strptime(rec.fecha_nacimiento,
                                          DEFAULT_SERVER_DATE_FORMAT)
                age_calc = ((current_dt - start).days / 365)
                # Age should be greater than 0
                if age_calc > 0.0:
                    rec.anio = age_calc

    @api.constrains('fecha_nacimiento')
    def check_anio(self):
        '''Metodo para verificar que la fecha de nacimiento sea mínimo 5'''
        current_dt = datetime.today()
        if self.fecha_nacimiento:
            start = datetime.strptime(self.fecha_nacimiento, DEFAULT_SERVER_DATE_FORMAT)
            age_calc = ((current_dt - start).days / 365)
            # Check if age less than 5 years
            if age_calc < 5:
                raise ValidationError(_('''La fecha de nacimiento dede estar erronea!'''))

    @api.model
    def create(self, vals):
        """
        Metodo para crear un usuarios cuando se crea el nuevo estudiante
        """
        if vals.get('pid', _('New')) == _('New'):
            vals['pid'] = self.env['ir.sequence'].next_by_code('biblioteca.usuarios') or _('New')
        if vals.get('pid', False):
            vals['login'] = vals['pid']
            vals['password'] = vals['pid']
        else:
            raise except_orm(_('Error!'),_('''PID no valido para guardar el registro.'''))
        if vals.get('cmp_id', False):
            company_vals = {'company_ids': [(4, vals.get('cmp_id'))],
                            'company_id': vals.get('cmp_id')}
            vals.update(company_vals)
        # if vals.get('email'):

        res = super(Usuarios, self).create(vals)
        emp_grp = self.env.ref('base.group_user')


        if res.tipo_usuarios == 'visitante':
            if res.state == 'borrador':
                admission_group = self.env.ref('biblioteca.group_biblioteca_visitantes')
                new_grp_list = [admission_group.id, emp_grp.id]
                res.user_id.write({'groups_id': [(6, 0, new_grp_list)]})
            elif res.state == 'hecho':
                done_student = self.env.ref('biblioteca.group_biblioteca_visitantes')
                group_list = [done_student.id, emp_grp.id]
                res.user_id.write({'groups_id': [(6, 0, group_list)]})
        if res.tipo_usuarios == 'estudiante':
            if res.state == 'borrador':
                admission_group = self.env.ref('biblioteca.group_biblioteca_estudiantes')
                new_grp_list = [admission_group.id, emp_grp.id]
                res.user_id.write({'groups_id': [(6, 0, new_grp_list)]})
            elif res.state == 'hecho':
                done_student = self.env.ref('biblioteca.group_biblioteca_estudiantes')
                group_list = [done_student.id, emp_grp.id]
                res.user_id.write({'groups_id': [(6, 0, group_list)]})
        return res

    user_id = fields.Many2one('res.users', 'User ID', ondelete="cascade", required=True, delegate=True)
    usuario_name = fields.Char(string='Nombres', related='user_id.name' , requird=True)
    usuario_id = fields.Many2one('biblioteca.usuarios', 'Name')
    tipo_usuarios = fields.Selection([('visitante', 'Visitante'), ('estudiante', 'Estudiante')],
                                    string='Seleccione el tipo de usuario', required=True, default='estudiante', track_visibility='onchange')
    apellidos = fields.Char(string='Apellidos')
    pid = fields.Char('Id del usuarios', required=True, default=lambda self: _('New'),
                      help='Numero de Cedula')
    cedula = fields.Char(string='Cedula', size=10, requird=True) #,related='user_id.login'

    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", requird=True)
    email = fields.Char(string='Correo Electronico')
    genero = fields.Selection([('hombre', 'Hombre'), ('mujer', 'Mujer'), ('otro', 'Otro')],
                              string='Genero', required=True, default='hombre', track_visibility='onchange')
    per_country_id = fields.Many2one('res.country', string='Pais de Nacimiento', ondelete='restrict')
    estado_civil = fields.Selection([('soltero', 'Soltero(a)'), ('casado', 'Casado(a)'), ('divorciado', 'Divorciado(a)'), ('union_libre', 'Unión Libre'), ('viudo', 'Viodo(a)')],
                              string='Estado Civil', required=True, default='soltero', track_visibility='onchange')
    imagen = fields.Binary() #para subir la foto
    telefono = fields.Char(string="Telefono Convencional")
    celular = fields.Char(string="Telefono Celular")
    ciudad = fields.Char(string="Ciudad")
    state = fields.Selection([('borrador', 'Borrador'),
                              ('terminado', 'Terminado'),
                              ('cancelar', 'Cancelar')
                              ],
                             'State', readonly=True, default="borrador")
    # probando estas características
    direccion_domicilio = fields.Char(string="Direccion Domiciliaria")
    anio = fields.Integer(compute='_compute_student_age', string='Años')

    _sql_constraints = [
        ('cedula', 'unique(cedula)', "Existe otro usuario con el mismo numero de cedula"),
    ]


    #def _create_expedientea(self):
    #    inv_obj = self.env['evaluacion.expedientea']
    #    self.ensure_one()
    #    expediente = inv_obj.create({
    #        'usuario_id': self.usuario_id,
    #        'fecha_registro': self.fecha_nacimiento,
    #        'numero_expediente': self.cedula,
    #        'name': self.cedula
    #    })
    #    return expediente


    @api.multi
    def set_to_borrador(self):
        '''Method to change state to draft'''
        self.write({'state': 'borrador'})

    @api.multi
    def set_usuario(self):
        '''Method to change state to alumni'''
        self.write({'state': 'usuarios'})

    @api.multi
    def set_hecho(self):
        '''Method to change state to done'''
        self.write({'state': 'hecho'})

    @api.multi
    def admission_draft(self):
        '''Set the state to draft'''
        self.write({'state': 'draft'})

    @api.multi
    def set_terminado(self):
        self.write({'state': 'terminado'})

    @api.multi
    def cancel_registro(self):
        self.write({'state': 'cancelar'})
