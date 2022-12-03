from odoo import api, fields, models, tools, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = 'Purchase order'

    branch_id = fields.Many2one('company.branches', string='Branch', domain="[('company_id','=',company_id)]",default=lambda self: self.env.user.branch_id[0].id)
    
    
    # def action_view_invoice(self,moves):
    #     result = super(PurchaseOrder,self).action_view_invoice(moves)
    #     result['context'].update({'default_branch_id':self.branch_id.id})
    #     return result
