import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set up the language model
llm = OpenAI(api_key=openai_api_key)

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Q: {question}\nA:",
)

# Create a chain using the | operator
chain = prompt_template | llm | StrOutputParser()

# Ask a question
question = "What is LangChain?"
response = chain.invoke({"question": question})

# Print the response
print(response)