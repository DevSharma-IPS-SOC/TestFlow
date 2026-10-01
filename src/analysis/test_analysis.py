def analyze_tests(data):
    analyzed = {
        "summary": {
            "total": 0,
            "passed": 0,
            "failed" : 0,
            "skipped": 0,
            "pass_percentage": 0.0,
            "fail_percentage": 0.0,
            "skip_percentage": 0.0

        },
        "status_distribution" : {
            "PASS": 0,
            "FAIL": 0,
            "SKIP": 0
        },

        "failure_analysis" : {
            "failed_tests": []
        },
        "performance_analysis": {
            "average_response_time": 0,
            "min_response_time": 0,
            "max_response_time": 0
        }
    }
    TIMEOUT = ["timeout", "time out", "timed out"]
    AUTHENTICATION = ["authentication", "login", "credential"]
    PAYMENT = ["payment", "billing"]

    performance_count = 0

    #calculating the PASS/FAIL/SKIP count
    for test in data["test_cases"]:
        
        if test["status"] == "PASS":
            analyzed["summary"]["passed"] += 1

        #Categorizing the ERRORs into Categories
        elif test["status"] == "FAIL":
            analyzed["summary"]["failed"] += 1
            error = test["error"].lower()
            if any(text in error for text in TIMEOUT):
                analyzed["failure_analysis"]["failed_tests"].append({"test_id": test["test_id"], "test_name": test["test_name"], "error": test["error"], "category": "TIMEOUT"})
            elif any(text in error for text in AUTHENTICATION):
                analyzed["failure_analysis"]["failed_tests"].append({"test_id": test["test_id"], "test_name": test["test_name"], "error": test["error"], "category": "AUTHENTICATION"})
            elif any(text in error for text in PAYMENT):
                analyzed["failure_analysis"]["failed_tests"].append({"test_id": test["test_id"], "test_name": test["test_name"], "error": test["error"], "category": "PAYMENT"})
            else:
                analyzed["failure_analysis"]["failed_tests"].append({"test_id": test["test_id"],"test_name": test["test_name"], "error": test["error"], "category": "OTHER" })
        
        elif test["status"] == "SKIP":
            analyzed["summary"]["skipped"] += 1
        analyzed["summary"]["total"] += 1

        if test["status"] != "SKIP":
            response_time = test["response_time"]
            #total response time
            analyzed["performance_analysis"]["average_response_time"] += response_time

            performance_count += 1

            if performance_count == 1:
                 analyzed["performance_analysis"]["min_response_time"] = response_time
                 analyzed["performance_analysis"]["max_response_time"] = response_time
            else:
                #minimum response time
                if analyzed["performance_analysis"]["min_response_time"] > response_time:
                    analyzed["performance_analysis"]["min_response_time"] = response_time

                #maximum reponse time
                if analyzed["performance_analysis"]["max_response_time"] < response_time:
                            analyzed["performance_analysis"]["max_response_time"] = response_time

    if performance_count > 0:
        #Average response time
        analyzed["performance_analysis"]["average_response_time"] = round(analyzed["performance_analysis"]["average_response_time"] / performance_count, 2)

    #Calculating Analyzed Summary Percentage part
    if analyzed["summary"]["total"] > 0:
        analyzed["summary"]["pass_percentage"] = round(((analyzed["summary"]["passed"] * 100) / analyzed["summary"]["total"]), 1)

        analyzed["summary"]["fail_percentage"] = round(((analyzed["summary"]["failed"] * 100) / analyzed["summary"]["total"]), 1)

        analyzed["summary"]["skip_percentage"] = round(((analyzed["summary"]["skipped"] * 100) / analyzed["summary"]["total"]), 1)

    

    analyzed["status_distribution"]["PASS"] = analyzed["summary"]["passed"]
    analyzed["status_distribution"]["FAIL"] = analyzed["summary"]["failed"]
    analyzed["status_distribution"]["SKIP"] = analyzed["summary"]["skipped"]

    return analyzed