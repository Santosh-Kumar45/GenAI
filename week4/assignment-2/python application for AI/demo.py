# ============================================================
# PART 4: BUILDING PYTHON APPLICATIONS FOR AI
# ============================================================

# ------------------------------------------------------------
# Problem 23: Organize an AI application
# ------------------------------------------------------------
# Imagine you are building a simple AI chatbot.
#
# Identify what each tool would be responsible for:
#
# Streamlit
# Pandas
# NumPy
# Python functions
# LLM/API
#
# Solution:
#
# Streamlit:
# Creates the user interface.
#
# Pandas:
# Processes tables, CSV files and structured data.
#
# NumPy:
# Performs numerical calculations and array operations.
#
# Python functions:
# Organize reusable application logic.
#
# LLM/API:
# Generates or analyzes natural-language responses.

# ------------------------------------------------------------
# Problem 24: Build an AI-style function
# ------------------------------------------------------------
# Create a function called generate_answer(question).
# It should receive a question and return a response.
#
# For now, do not call an actual AI API.
# Return a simple message containing the question.
#
# Solution:
def generate_answer(question):
    return f"AI response for: {question}"


question = "What is machine learning?"

print("\nQuestion:", question)
print("Answer:", generate_answer(question))

# ------------------------------------------------------------
# Problem 25: Mini application challenge
# ------------------------------------------------------------
# Build a small Streamlit application with:
#
# 1. A title
# 2. A sidebar
# 3. A text input for a question
# 4. A button called "Ask AI"
# 5. A function that generates a placeholder answer
# 6. The answer displayed on the page
#
# Solution:
st.header("Mini AI Assistant")

st.sidebar.title("AI Assistant Settings")

model = st.sidebar.selectbox(
    "Choose model",
    ["Demo Model", "Local Model", "Cloud Model"]
)

user_question = st.text_input(
    "Ask a question",
    key="p25_question"
)


def generate_ai_response(question):
    return f"[{model}] received your question: {question}"


if st.button("Ask AI", key="p25_button"):
    if user_question:
        answer = generate_ai_response(user_question)
        st.write(answer)
    else:
        st.warning("Please enter a question first.")

