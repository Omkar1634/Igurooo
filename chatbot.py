import streamlit as st
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from jsonschema import validate, ValidationError
from Prompts.quize import Quize_Prompt

# Initialize Groq LLM
def initialize_llm():
    return ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )

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
def create_prompt():
    return ChatPromptTemplate.from_template(
        """system: You are a professor who is creating a quiz for your students. Based on the number of questions {no_of_questions},
        generate a quiz on the topic {Topic} and sub-topic {Sub_Topic}.
        The quiz should have multiple-choice questions with 4 options each.
        Each question should have only one correct answer. The quiz should be in JSON format and should follow the following schema:

        {schema}

        user: Generate a quiz based on the topic {Topic}, sub-topic {Sub_Topic}, and {no_of_questions} questions."""
    )


# Streamlit App
st.title("Quiz Generator")

# Inputs
topic = st.text_input("Enter the Topic")
sub_topic = st.text_input("Enter the Sub-Topic",)
no_of_questions = st.number_input("Enter the number of questions")

if st.button("Generate Quiz"):
    with st.spinner("Generating quiz..."):
        try:
            # Initialize LLM and prompt
            llm = initialize_llm()
            prompt = create_prompt()
            
            # Substitute the schema into the prompt
            schema_text = json.dumps(quiz_schema, indent=4)
            chain = prompt | llm
            
            # Generate result
            result = chain.invoke({
                "Topic": topic,
                "Sub_Topic": sub_topic,
                "schema": schema_text,
                "no_of_questions": no_of_questions
            })
            
            # Extract and validate result
            raw_content = result.content if hasattr(result, "content") else str(result)
            
            # DEBUG: Show raw content for troubleshooting
            st.text("Raw Output:")
            st.code(raw_content, language="json")

            # Clean up and parse the JSON output
            if raw_content.startswith("```json"):
                raw_content = raw_content.strip("```json").strip("```")
            
            # Parse JSON
            parsed_result = json.loads(raw_content)
            validate(instance=parsed_result, schema=quiz_schema)
            
            # Display validated JSON output
            st.json(parsed_result)

        except ValidationError as e:
            st.error(f"Validation Error: {e.message}")
        except json.JSONDecodeError:
            st.error("The generated output is not valid JSON.")
            st.text("Raw Output:")
            st.code(raw_content, language="json")
        except Exception as e:
            st.error(f"An error occurred: {e}")
