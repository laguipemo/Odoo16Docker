# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.
from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_ascending = fields.Boolean('Ascending',default=True)

    @api.model
    def menu_ascending(self):
        records = self.env['ir.ui.menu'].search([('parent_id', '=', False)], order="name")
        count = 10
        for each in records:
            each.write({'sequence': count})
            count = count + 1
        records._copy_sequence()
        return True


class menu_items_arrange(models.Model):
    _inherit = 'ir.ui.menu'

    old_seq = fields.Integer(string="Old Sequence", compute='_copy_sequence', store=True)
    is_ascending = fields.Boolean()

    @api.depends('sequence')
    def _copy_sequence(self):
        for each in self:
            if each.old_seq == False or each.old_seq == 0:
                each.old_seq = each.sequence
            else:
                return False
