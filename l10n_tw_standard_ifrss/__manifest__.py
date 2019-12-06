# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2017-now  yuanchih-consult.com :chingyun@yuanchih-consult.com

{
    'name': u'會計科目表 - 台灣企業會計準則 - IFRSs會計科目',
    'version': '1.0',
    'category': 'Localization',
    'author': ['www.yuanchih-consult.com'],

    'website': 'https://www.yuanchih-consult.com',
    'description': """
Including the following data in the Accounting Standards for Business Enterprises

* Chart of Accounts

* Account templates

* Tax templates

* Taiwan localization Data

* Taiwan Financial Report

* Chang Rounding

本模塊提供一鍵安裝之解決方案完成台灣會計與稅務設定在地化

* 台灣企業會計準則-一般行業IFRSs會計科目 (民國106.10.12修訂)

* 台灣企業會計準則-會計項目模板

* 台灣營業稅設定

* 台灣稅務扣繳設定

* 台灣銀行分行資訊

* 台灣二代健保與補充保費設定

* 台灣縣市資料

* 台灣財務報表設定

* 調整小數點位數


*特別感謝：

★社群支持：工具人

★技術支援：先捷電腦





    """,
    'depends': ['base', 'account','accounting_pdf_reports'],
    'data': [
        'data/account_account_type_data.xml',
        'data/l10n_tw_standard_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_templates.xml',
        'data/account_chart_template_data.xml',
        'data/data_taiwan.xml',
        'data/account.financial.report.csv',
        'data/account.financial.report.xml',
        'data/res.currency.xml',
        'data/res.bank.csv',
        'views/res.company.form.xml',
    ],
}
