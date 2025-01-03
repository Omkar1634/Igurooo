from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import json
import getpass
import os
from langchain_core.prompts import ChatPromptTemplate
from Prompts.quize import Quize_Prompt

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")


# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)
import json
from jsonschema import validate, ValidationError
from langchain.prompts.chat import ChatPromptTemplate

import json
from jsonschema import validate, ValidationError
from langchain.prompts.chat import ChatPromptTemplate

import json
from jsonschema import validate, ValidationError
from langchain.prompts.chat import ChatPromptTemplate

# Define the JSON schema for your output
quiz_schema = {
    "type": "object",
    "properties": {
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "questionText": {"type": "string"},
                    "options": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "option": {"type": "string"},
                                "isCorrectAnswer": {"type": "boolean"},
                            },
                            "required": ["option", "isCorrectAnswer"],
                        },
                    },
                },
                "required": ["questionText", "options"],
            },
        }
    },
    "required": ["questions"],
}

# Define the prompt template
prompt = ChatPromptTemplate.from_template(
    "system: You are a professor who is creating a quiz for your students. "
    "You must strictly provide a JSON output that aligns with the following schema:\n\n"
    "{schema}\n\n"
    "user: Generate a quiz for the topic {Topic} and sub-topic {Sub_Topic}."
)

# Substitute the schema into the prompt
schema_text = json.dumps(quiz_schema, indent=4)

# Execute the chain
chain = prompt | llm
result = chain.invoke(
    {
        "Topic": "Python",
        "Sub_Topic": "Data Types",
        "schema": schema_text
    }
)

# Parse the LLM result
if hasattr(result, "content"):
    raw_content = result.content
else:
    raw_content = str(result)

try:
    # Remove Markdown formatting if present
    if raw_content.startswith("```json"):
        raw_content = raw_content.strip("```json").strip("```")
    
    # Try to parse the cleaned output as JSON
    parsed_result = json.loads(raw_content)
    # Validate the result against the schema
    validate(instance=parsed_result, schema=quiz_schema)
    print("Validated JSON output:", json.dumps(parsed_result, indent=4))

    # Save the result to a JSON file
    with open("custom_quiz.json", "w", encoding="utf-8") as json_file:
        json.dump(parsed_result, json_file, ensure_ascii=False, indent=4)
    print("Result saved to custom_quiz.json")

except ValidationError as e:
    print("Validation error:", e.message)
except json.JSONDecodeError:
    print("Error: The cleaned LLM output is not valid JSON.")
    print("Raw Output:", raw_content)
