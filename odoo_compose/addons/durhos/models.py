from odoo import api, models, fields

class Moneda(models.Model):
    _name = 'durhos.moneda'
    cod_moneda = fields.Char(string="codigo", required=True)
    valor_facial = fields.Float(string="valor facial", required=True)
    unidad_monetaria = fields.Selection([
        ('Pesetas', 'pesetas'),
        ('euros', 'euros'),
        ('libras', 'libras')
    ], string='unidad', required=True)
    diametro = fields.Float(string="diametro", required=True)
    peso = fields.Float(string="peso(gr)", required=True)
    descripcion = fields.Char(string="descripcion", required=True)
    metal_id = fields.One2many(comodel_name='durhos.metal', inverse_name='moneda_id')
    molde_id = fields.One2many(comodel_name='durhos.molde', inverse_name='moneda_id')
    estado_moneda_id = fields.Many2one(comodel_name='durhos.estado_moneda', inverse_name='moneda_id')

class Metal(models.Model):
    _name = 'durhos.metal'
    proporcion = fields.Float(string="proporcion", required=True)
    ley = fields.Float(string="ley", required=True)
    moneda_id = fields.Many2one(comodel_name='durhos.moneda', inverse_name='metal_id')

class Molde(models.Model):
    _name = 'durhos.molde'
    _descripcion = 'Molde para la acuñacion de monedas'
    cod_molde = fields.Char(string="codigo", required=True)
    ano_acunacion = fields.Date(required=True)
    ano_visible = fields.Date(string="año visible", required=True)
    moneda_id = fields.Many2one(comodel_name='durhos.moneda', inverse_name='molde_id')
    estrella_id = fields.One2many(comodel_name='durhos.estrella', inverse_name='molde_id')

class Estrella(models.Model):
    _name = 'durhos.estrella'
    # _descripcion = 'Estrella de la moneda'  # Comentario no necesario
    fecha = fields.Date(required=True)
    molde_id = fields.Many2one(comodel_name='durhos.molde', inverse_name='estrella_id')

class Estado_moneda(models.Model):
    _name = 'durhos.estado_moneda'
    _descripcion = 'Estado de la moneda'
    precio = fields.Float(string="precio", required=True)
    estado_conservacion = fields.Selection([
        ('BC', 'MBC'),
        ('EBC', 'SC'),
    ], string='estado', required=True)
    nombre = fields.Char(string="nombre", required=True)
    descripcion = fields.Char(string="descripcion", required=True)
    moneda_id = fields.One2many(comodel_name='durhos.moneda', inverse_name='estado_moneda_id')

class Ejemplares(models.Model):
    _name = 'durhos.ejemplares'
    _descripcion = 'Ejemplares de la moneda'
    cod_moneda = fields.Char(string="codigo", required=True)
    num_correlativo = fields.Integer(string="numero correlativo", required=True)
    precio = fields.Float(string="precio", required=True)
    fecha_adquisicion = fields.Date(required=True)
    proveedores_id = fields.Many2many(comodel_name='durhos.proveedores', inverse_name='ejemplares_id')
    clientes_id = fields.Many2one(comodel_name='durhos.clientes', inverse_name='ejemplares_id')
    estado_ejemplar_id = fields.Many2one(comodel_name='durhos.estado_ejemplar', inverse_name='ejemplares_id')

class Proveedores(models.Model):
    _name = 'durhos.proveedores'
    _descripcion = 'Proveedores de la moneda'
    nombre = fields.Char(string="nombre", required=True)
    direccion = fields.Char(string="direccion", required=True)
    telefono = fields.Integer(string="telefono", required=True)
    ejemplares_id = fields.Many2many(comodel_name='durhos.ejemplares', inverse_name='proveedores_id')

class Clientes(models.Model):
    _name = 'durhos.clientes'
    _descripcion = 'Clientes de la moneda'
    fecha_venta = fields.Date(required=True)
    precio_venta = fields.Float(string="precio venta", required=True)
    nombre_cliente = fields.Char(string="nombre cliente", required=True)
    direccion = fields.Char(string="direccion", required=True)
    telefono = fields.Integer(string="telefono", required=True)
    num_compras = fields.Integer(string="numero de compras", required=True)
    ejemplares_id = fields.One2many(comodel_name='durhos.ejemplares', inverse_name='clientes_id')

class Estado_ejemplar(models.Model):
    _name = 'durhos.estado_ejemplar'
    _descripcion = 'Estado del ejemplar'
    ajuste = fields.Selection([
        ('+', '-'),
    ], string='ajuste', required=True)
    comentario = fields.Char(string="comentario", required=True)
    ejemplares_id = fields.One2many(comodel_name='durhos.ejemplares', inverse_name='estado_ejemplar_id')


