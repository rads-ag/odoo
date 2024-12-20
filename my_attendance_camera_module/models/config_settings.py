from odoo import models, fields,api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allow_image = fields.Boolean(
        string="Allow Webcam Image",
        help="This is a custom boolean setting."
    )

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        # Save the value of the boolean field to the ir.config_parameter model
        self.env['ir.config_parameter'].set_param('my_attendance_camera_module.allow_image', str(self.allow_image))

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # Get the value of the boolean field from the ir.config_parameter model
        res.update(
           allow_image=self.env['ir.config_parameter'].get_param(
                'my_attendance_camera_module.allow_image', 
                'False'  # Default to 'False' if not set
            ) == 'True' 
        )
        return res
    
    @api.model
    def get_camera_enabled(self, *args, **kwargs):
        """Return the boolean value for use in JavaScript."""
        allow_image = self.env['ir.config_parameter'].get_param(
            'my_attendance_camera_module.allow_image', 
            'False'
        ) == 'True'  # Convert string to Boolean
        print(allow_image)  # Debugging statement
        return allow_image
    
