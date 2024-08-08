import frappe
from frappe.utils import getdate


def validate(doc, method):
    if doc.docstatus == 0:  # Ensure this runs only before the submission
        # Initialize variables to store purchase receipt and its grand total
        purchase_receipt = None
        pr_grand_total = 0

        # Check if any item in the invoice has a linked purchase receipt
        for item in doc.items:
            if item.purchase_receipt:
                purchase_receipt = item.purchase_receipt
                break

        # If a purchase receipt is found, proceed with validation
        if purchase_receipt:
            pr_grand_total = frappe.get_value("Purchase Receipt", purchase_receipt, 'grand_total') or 0

            # Calculate the total of all linked Purchase Invoices excluding the current one if it's already submitted
            pi_grand_total = frappe.db.sql("""
                SELECT SUM(pi.grand_total)
                FROM `tabPurchase Invoice` pi
                LEFT JOIN `tabPurchase Invoice Item` pii ON pi.name = pii.parent
                WHERE pii.purchase_receipt = %s AND pi.name != %s
            """, (purchase_receipt, doc.name))[0][0] or 0

            pi_grand_total += doc.grand_total  # Include the current invoice's total

            # Validate the summed grand total against the purchase receipt's grand total
            if pi_grand_total > pr_grand_total:
                frappe.throw(
                    frappe._(
                        "The total of linked Purchase Invoices ({0}) exceeds the total of the Purchase Receipt ({1}). Submission blocked.".format(
                            pi_grand_total, pr_grand_total)))
        else:
            # Optionally handle the case where no purchase receipt is linked
            frappe.msgprint(_("No linked Purchase Receipt found in the items of this Purchase Invoice."))
