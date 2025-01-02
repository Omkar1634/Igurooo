"This will create a quiz for the user to take as a assessment of their knowledge."




Quize_Prompt = """
Generate questions that align with the following requirements, given a specific input text passage. 
Ensure your structured JSON output is correct and follows the specified format. 
Strictly return the result in the following JSON format:

{
    "title": "QuizStateBaseModel",
    "description": "Pydantic BaseModel for a quiz. A quiz can have many questions belonging to MCQ.",
    "attributes": {
        "topic": "The topic covered in this quiz.",
        "question_count": "The total number of questions in this quiz.",
        "question_type": "The question type of the questions in this quiz.",
        "question": "The list of questions."
    },
    "type": "object",
    "properties": {
        "topic": {
            "title": "Topic",
            "description": "The topic covered in this quiz.",
            "type": "string"
        },
        "question_count": {
            "title": "Question Count",
            "description": "The total number of questions in this quiz.",
            "type": "integer"
        },
        "question_type": {
            "title": "Question Type",
            "description": "The question type of the questions in this quiz.",
            "enum": ["MCQ"],
            "type": "string"
        },
        "question": {
            "title": "Question",
            "description": "The list of questions. Supports different types of questions.",
            "type": "array",
            "items": {
                "anyOf": [
                    { "$ref": "#/definitions/MCQQuestionState" },
                    { "$ref": "#/definitions/TrueFalseQuestionState" }
                ]
            }
        }
    },
    "required": ["topic", "question_count", "question_type", "question"],
    "definitions": {
        "MCQQuestionState": {
            "title": "MCQQuestionState",
            "description": "Class for a single MCQ question.",
            "attributes": {
                "id": "The id of the question.",
                "question_type": "The classification of the question data model type i.e., 'MCQ'.",
                "question": "The text of the single-choice question.",
                "option": "A list of possible answer options (strings).",
                "answer": "The index of the correct answer option in the array 'option'."
            },
            "type": "object",
            "properties": {
                "question_type": {
                    "title": "Question Type",
                    "description": "The classification of the question data model type i.e., 'MCQ'.",
                    "enum": ["MCQ"],
                    "type": "string"
                },
                "question": {
                    "title": "Question",
                    "description": "The text of the multiple-choice question.",
                    "type": "string"
                },
                "option": {
                    "title": "Option",
                    "description": "A list of possible answer options (strings).",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "answer": {
                    "title": "Answer",
                    "description": "The correct answer to the multiple-choice question, must be in the list 'option'.",
                    "type": "string"
                }
            },
            "required": ["question_type", "question", "option", "answer"]
        },
        "TrueFalseQuestionState": {
            "title": "TrueFalseQuestionState",
            "description": "Class for a single True/False question.",
            "attributes": {
                "question_type": "The classification of the question data model type i.e., 'MCQ'.",
                "question": "The text of the single-choice question.",
                "option": "A list of possible answer options (strings). Default is ['False', 'True'].",
                "answer": "The correct answer to the true/false question, must be in the list 'option'."
            },
            "type": "object",
            "properties": {
                "question_type": {
                    "title": "Question Type",
                    "description": "The classification of the question data model type i.e., 'MCQ'.",
                    "enum": ["MCQ"],
                    "type": "string"
                },
                "question": {
                    "title": "Question",
                    "description": "The text of the true/false question.",
                    "type": "string"
                },
                "option": {
                    "title": "Option",
                    "description": "A list of possible answer options (strings). Default is ['False', 'True'].",
                    "default": ["False", "True"],
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "answer": {
                    "title": "Answer",
                    "description": "The correct answer to the true/false question, must be in the list 'option'.",
                    "type": "string"
                }
            },
            "required": ["question_type", "question", "answer"]
        }
    }
}
"""
