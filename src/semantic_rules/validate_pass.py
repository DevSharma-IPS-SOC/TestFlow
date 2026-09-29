def validate_pass(test_case):

    if test_case["status"] == "PASS":
        if test_case["error"] is None:
            return []
    
        return [{
        "test_id": test_case["test_id"],
        "rule": "PASS_ERROR",
        "message": "PASS test must have error = None" }]
    
    return []