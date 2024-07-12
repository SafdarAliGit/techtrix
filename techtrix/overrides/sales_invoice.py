import frappe
from frappe.utils import getdate


def validate(doc, method):
    # Check if there are items and the first item has a delivery note linked
    if doc.items and doc.items[0].delivery_note:
        # Get the delivery note from the first item
        dn = doc.items[0].delivery_note

        # Fetch the Delivery Note document
        dn_doc = frappe.get_doc("Delivery Note", dn)
        dn_posting_date = getdate(dn_doc.posting_date)
        doc_posting_date = getdate(doc.posting_date)

        # Compare the posting dates
        if doc_posting_date < dn_posting_date:
            # Throw an error if the Sales Invoice posting date is before the Delivery Note posting date
            frappe.throw(
                frappe._(
                    "The posting date of the Sales Invoice cannot be before the posting date of the Delivery Note {0}"
                ).format(dn)
            )
