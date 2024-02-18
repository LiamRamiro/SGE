from odoo import models, fields, api

class Cerveza(models.Model):
    _name = 'examen.cerveza'
    _description = 'Modelo para gestionar cervezas'
    tipo = fields.Char(string='Tipo')
    nombre = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    contenido_alcohol = fields.Float(string='Contenido de alcohol (%)')
    precio_unidad = fields.Float(string='Precio por unidad')
    volumen_unidad = fields.Float(string='Volumen por unidad (ml)')
    lote_produccion_id = fields.One2many(comodel_name='examen.lote_produccion', inverse_name='cerveza_id')
    ingrediente_id = fields.One2many(comodel_name='examen.ingrediente', inverse_name='cerveza_id')
    distribuidor_id = fields.Many2many(comodel_name='examen.distribuidor', inverse_name='cerveza_id')
    disponible = fields.Boolean(string='Disponible')


class LoteProduccion(models.Model):
    _name = 'examen.lote_produccion'
    _description = 'Lote de Producción'
    fecha_inicio = fields.Date(string='Fecha de Inicio de Producción')
    fecha_finalizacion = fields.Date(string='Fecha Estimada de Finalización')
    cantidad_producida = fields.Integer(string='Cantidad Producida')
    estado = fields.Selection([
        ('en proceso', 'En Proceso'),
        ('completo', 'Completo'),
        ('en espera de empaquetado', 'En Espera de Empaquetado')],
        string='Estado')
    cerveza_id = fields.Many2one(comodel_name='examen.cerveza', inverse_name='lote_produccion_id')
    empaquetado_id = fields.One2many(comodel_name='examen.empaquetado', inverse_name='lote_produccion_id')

class Ingrediente(models.Model):
    _name = 'examen.ingrediente'
    _description = 'Ingredientes de la cerveza'
    nombre = fields.Char(string='Nombre')
    tipo = fields.Selection([
        ('malta', 'Malta'),
        ('lupulo', 'Lúpulo'),
        ('levadura', 'Levadura'),
        ('agua', 'Agua'),
        ('otro', 'Otro')],
        string='Tipo'
    )
    cantidad_disponible = fields.Float(string='Cantidad Disponible (kg/l)')
    cerveza_id = fields.Many2many(comodel_name='examen.cerveza', inverse_name='ingrediente_id')

class Empaquetado(models.Model):
    _name = 'examen.empaquetado'
    _description = 'Empaquetado'
    lote_produccion_id = fields.Many2one(comodel_name='examen.lote_produccion', inverse_name='empaquetado_id')
    fecha_empaquetado = fields.Date(string='Fecha de Empaquetado')
    cantidad_empaquetada = fields.Integer(string='Cantidad Empaquetada')


class Distribuidor(models.Model):
    _name = 'examen.distribuidor'
    _description = 'Distribuidor'
    nombre = fields.Char(string='Nombre')
    direccion = fields.Text(string='Dirección')
    telefono_contacto = fields.Char(string='Teléfono de Contacto')
    cerveza_id = fields.Many2many(comodel_name='examen.cerveza', inverse_name='distribuidor_id')
