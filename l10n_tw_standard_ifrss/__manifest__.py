# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2017-now  yuanchih-consult.com :chingyun@yuanchih-consult.com

{
    'name': '台灣常用會計科目與台灣財務報表結構(社區版)',
    'version': '1.8',
    'category': 'Localization',
    'license': 'LGPL-3',
    'author': ['元植SmithLin'],
    'depends': ['base', 'account','l10n_tw','accounting_pdf_reports'],
    'website': 'https://www.yuanchih-consult.com',
    'images': ['static/description/twbs-1.png'],
    'description': """


*特別感謝：
★技術支援：新北工具人

★技術支援：先傑電腦

★技術支援：odooTaiwan曾大大



    """,

    'data': [
        'data/account_account_type_data.xml',
#        'data/account.account.template.csv',
        'data/account.financial.report.csv',
        'data/account.financial.report.xml',
        'views/res.company.form.xml',
#        'data/account.account.csv',
    ],
}
