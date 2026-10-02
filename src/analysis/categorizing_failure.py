def categorization(test):
    TIMEOUT = ["timeout", "time out", "timed out"]
    AUTHENTICATION = ["authentication", "login", "credential"]
    PAYMENT = ["payment", "billing"]

    analyzed = {
        "test_id": test["test_id"],
        "test_name": test["test_name"],
        "error": test["error"]
    }
    error_lower = test["error"].lower()

    if any(text in error_lower for text in TIMEOUT):
        analyzed["category"] = "TIMEOUT"
    elif any(text in error_lower for text in AUTHENTICATION):
        analyzed["category"] = "AUTHENTICATION"
    elif any(text in error_lower for text in PAYMENT):
        analyzed["category"] = "PAYMENT"
    else:
        analyzed["category"] = "OTHER"

    return analyzed