import boto3
from langchain_aws import BedrockLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st


# Initialize boto3 client for AWS Bedrock
bedrock_client = boto3.client("bedrock-runtime")

# Construct the LLM model
llm = BedrockLLM(
    client=bedrock_client,
    model_id="meta.llama3-70b-instruct-v1:0",
  
)


# Define the prompt with LangChain PromptTemplate
prompt_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>


You are a very intelligent bot with exceptional critical thinking.


<|start_header_id|>user<|end_header_id|>


{question}


<|start_header_id|>assistant<|end_header_id|>
"""


PROMPT = PromptTemplate(template=prompt_template, input_variables=["question"])


# Using LLMChain for prompting the LLM
chain = LLMChain(llm=llm, prompt=PROMPT)


def ask_llama3(question: str) -> str:
  
    response = chain.invoke(
        question,
        model_kwargs={
            "body": {
                "max_gen_len": 512,
                "temperature": 0.5,
                "top_p": 0.9,
            }
        },
    )
    return response


def main():
    st.title("Ask Anything: Chat with Llama 3 (AWS Bedrock) 🌟")

    question = st.text_area("Enter your question here:")

    if st.button("Submit"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating answer..."):
                answer = ask_llama3(question)
                st.subheader("Answer:")
                st.write(answer)


if __name__ == "__main__":
    main()
