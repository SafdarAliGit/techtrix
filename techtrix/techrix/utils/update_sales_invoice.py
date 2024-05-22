import frappe

@frappe.whitelist()
def update_sales_invoice():
    # Get all Sales Invoice records
    sales_invoices = frappe.get_list("Sales Invoice", fields=["name", "sales_person"])

    # Count the number of records affected
    num_records_affected = 0

    for invoice in sales_invoices:
        sales_person = invoice.get("sales_person")
        if sales_person:
            # Create Sales Team record
            sales_team = frappe.new_doc("Sales Team")
            sales_team.sales_person = sales_person
            sales_team.allocated_percentage = 100
            # Set parent and parenttype to link to Sales Invoice
            sales_team.parent = invoice["name"]
            sales_team.parenttype = "Sales Invoice"
            sales_team.parentfield = "sales_team"
            sales_team.insert(ignore_permissions=True)
            num_records_affected += 1
    frappe.db.commit()

    # Return a success message with the number of records affected
    return {
        "success": True,
        "message": f"Successfully created {num_records_affected} Sales Team records."
    }
