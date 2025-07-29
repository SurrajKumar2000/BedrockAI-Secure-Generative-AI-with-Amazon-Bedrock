# Ask Anything: Chat with Llama 3 (AWS Bedrock) ⭐

A modern, interactive chat application powered by Meta's Llama 3 model through AWS Bedrock, built with Streamlit for a seamless user experience.

## 🚀 Features

- **Llama 3 Integration**: Leverage the power of Meta's latest language model via AWS Bedrock
- **Real-time Chat Interface**: Clean, responsive UI built with Streamlit
- **AWS Bedrock Backend**: Enterprise-grade AI service with high availability
- **Simple Deployment**: Easy setup and deployment process
- **Scalable Architecture**: Built on AWS infrastructure for reliability

📸 Screenshots
🏠 Main Interface
<img width="1700" height="743" alt="AWS-Bedrock Output-1" src="https://github.com/user-attachments/assets/ee4a5257-c5da-4aa2-8e57-3c9ce887ca6e" />
Clean and intuitive chat interface with question input area

💬 Chat Interaction
Show Image
Example conversation showing Llama 3 responses

✨ Sample Output
Show Image
Demonstration of AI-generated responses and formatting




## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Meta Llama 3 (via AWS Bedrock)
- **Backend**: LangChain + AWS Bedrock
- **Cloud Platform**: AWS
- **Language**: Python

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.3 or higher
- AWS account with Bedrock access
- AWS CLI configured with appropriate credentials
- Access to Llama 3 model in AWS Bedrock (request access if needed)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/llama3-bedrock-chat.git
   cd llama3-bedrock-chat
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS credentials**
   ```bash
   aws configure
   ```
   Or set environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=us-east-1
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the interface**
   - Open your browser and navigate to `http://localhost:8501`
   - Enter your question in the text area
   - Click "Submit" to get responses from Llama 3

## ⚙️ Configuration

### AWS Bedrock Setup

1. **Enable Bedrock in your AWS account**
   - Navigate to AWS Bedrock console
   - Request access to Llama 3 model if not already available

2. **Set up IAM permissions**
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "bedrock:InvokeModel",
           "bedrock:ListFoundationModels"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

### Environment Variables

Create a `.env` file in the root directory:

```env
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=meta.llama3-70b-instruct-v1:0
STREAMLIT_SERVER_PORT=8501
```

## 🔍 Model Configuration

The application uses Meta's Llama 3 model through AWS Bedrock. You can customize model parameters:

- **Temperature**: Controls randomness (0.1 - 1.0)
- **Max Tokens**: Maximum response length
- **Top P**: Nucleus sampling parameter

## 📊 Performance

- **Response Time**: Typically 2-5 seconds depending on query complexity
- **Concurrent Users**: Supports multiple simultaneous conversations
- **Availability**: 99.9% uptime through AWS Bedrock SLA

## 🐛 Troubleshooting

### Common Issues

1. **AWS Credentials Error**
   ```
   Solution: Ensure AWS CLI is configured or environment variables are set
   ```

2. **Model Access Denied**
   ```
   Solution: Request access to Llama 3 in AWS Bedrock console
   ```

3. **Streamlit Port Conflict**
   ```bash
   streamlit run app.py --server.port 8502
   ```

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```


## 🙏 Acknowledgments

- Meta AI for the Llama 3 model
- AWS for Bedrock infrastructure
- Streamlit team for the amazing framework
- LangChain for seamless AI integration
