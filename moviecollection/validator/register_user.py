from jsonschema import validate


schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "username": {"type": "string"},
    "password": {"type": "string"},
      "required": [
        "username", "password"
      ]
    }
  }


def validate_user_schema(body):
    try:
        validate(body,schema)
        return True
    except:
        return False