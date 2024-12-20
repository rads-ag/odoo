from odoo import http, exceptions
from odoo.http import request
import base64

class AttendanceImageController(http.Controller):

    @http.route('/attendance/save_image', type='json', auth='user')
    def save_image(self, **kwargs):
        # Extract the image data
        image_data = kwargs.get('image_data')
        is_check_out = kwargs.get('is_check_out', False)  # Flag to determine if it's a check-out image
        print(image_data)
        
        if not image_data:
            return {'error': 'No image data received'}
        
        # Get the current logged-in user
        user = request.env.user

        # Find the employee linked to the logged-in user
        employee = request.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)

        if employee:
            print('Employee exists')

            # Find the most recent attendance record where check_out is False (still checked in)
            attendance = request.env['hr.attendance'].search(
                [('employee_id', '=', employee.id)],
                order='check_in desc',  # Order by check_in, most recent first
                limit=1
            )

            if attendance:
                if attendance.check_out:
                    # If it's check-in image, save it in the checkin_image field
                    attendance.write({'checkout_image': image_data})
                    print('Check-out image saved')
                else:
                    # If it's check-out image, save it in the checkout_image field and set check_out time
                    attendance.write({'checkin_image': image_data})
                    print('Check-in image saved')

            else:
                print('No active attendance record found')

        else:
            print('Employee does not exist')

        return {'success': 'Image saved successfully'}



        
        