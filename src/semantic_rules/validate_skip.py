def validate_skip(test_case):

    errors = []
    
    if test_case["status"] == "SKIP":
        if test_case["response_time"] != 0:
            errors.append({
                "test_id": test_case["test_id"],
                "rule": "SKIP_RESPONSE_TIME",
                "message": "SKIP test must have response_time = 0" })
        if test_case["error"] is not None:
            errors.append({
            "test_id": test_case["test_id"],
            "rule": "SKIP_ERROR",
            "message": "SKIP test must have error = None" })
        
        return errors
    
    return []