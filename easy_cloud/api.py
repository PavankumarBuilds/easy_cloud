import frappe

@frappe.whitelist()
def test_endpoint():
    return {
        "status": "success",
        "message": "easy_cloud API is working perfectly!"
    }