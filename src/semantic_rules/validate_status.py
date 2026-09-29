def validate_status(test_case):
    allowed_status = ("PASS", "FAIL", "SKIP")

    if test_case["status"] in allowed_status:
        return []
    else:
        return [{
        "test_id": test_case["test_id"],
        "rule": "INVALID_STATUS",
        "message": "Status must be one of PASS, FAIL, or SKIP" }]