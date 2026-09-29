def validate_fail(test_case):

    if test_case["status"] == "FAIL":
        if isinstance(test_case["error"], str):
            return []
    
        return [{
        "test_id": test_case["test_id"],
        "rule": "FAIL_ERROR",
        "message": "FAIL test must contain an error message" }]
    
    return []