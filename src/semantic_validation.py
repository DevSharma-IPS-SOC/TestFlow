def semantic_validation(data):
    case_report = {
        "Duplicate_test": [],
        "Failed": [],
        "Passed_test_cases": []
    }
    allowed_status = ["PASS", "FAIL", "SKIP"]
    unique_test_id = []

    #Semantic Validation True/False/Skip        
    for report in data["test_cases"]:
        if report["test_id"] not in unique_test_id:
            unique_test_id.append(report["test_id"])
        else:
            case_report["Duplicate_test"].append(f"{report["test_id"]}")

        
        if report["status"] in allowed_status:
            if report["response_time"] >= 0:
                if report["status"] == "PASS" and report["error"] == None:
                    case_report["Passed_test_cases"].append(f"{report["test_id"]}: Passed Case: Valid")

                elif report["status"] == "FAIL" and isinstance(report["error"], str):
                    case_report["Passed_test_cases"].append(f"{report["test_id"]}: Failed Case: Valid")

                elif report["status"] == "SKIP" and report["response_time"] == 0 and report["error"] == None:
                    case_report["Passed_test_cases"].append(f"{report["test_id"]}: Skipped Case: Valid")

                else:
                    case_report["Failed"].append([f"Invalid: Test Id: {report["test_id"]}, Response time: {report["response_time"]}, Status: {report["status"]}, error: {report["error"]}"])
                
                # Test_case_error["test_id"] = report["test_id"]
                # Test_case_error["response_time"] = report["response_time"]
                # Test_case_error["status"] = report["status"]
                # Test_case_error["error"] = report["error"]

            else:
                case_report["Failed"].append(f"Invalid: Response time on {report["test_id"]}")
        
        else:
            case_report["Failed"].append(f"Invalid: Status on {report["test_id"]}")

            

    return case_report