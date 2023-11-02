# -*- coding: utf-8 -*-

from odoo import api, models, fields


class AccountAccount(models.Model):
    _inherit = 'account.account'

    account_type = fields.Selection(
        selection=[
            ("asset_receivable", "Receivable"),
            ("asset_cash", "Bank and Cash"),
            ("asset_current", "Current Assets"),
            ("asset_non_current", "Non-current Assets"),
            ("asset_prepayments", "Prepayments"),
            ("asset_fixed", "Fixed Assets"),
            ("liability_payable", "Payable"),
            ("liability_credit_card", "Credit Card"),
            ("liability_current", "Current Liabilities"),
            ("liability_non_current", "Non-current Liabilities"),
            ("equity", "Equity"),
            ("equity_unaffected", "Current Year Earnings"),
            ("income", "Income"),
            ("income_other", "Other Income"),
            ("expense", "Expenses"),
            ("expense_depreciation", "Depreciation"),
            ("expense_direct_cost", "Cost of Revenue"),
            ("off_balance", "Off-Balance Sheet"),
            ("expense_non-operating_expenses", "營業外費損"),
            ("expense_income_tax_expense", "所得稅費用"),
            ("expense_other_comprehensive", "其他綜合損益"),
            ("expense_discontinued_operations", "停業部門損益"),
        ],
        string="Type", tracking=True,
        required=True,
        compute='_compute_account_type', store=True, readonly=False, precompute=True,
        help="Account Type is used for information purpose, to generate country-specific legal reports, and set the rules to close a fiscal year and generate opening entries."
    )


class AccountAccountTemplate(models.Model):
    _inherit = 'account.account.template'
    
    account_type = fields.Selection(
        selection=[
            ("asset_receivable", "Receivable"),
            ("asset_cash", "Bank and Cash"),
            ("asset_current", "Current Assets"),
            ("asset_non_current", "Non-current Assets"),
            ("asset_prepayments", "Prepayments"),
            ("asset_fixed", "Fixed Assets"),
            ("liability_payable", "Payable"),
            ("liability_credit_card", "Credit Card"),
            ("liability_current", "Current Liabilities"),
            ("liability_non_current", "Non-current Liabilities"),
            ("equity", "Equity"),
            ("equity_unaffected", "Current Year Earnings"),
            ("income", "Income"),
            ("income_other", "Other Income"),
            ("expense", "Expenses"),
            ("expense_depreciation", "Depreciation"),
            ("expense_direct_cost", "Cost of Revenue"),
            ("off_balance", "Off-Balance Sheet"),
            ("expense_non-operating_expenses", "營業外費損"),
            ("expense_income_tax_expense", "所得稅費用"),
            ("expense_other_comprehensive", "其他綜合損益"),
            ("expense_discontinued_operations", "停業部門損益"),
        ],
        string="Type",
        help="These types are defined according to your country. The type contains more information "\
        "about the account and its specificities."
    )


class AccountAccountType(models.Model):
    _inherit = "account.account.type"

    type = fields.Selection(
        selection=[
            ("asset_receivable", "Receivable"),
            ("asset_cash", "Bank and Cash"),
            ("asset_current", "Current Assets"),
            ("asset_non_current", "Non-current Assets"),
            ("asset_prepayments", "Prepayments"),
            ("asset_fixed", "Fixed Assets"),
            ("liability_payable", "Payable"),
            ("liability_credit_card", "Credit Card"),
            ("liability_current", "Current Liabilities"),
            ("liability_non_current", "Non-current Liabilities"),
            ("equity", "Equity"),
            ("equity_unaffected", "Current Year Earnings"),
            ("income", "Income"),
            ("income_other", "Other Income"),
            ("expense", "Expenses"),
            ("expense_depreciation", "Depreciation"),
            ("expense_direct_cost", "Cost of Revenue"),
            ("off_balance", "Off-Balance Sheet"),
            ("expense_non-operating_expenses", "營業外費損"),
            ("expense_income_tax_expense", "所得稅費用"),
            ("expense_other_comprehensive", "其他綜合損益"),
            ("expense_discontinued_operations", "停業部門損益"),   
        ],
        string="Type",
        help="These types are defined according to your country. The type contains more information " \
             "about the account and its specificities."
    )