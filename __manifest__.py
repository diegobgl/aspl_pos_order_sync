# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'POS Order Synchronization (Community)',
    'version': '1.0.2',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'summary': 'POS Order sync between Salesman and Cashier',
    'description': "Allow salesperson to only create draft order and send draft order to Cashier for payment",
    'category': 'Point Of Sale',
    'website': 'http://www.acespritech.com',
    'depends': ['base', 'point_of_sale'],
    'price': 25.00,
    'currency': 'EUR',
    'images': [
        'static/description/main_screenshot.png',
    ],
    'data': [
        'views/point_of_sale.xml',
        'views/res_users_view.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'aspl_pos_order_sync/static/src/css/style.css',
            'aspl_pos_order_sync/static/src/js/Chrome.js',
            'aspl_pos_order_sync/static/src/js/db.js',
            'aspl_pos_order_sync/static/src/js/models.js',
            'aspl_pos_order_sync/static/src/js/Popups/AuthenticationPopup.js',
            'aspl_pos_order_sync/static/src/js/Popups/CreateDraftOrderPopup.js',
            'aspl_pos_order_sync/static/src/js/Popups/ReOrderPopup.js',
            'aspl_pos_order_sync/static/src/js/Screens/ChromeWidgets/OrdersIconChrome.js',
            'aspl_pos_order_sync/static/src/js/Screens/OrderScreen/OrderScreen.js',
            'aspl_pos_order_sync/static/src/js/Screens/OrderScreen/PopupProductLines.js',
            'aspl_pos_order_sync/static/src/js/Screens/PaymentScreen/PaymentScreen.js',
            'aspl_pos_order_sync/static/src/js/Screens/ProductScreen/ControlButtons/OrderScreenButton.js',
            'aspl_pos_order_sync/static/src/js/Screens/ProductScreen/NumpadWidget.js',
            'aspl_pos_order_sync/static/src/js/Screens/ProductScreen/ProductScreen.js',
        ],
        'web.assets_qweb': [
            'aspl_pos_order_sync/static/src/xml/**/*',
        ],
    },
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
