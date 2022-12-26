# -*- coding: utf-8 -*-  

{
    'name': 'Diligo Device Management',
    'description': 'Device Management',
    'summary': 'Device Management',
    'category': 'Construction',
    "sequence": 3,
    'version': '1.0.0',
    'author': 'Chí Nguyễn',
    'company': 'Diligo Holdings',
    'website': "diligo.vn",
    'depends': ['diligo_hr'],
    'data': [
        'wizard/change_employee_used.xml',
        'views/device/device_extra.xml',
        'views/device/device_main.xml',
        'views/device/device_parts_in.xml',
        'views/device/device_group.xml',
        # 'views/device/device_category_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'menu/device_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
