import json
from jsonschema import validate, ValidationError, SchemaError
def check_json_against_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
        return "Validation successful"
    except ValidationError as ex:
        return f"Validation error: {ex.message}. Path: {'/'.join(map(str, ex.path))}"
    except SchemaError as ex:
        return f"Schema error: {ex.message}"
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as ex:
        print(f"Error: Failed to decode JSON from '{file_path}'. Details: {ex}")
        return None
def main():
    schema = load_json_file("ex_1_schema.json")
    if schema is None:
        return
    for file_name in ["ex_1.json", "err_ex_1.json"]:
        json_data = load_json_file(file_name)
        if json_data is None:
            continue
        result = check_json_against_schema(json_data, schema)
        print(f"Result for '{file_name}': {result}")
if __name__ == "__main__":
    main()
