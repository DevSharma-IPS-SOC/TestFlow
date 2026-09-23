from output.dict_error import is_not_dic

def validate_root(data):

    error_dic ={
        "valid": True,
        "errors": []
    }

    if not isinstance(data, dict):
        return is_not_dic()


    # project checking condition
    if "project" not in data:
        error_dic["valid"] = False
        error_dic["errors"].append("Required field 'project' is missing.")
    elif not isinstance(data["project"], str):
        error_dic["valid"] = False
        error_dic["errors"].append("'project' must be a string.")
            
    # run_id  checking condition
    if "run_id" not in data:
        error_dic["valid"] = False
        error_dic["errors"].append("Required field 'run_id' is missing.")
    elif not isinstance(data["run_id"], str):
        error_dic["valid"] = False
        error_dic["errors"].append("'run_id' must be a string.")

    # Test_cases checking condition
    if "test_cases" not in data:
        error_dic["valid"] = False
        error_dic["errors"].append("Required field 'test_cases' is missing.")
    elif not isinstance(data["test_cases"], list):
        error_dic["valid"] = False
        error_dic["errors"].append("'test_cases' must be a list.")
    else:
        index_invalid = []
        for index, dictionary in enumerate(data["test_cases"]):

            if not isinstance(dictionary, dict):
                index_invalid.append(index)

            else:
                if "test_id" not in dictionary:
                    error_dic["valid"] = False
                    error_dic["errors"].append(f"'test_id' is missing in dictionary at {index}.")
                elif not isinstance(dictionary["test_id"], str):
                    error_dic["valid"] = False
                    error_dic["errors"].append("'test_id' must be a string.")

                if "test_name" not in dictionary:
                    error_dic["valid"] = False
                    error_dic["errors"].append(f"'test_name' is missing in dictionary at {index}.")
                elif not isinstance(dictionary["test_name"], str):
                    error_dic["valid"] = False
                    error_dic["errors"].append("'test_name' must be a string.")

                if "status" not in dictionary:
                    error_dic["valid"] = False
                    error_dic["errors"].append(f"'status' is missing in dictionary at {index}.")
                elif not isinstance(dictionary["status"], str):
                    error_dic["valid"] = False
                    error_dic["errors"].append("'status' must be a string.")

                if "response_time" not in dictionary:
                    error_dic["valid"] = False
                    error_dic["errors"].append(f"'response_time' is missing in dictionary at {index}.")
                elif not isinstance(dictionary["response_time"], (int, float)):
                    error_dic["valid"] = False
                    error_dic["errors"].append("'response_time' must be a Int or float.")

                if "error" not in dictionary:
                    error_dic["valid"] = False
                    error_dic["errors"].append(f"'error' is missing in dictionary at {index}.")
                elif not (isinstance(dictionary["error"], str) or dictionary["error"] is None):
                    error_dic["valid"] = False
                    error_dic["errors"].append("'error' must be a string or none.")


        if not index_invalid == []:
            error_dic["valid"] = False
            error_dic["errors"].append(f"{index_invalid} These indices contain values that are not dictionaries.")



    return error_dic