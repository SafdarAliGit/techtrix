import frappe
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder


class SalesOrderOverrides(SalesOrder):
    def before_save(self):
        self.update_custom_status()
        self.db_update()

    def after_save(self):
        self.update_custom_status()
        self.db_update()

    def before_submit(self):
        self.update_custom_status()
        self.db_update()

    def before_cancel(self):
        self.update_custom_status()
        self.db_update()

    def on_update_after_submit(self):
        self.update_custom_status()
        self.db_update()

    def before_insert(self):
        self.update_custom_status()
        self.db_update()

    def after_insert(self):
        self.update_custom_status()
        self.db_update()

    def on_cancel(self):
        self.custom_status = '<span style="color:red">Cancelled</span>'
        self.db_update()
        frappe.db.commit()

    def on_submit(self):
        self.custom_status = 'Submitted'
        self.db_update()
        frappe.db.commit()

    def update_custom_status(self):
        if self.docstatus == 0:
            self.custom_status = "Draft"
        elif self.docstatus == 1:
            self.custom_status = "Submitted"
        elif self.docstatus == 2:
            self.custom_status = '<span style="color:red">Cancelled</span>'
