from src.parser import load_json
from src.validator import validate_root
from src.semantic_validation import semantic_validation


def main(file_path):
    data = load_json(file_path)
    error_result = validate_root(data)

    print(f"Root Validation --> \nValid: {error_result['valid']} \nErrors: {error_result['errors']} \n")

    if error_result["valid"]:
        semantic_result = semantic_validation(data)
        print("Semantic Validation --> \n")
        for key, value in semantic_result.items():
            print(key,": ",value)

    

if __name__ == "__main__":
    main(input("Enter JSON File Path: "))