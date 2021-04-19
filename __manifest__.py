#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Idk",
    "version": "12.0.1.1.0",
    "category": "Manufactura",
    "website": "https://github.com/colinak/",
    "author": "Kewitz Colina",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        'base',
        'sale',
        'mrp',
    ],
    "data": [
        'views/mrp_production_view.xml',
        'views/mrp_workorder_views.xml',
    ],
    "demo": [
    ],
}

