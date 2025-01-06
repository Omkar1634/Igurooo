Quize_Prompt = """
You are designing a self-assessment quiz to evaluate understanding of a  Main Topic {Main_Topic} with/without Sub-Topics{Sub_Topics} or they might upload a document. 
The quiz should be suitable for an audience with a level of understanding {Level_of_Understanding}. 

Follow these steps to create the quiz:

1. Define the Scope
    Main Topic: {Main_Topic} [ e.g., "Machine Learning"].
    Sub-Topics (if applicable): {Sub_Topics} [ e.g., "Supervised Learning, Unsupervised Learning, Reinforcement Learning"].
    Level of Understanding: {Level_of_Understanding} [e.g., "Beginner, Intermediate, Expert"].

2. Create Question Types:
Include a mix of the following types of questions:
    Multiple Choice
    True/False
    Fill-in-the-Blanks
    Short Answer
    Scenario-Based (if applicable)


3. Craft the Questions
For each question:
    Clearly identify the concept or sub-topic it evaluates.
    Consider common misconceptions to design challenging options.
    Specify feedback for correct and incorrect answers.


4. Organize the Quiz
    Divide questions by sub-topic or difficulty level.
    Start with easier questions to build confidence and progressively increase difficulty.


5. Include Feedback and Self-Assessment Metrics
    For each question, provide feedback (both for correct and incorrect answers).
    After quiz completion, summarize performance:
    Display overall score.
    Highlight strengths and weaknesses by topic/sub-topic.
    Offer learning recommendations for improvement.


Example Output:
    Question 1 ( Main Topic: {Main_Topic}):
    "What is the primary characteristic of supervised learning?"
    (A) Learning from unlabeled data
    (B) Learning from labeled data
    (C) Learning through trial and error
    (D) Learning without feedback
    Correct Answer: (B)
    Feedback:
    Correct: "Supervised learning involves learning from labeled data, where the input-output relationship is defined."
    Incorrect: "Supervised learning differs from unsupervised learning, which deals with unlabeled data (A), or reinforcement learning, which uses trial and error (C)."
    
    Question 2 (Sub-Topic: {Sub_Topics}):
    "Which algorithm is typically used in clustering?"
    (A) K-Means
    (B) Linear Regression
    (C) Decision Tree
    (D) Neural Networks
    Correct Answer: (A)
    Feedback:
    Correct: "K-Means is a popular clustering algorithm in unsupervised learning."
    Incorrect: "Linear regression (B) and decision trees (C) are generally used in supervised learning tasks."

Use this structure to create quizzes for other topics or sub-topics. Add adaptive branching if needed to guide users based on their answers.


"""
