from src.parser import load_json
from src.validator import validate_root

def main():
    data = load_json("data/invalid_structure.json")
    result = validate_root(data)

    
    print(f"Valid: {result["valid"]} \nErrors: {result["errors"]}")

if __name__ == "__main__":
    main()