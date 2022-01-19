# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo58(models.Model):
	_name = 'odoo58.odoo58'
	_description = 'odoo58.odoo58'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	equipo = fields.Char(string='equipo',required=True)

class zapateria(models.Model):
	_name = 'odoo58.zapateria'
	_description = 'odoo58.zapateria'

	name = fields.Char('idzapateria',required=True)
	marca = fields.Char(string='marca',required=True)
	modelo = fields.Char(string='modelo',required=True)

class liga(models.Model):
	_name = 'odoo58.liga'
	_description = 'odoo58.liga'

	name = fields.Char('idliga',required=True)
	nombreliga = fields.Char(string='nombreliga',required=True)
	nacionalidad = fields.Char(string='nacionalidad',required=True)



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
