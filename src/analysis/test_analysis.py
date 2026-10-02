from src.analysis.categorizing_failure import categorization

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
            "failed_tests": [],
            "failed_frequency": {"TIMEOUT": 0, "AUTHENTICATION": 0, "PAYMENT": 0, "OTHER": 0},
            "failure_percentage":{
                 "TIMEOUT": 0.0,
                 "AUTHENTICATION": 0.0,
                 "PAYMENT": 0.0,
                 "OTHER": 0.0
            },
            "failure_dominance": []

        },
        "performance_analysis": {
            "average_response_time": 0,
            "min_response_time": 0,
            "max_response_time": 0,
        }
    }
    performance_count = 0

    #calculating the PASS/FAIL/SKIP count
    for test in data["test_cases"]:

        if test["status"] == "PASS":
            analyzed["summary"]["passed"] += 1

        #Categorizing the ERRORs into Categories For FAIL Status
        elif test["status"] == "FAIL":
            analyzed["summary"]["failed"] += 1
            category = categorization(test) 
            #categorizing failures
            analyzed["failure_analysis"]["failed_tests"].append(category)
            if category["category"] not in analyzed["failure_analysis"]["failed_frequency"]:
                analyzed["failure_analysis"]["failed_frequency"][category["category"]] = 1
            else:
                analyzed["failure_analysis"]["failed_frequency"][category["category"]] += 1

        #Counting SKIP Tests
        if test["status"] == "SKIP":
            analyzed["summary"]["skipped"] += 1

        #Counting Total Tests
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

    if analyzed["summary"]["failed"] > 0:
        #calculating failed percentage
        total_failed_frequency = analyzed["summary"]["failed"]
        
        #calculating TIMEOUT percentage
        analyzed["failure_analysis"]["failure_percentage"]["TIMEOUT"] = analyzed["failure_analysis"]["failed_frequency"]["TIMEOUT"] / total_failed_frequency * 100

        #calculating AUTHENTICATION percentage
        analyzed["failure_analysis"]["failure_percentage"]["AUTHENTICATION"] = analyzed["failure_analysis"]["failed_frequency"]["AUTHENTICATION"] / total_failed_frequency * 100

        #calculating PAYMENT percentage
        analyzed["failure_analysis"]["failure_percentage"]["PAYMENT"] = analyzed["failure_analysis"]["failed_frequency"]["PAYMENT"] / total_failed_frequency * 100

        #calculating OTHER percentage
        analyzed["failure_analysis"]["failure_percentage"]["OTHER"] = analyzed["failure_analysis"]["failed_frequency"]["OTHER"] / total_failed_frequency * 100

        #Calculate Dominant Failure
        largest_count = 0
        for value in analyzed["failure_analysis"]["failed_frequency"].values():
            if largest_count < value:
                largest_count = value
        
        for key, value in analyzed["failure_analysis"]["failed_frequency"].items():
            if largest_count == value:
                analyzed["failure_analysis"]["failure_dominance"].append(key)
    
    analyzed["status_distribution"]["PASS"] = analyzed["summary"]["passed"]
    analyzed["status_distribution"]["FAIL"] = analyzed["summary"]["failed"]
    analyzed["status_distribution"]["SKIP"] = analyzed["summary"]["skipped"]

    return analyzed