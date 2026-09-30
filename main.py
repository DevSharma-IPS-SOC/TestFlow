from src.parser import load_json
from src.validator import validate_root
from src.semantic_validation import semantic_validation
from src.analysis.test_analysis import analyze_tests


def main(file_path):
    data = load_json(file_path)
    error_result = validate_root(data)

    print(f"Root Validation --> \nValid: {error_result['valid']} \nErrors: {error_result['errors']} \n")

    if error_result["valid"]:
        semantic_result = semantic_validation(data)
        if semantic_result["valid"]:
            analysis_result = analyze_tests(data)
            print("Analysis Result -->\n")
            for key, value in analysis_result.items():
                print(key,": ",value)

    

if __name__ == "__main__":
    main(input("Enter JSON File Path: "))