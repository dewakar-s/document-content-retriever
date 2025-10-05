from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import os
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = os.getenv("ENDPOINT_URL")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")
API_VERSION = "2025-03-01-preview"
SESSION_ID = "cli_chat_session_1"
def final_answer_llm(content,query_text):
    try:
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_ENDPOINT,
            openai_api_key=AZURE_API_KEY,
            openai_api_version=API_VERSION,
            azure_deployment=DEPLOYMENT_NAME,
            temperature=0.7,
        )
        print("✅ AzureChatOpenAI initialized successfully.")

        messages = [
            SystemMessage(content="You are a helpful AI assistant that answers questions using the provided context."),
            HumanMessage(content=content)
        ]
        
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        print(f"❌ Error initializing AzureChatOpenAI: {e}")
        print("Hint: Please check endpoint, deployment name, and API_VERSION in Azure portal.")
        exit()