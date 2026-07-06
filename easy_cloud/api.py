import frappe

@frappe.whitelist()
def test_endpoint():
    return {
        "status": "success",
        "message": "easy_cloud API is working perfectly!"
    }
@frappe.whitelist()
def get_status():
    return {
        "server_status": "online",
        "database": "connected"
    }