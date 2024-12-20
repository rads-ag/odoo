{
    "name": " test",
    "description": """ """,
    "version": "17.0.1.0.0",
    "summary": "",
    "category": "Services",
    "author": "Zehntech Technologies Inc.",
    "company": "Zehntech Technologies Inc.",
    "maintainer": "Zehntech Technologies Inc.",
    "contributor": "Zehntech Technologies Inc.",
    "website": "https://www.zehntech.com/",
    "support": "odoo-support@zehntech.com",
    "depends":['hr_attendance','web'],
    "data": [
       
        'views/attendance_view.xml',
        'views/config_settings.xml',
        
       ],
    "assets": {
        'web.assets_backend': [
                               
           
            'my_attendance_camera_module/static/src/xml/camera_dialog_templates.xml',
            'my_attendance_camera_module/static/src/js/CameraDialog.js',
             'my_attendance_camera_module/static/src/js/hr_attendance_custom.js',
            
              
             
                         
    ],
        'hr_attendance.assets_public_attendance': [
                               
           
            'my_attendance_camera_module/static/src/xml/camera_dialog_templates.xml',
            'my_attendance_camera_module/static/src/js/CameraDialog.js',
             'my_attendance_camera_module/static/src/js/kiosk.js',
            
              
             
                         
    ],
},
    "license": "OPL-1",  
    "installable": True,
    "application": True,
    "auto_install": False,
    "price": 00.00,
    "currency": "USD",
     
}
