from odoo import models, fields

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    checkin_image = fields.Binary('Check-in Image')
    checkout_image = fields.Binary('Check-out Image')
