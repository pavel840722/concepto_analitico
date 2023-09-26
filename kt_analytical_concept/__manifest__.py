# -*- coding: utf-8 -*-

{
    'name': 'Analytical Concept',
    'description': """
              Analytical Concept.
    """,
    'category': 'Accounting/Accounting',
    'depends': ['account', 'purchase', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/kt_analytical_concept_views.xml',
        'views/purchase_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'data/analytical_concept_data.xml'

     ],
    'demo': [],
    'license': 'LGPL-3',
}
