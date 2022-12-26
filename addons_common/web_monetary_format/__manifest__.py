# See LICENSE file for full copyright and licensing details.

{
    "name": "Web Monetary Format",
    "version": "15.0.1.0.0",
    "author": "",
    "maintainer": "",
    "complexity": "easy",
    "depends": ["web"],
    "license": "AGPL-3",
    "category": "Tools",
    "description": """
     
    """,
    "summary": """
        Touch screen enable so user can add signature with touch devices.
        Digital signature can be very usefull for documents.
    """,
    "images": [],
    "data": [],
    "website": "",
    'assets': {
        'web.assets_backend': [
            'web_monetary_format/static/src/js/monetary_format.js',
        ],
    },
    "qweb": ["static/src/xml/monetary_format.xml"],
    "installable": True,
    "auto_install": False,
}
