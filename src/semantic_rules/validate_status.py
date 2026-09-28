from src.semantic_validation import semantic_validation



def validate_status(data):
    allowed_status = ("PASS", "FAIL", "SKIP")

    if data["status"] in allowed_status:
        return True
    else:
        return (case_report["summary"]["failed"] += 1), (case_report["errors"].append({"test_id": report["test_id"], "rule": "INVALID_STATUS", "message" : "Status must be one of PASS, FAIL, or SKIP"}))