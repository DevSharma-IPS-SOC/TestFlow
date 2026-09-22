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
            
    # run_id  checking condition
    if "run_id" not in data:
        error_dic["valid"] = False
        error_dic["errors"].append("Required field 'run_id' is missing.")

    # Test_cases checking condition
    if "test_cases" not in data:
        error_dic["valid"] = False
        error_dic["errors"].append("Required field 'test_cases' is missing.")

    return error_dic