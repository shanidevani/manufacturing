{
    "name": "Production Management",
    "summary": "Sales",
    'description': """

    """,
    'author': "Shani Devani",
    'website': "www.getssolution.com",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "depends": [
        'base','sale_management', 'account','crm','mrp_workorder', 'stock','acount_accountant','purchase', 'point_of_sale',
        'mrp','hr_expense', 'hr_holidays', 'hr_recruitment', 'helpdesk', 'maintenance', 'hr', 'quality_control', 'planning',
        'calendar', 'social', 'appointment', 'im_livechat', 'marketing_automation', 'hr_appraisal', 'hr_attendance', 'lunch',
        'stock_barcode', 'hr_contract', 'industry_fsm',
    ],
    "data": [
        'security/ir.model.access.csv',
    ],
    'sequence': 1,
    'installable': True,
    'auto_install': False,
    'application': True,
}
