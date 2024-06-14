import frappe
from erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder


class PurchaseOrderOverrides(PurchaseOrder):
    def on_cancel(self):
        self.custom_status = '<span style="color:red">Cancelled</span>'
        self.db_update()
        frappe.db.commit()

    def on_submit(self):
        self.custom_status = 'Submitted'
        self.db_update()
        frappe.db.commit()
