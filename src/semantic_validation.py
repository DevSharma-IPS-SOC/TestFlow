def semantic_validation(data):
    case_report = {
        "valid": False,
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



    


    allowed_status = ["PASS", "FAIL", "SKIP"]
    unique_test_id = ()

    #Semantic Validation True/False/Skip        
    for report in data["test_cases"]:
        if report["test_id"] not in unique_test_id:
            unique_test_id.append(report["test_id"],)
        else:
            case_report["summary"]["duplicate_count"] += 1
            case_report["duplicate_ids"].append(f"{report['test_id']}")

        
        if report["status"] in allowed_status:
            if report["response_time"] >= 0:
                if report["status"] == "PASS":
                    if report["error"] is None:
                        case_report["summary"]["passed"] += 1
                    else:
                        case_report["summary"]["failed"] += 1
                        case_report["errors"].append({"test_id" : report["test_id"], "rule": "PASS_ERROR", "message": "PASS test must have error = None"})

                elif report["status"] == "FAIL":
                    if isinstance(report["error"], str):
                        case_report["summary"]["passed"] += 1
                    else:
                        case_report["summary"]["failed"] += 1
                        case_report["errors"].append({"test_id" : report["test_id"], "rule": "FAIL_ERROR", "message": "FAIL test must contain an error message"})
                        
                    
                elif report["status"] == "SKIP":
                    if report["response_time"] == 0 and report["error"] is None :
                        case_report["summary"]["passed"] += 1
                    if report["response_time"] != 0:
                        case_report["summary"]["failed"] += 1
                        case_report["errors"].append({"test_id" : report["test_id"], "rule": "SKIP_RESPONSE_TIME", "message": "SKIP test must have response_time = 0"})
                    if report["error"] is not None:
                        case_report["summary"]["failed"] += 1
                        case_report["errors"].append({"test_id" : report["test_id"], "rule": "SKIP_ERROR", "message": "SKIP test must have error = None"})
    

            else:
                case_report["summary"]["failed"] += 1
                case_report["errors"].append({"test_id" : report["test_id"], "rule": "NEGATIVE_RESPONSE_TIME", "message": "Response time must be greater than or equal to 0"})
        
        else:
            case_report["summary"]["failed"] += 1
            case_report["errors"].append({"test_id": report["test_id"], "rule": "INVALID_STATUS", "message" : "Status must be one of PASS, FAIL, or SKIP"})

        case_report["summary"]["total"] += 1

    case_report["summary"]["error_count"] = len(case_report["errors"])
    if case_report["errors"] == [] and case_report["duplicate_ids"] == []:
        case_report["valid"] = True


            

    return case_report