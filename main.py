from src.parser import load_json
from src.validator import validate_root
from src.semantic_validation import semantic_validation

def main():
    data = load_json("data/test_group/group_h.json")
    error_result = validate_root(data)

    print(f"Root Validation --> \nValid: {error_result["valid"]} \nErrors: {error_result["errors"]} \n")

    if error_result["valid"]:
        semantic_result = semantic_validation(data)
        print(f"Semantic Validation --> \n{semantic_result}\n")
        print(f"Passed_test_cases: {len(semantic_result["Passed_test_cases"])} \nFailed: {len(semantic_result["Failed"])} \nDuplicate_test: {len(semantic_result["Duplicate_test"])}\n")

    

if __name__ == "__main__":
    main()