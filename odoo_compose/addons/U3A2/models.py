from odoo import models, fields, api

class Equipo(models.Model):
    _name = 'liga.equipo'
    nombre = fields.Char(string="Nombre", required=True)
    fecha_fundacion = fields.Date(string="Fecha de fundacion", required=True)
    liga = fields.Selection([
        ('Primera', 'Primera'),
        ('Segunda', 'Segunda'),
    ], string='Categorias', required=True)
    entrenador = fields.Char(string="Entrenador", required=True)
    jugador_id = fields.One2many(comodel_name='liga.jugador', inverse_name='equipo_id')

class Jugador(models.Model):
    _name = 'liga.jugador'
    nombre = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad", required=True)
    posicion = fields.Selection([
        ('Portero', 'Portero'),
        ('Defensa', 'Defensa'),
        ('Medio', 'Medio'),
        ('Delantero', 'Delantero'),
    ], string='Posicion', required=True)
    equipo_id = fields.Many2one(comodel_name='liga.equipo', inverse_name='jugador_id')
