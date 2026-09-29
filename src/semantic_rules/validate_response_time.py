def validate_response_time(test_case):

    if test_case["response_time"] >= 0:
        return []
    else:
        return [{
        "test_id": test_case["test_id"],
        "rule": "NEGATIVE_RESPONSE_TIME",
        "message": "Response time must be greater than or equal to 0" }]