import boto3
import json

prompt_data = """
Act as a Shakespeare and write a poem on Generative AI
"""

bedrock = boto3.client(service_name="bedrock-runtime")

# Updated prompt format for Llama 3
payload = {
    "prompt": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{prompt_data}<|end_header_id|>\n\n<|start_header_id|>assistant<|end_header_id|>\n\n",
    "max_gen_len": 512,
    "temperature": 0.5,
    "top_p": 0.9
}

body = json.dumps(payload)

# Updated model ID for Llama 3
model_id = "meta.llama3-70b-instruct-v1:0"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
response_text = response_body['generation']
print(response_text)