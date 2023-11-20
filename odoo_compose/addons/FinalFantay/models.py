from odoo import models, fields, api

class Shinra(models.Model):
    _name = 'fantasy.shinra'
    _description = 'SHINRA Member'
    name = fields.Char(string='Nombre')
    fecha_nacimiento = fields.Date(string='Fecha nacimiento', required=True)


class Turcos(models.Model):
    _name = 'fantasy.turcos'
    _description = 'TURCOS Member'
    name = fields.Char(string='Nombre')
    fecha_nacimiento = fields.Date(string='Fecha nacimiento', required=True)
    rango = fields.Char(string='Rango')
    avalancha_id = fields.One2many(comodel_name='fantasy.avalancha', inverse_name='turcos_id')
    


class Soldado(models.Model):
    _name = 'fantasy.soldado'
    _description = 'SOLDADO Member'
    name = fields.Char(string='Nombre')
    fecha_nacimiento = fields.Date(string='Fecha nacimiento', required=True)
    arma_especial = fields.Char(string='Arma especial')
    clase = fields.Selection([('Primera clase', 'primera clase'), ('Segunda clase', 'segunda clase')], string='Clase del soldado')
    indice_locura = fields.Integer(string='Indice locura')
    
    


class Armas(models.Model):
    _name = 'fantasy.armas'
    _description = 'Weapon'
    name = fields.Char(string='Nombre')
    material_fabricacion = fields.Char(string='Material fabricacion')
    ranuras = fields.Integer(string='Ranuras donde alojar materia')
    materias_id = fields.Many2many(comodel_name='fantasy.materia', inverse_name='armas_id')
    


class Materias(models.Model):
    _name = 'fantasy.materias'
    _description = 'Materia'
    name = fields.Char(string='Nombre')
    tipo = fields.Selection([('invocacion', 'Invocación'), ('magia negra', 'Magia Negra'), ('apoyo', 'Apoyo')], string='Type')
    ranuras = fields.Integer(string='Ranuras')
    armas_id = fields.Many2many(comodel_name='fantasy.armas', inverse_name='materias_id')
    


class Avalancha(models.Model):
    _name = 'fantasy.avalancha'
    _description = 'AVALANCHA Member'
    name = fields.Char(string='Nombre')
    arma_especial = fields.Char(string='Arma especial')
    antiguo_soldado = fields.Boolean(string='Antiguo Soldado')
    misiones = fields.Integer(string='Misiones participadas')
    reserva = fields.Boolean(string='En reserva')
    fecha_entrada_reserva = fields.Date(string='Fecha entrada reserva')
    turcos_id = fields.Many2one(comodel_name='fantasy.turcos', inverse_name='avalancha_id')
    
  