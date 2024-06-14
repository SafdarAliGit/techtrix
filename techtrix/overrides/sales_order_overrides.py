import frappe
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder


class SalesOrderOverrides(SalesOrder):
    def on_cancel(self):
        self.custom_status = '<span style="color:red">Cancelled</span>'
        self.db_update()
        frappe.db.commit()

    def on_submit(self):
        self.custom_status = 'Submitted'
        self.db_update()
        frappe.db.commit()
