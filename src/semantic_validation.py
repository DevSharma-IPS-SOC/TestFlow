from src.semantic_rules import validate_status, validate_response_time, validate_pass, validate_fail, validate_skip

def semantic_validation(data):
    case_report = {
        "valid": True,
        "summary":{
            "total": 0,
            "passed": 0,
            "failed": 0,
            "error_count": 0,
            "duplicate_count": 0
        },
        "errors":[],
        "duplicate_ids": []
    }

    unique_test_id = set()

#Semantic Validation True/False/Skip        
    for report in data["test_cases"]:
        case_report["summary"]["total"] += 1

        if report["test_id"] not in unique_test_id:
            unique_test_id.add(report["test_id"])

        else:
            case_report["duplicate_ids"].append(report["test_id"])
            case_report["summary"]["duplicate_count"] += 1


        report_error = []
        report_error.extend(validate_status(report))
        report_error.extend(validate_response_time(report))
        report_error.extend(validate_pass(report))
        report_error.extend(validate_fail(report))
        report_error.extend(validate_skip(report))

        if report_error == []:
            case_report["summary"]["passed"] += 1
        else:
            case_report["summary"]["failed"] += 1

        case_report["errors"].extend(report_error)

    case_report["summary"]["error_count"] = len(case_report["errors"])

    if case_report["errors"] != [] or case_report["duplicate_ids"] != []:
        case_report["valid"] = False

    return case_report