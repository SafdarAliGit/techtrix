import frappe


@frappe.whitelist()
def get_bank_balance():
    bank_query = """
        SELECT 
            gle.account,
            SUM(gle.debit) as debit,
            SUM(gle.credit) as credit, 
            SUM(gle.debit - gle.credit) as balance
        FROM 
            `tabGL Entry` gle
        INNER JOIN 
            `tabAccount` acc ON gle.account = acc.name
        WHERE 
            gle.is_cancelled = 0 
            AND acc.account_type = 'Bank'
            AND acc.is_group = 0
        GROUP BY 
            gle.account 
        ORDER BY
            gle.account
    """

    # Execute the query
    result = frappe.db.sql(bank_query, as_dict=True)
    if result:
        return result
    else:
        return None
