from odoo import models, fields, api, exceptions, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def _attendance_action_change(self, geo_information=None):
        """
        Check In/Check Out action
        Check In: create a new attendance record and capture a webcam image
        Check Out: modify check_out field of the appropriate attendance record and capture a webcam image
        """
        self.ensure_one()
        action_date = fields.Datetime.now()
        print('hello')  # This is the point where we print 'hello' in the backend
        
        if self.attendance_state != 'checked_in':  # Check-In
            # Prepare attendance values
            vals = {
                'employee_id': self.id,
                'check_in': action_date,
            }
            if geo_information:
                vals.update({f'in_{key}': geo_information[key] for key in geo_information})
            self.env['hr.attendance'].create(vals)

        else:  # Check-Out
            # Perform check-out action
            attendance = self.env['hr.attendance'].search(
                [('employee_id', '=', self.id), ('check_out', '=', False)],
                limit=1
            )
            if attendance:
                # Capture an image during check-out
                # base64_image = capture_webcam_image()  # This could be part of the camera dialog logic
                write_vals = {
                    'check_out': action_date,
                }
                if geo_information:
                    write_vals.update({f'out_{key}': geo_information[key] for key in geo_information})
                attendance.write(write_vals)

                # Trigger the Camera Dialog after check-out logic
                return {
                    'type': 'ir.actions.client',
                    'tag': 'open_camera_dialog',  # This is a custom tag that will trigger the JS dialog
                }
            else:
                raise exceptions.UserError(_(
                    'Cannot perform check out on %(empl_name)s, could not find corresponding check in. '
                    'Your attendances have probably been modified manually by human resources.',
                    empl_name=self.sudo().name
                ))

        # Return the action to show the Camera Dialog after the logic has completed
        return {}
