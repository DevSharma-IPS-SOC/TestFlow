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
        "performance_analysis": {}
    }

    #calculating the PASS/FAIL/SKIP count
    for test in data["test_cases"]:
        if test["status"] == "PASS":
            analyzed["summary"]["passed"] += 1
        elif test["status"] == "FAIL":
            analyzed["summary"]["failed"] += 1
            analyzed["failure_analysis"]["failed_tests"].append({"test_id": test["test_id"], "test_name": test["test_name"], "error": test["error"]})
        elif test["status"] == "SKIP":
            analyzed["summary"]["skipped"] += 1
        analyzed["summary"]["total"] += 1

    #Calculating Analyzed Summary Percentage part
    if analyzed["summary"]["total"] > 0:
        analyzed["summary"]["pass_percentage"] = round(((analyzed["summary"]["passed"] * 100) / analyzed["summary"]["total"]), 1)

        analyzed["summary"]["fail_percentage"] = round(((analyzed["summary"]["failed"] * 100) / analyzed["summary"]["total"]), 1)

        analyzed["summary"]["skip_percentage"] = round(((analyzed["summary"]["skipped"] * 100) / analyzed["summary"]["total"]), 1)

    analyzed["status_distribution"]["PASS"] = analyzed["summary"]["passed"]
    analyzed["status_distribution"]["FAIL"] = analyzed["summary"]["failed"]
    analyzed["status_distribution"]["SKIP"] = analyzed["summary"]["skipped"]

    return analyzed