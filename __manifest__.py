{
    'name': "Airline Database",
    'summary': "Airline Database in Odoo",
    'description': """
        Airline Database module includes those datatables:
            - Airline
            - Airline Alliance""",
    'author': "Serkan Korkusuz",
    'website': "https://sevengates.co/en/products/odoo",
    'category': 'Inventory',
    'version': '1.0',
    'installable': True,
    'auto_install': False,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/airline_alliance_view.xml',
        'views/airline_view.xml',
    ],
    'images': []
}
