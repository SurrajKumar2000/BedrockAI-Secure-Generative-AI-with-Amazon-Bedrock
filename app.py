import boto3
from langchain_aws import BedrockLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
from datetime import datetime

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

# Use LLMChain for prompting the LLM
chain = LLMChain(llm=llm, prompt=PROMPT)

def ask_llama3(question: str) -> str:
    # Run with model kwargs as content in `model_kwargs` dict with `body` string
    response = chain.invoke(
        question,
        model_kwargs={
            "body": {
                "max_gen_len": 512,
                "temperature": 0.5,
                "top_p": 0.9,
                # you can add more params here as needed
            }
        },
    )
    return response

def initialize_session_state():
    """Initialize session state variables for conversation history"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation_count" not in st.session_state:
        st.session_state.conversation_count = 0

def add_message(role: str, content: str):
    """Add a message to the conversation history"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": role,
        "content": content,
        "timestamp": timestamp
    })

def add_custom_animations():
    """Add custom CSS animations to the Streamlit app"""
    st.markdown("""
    <style>
    /* Global App Styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Animated Title */
    @keyframes titleGlow {
        0% { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #0073e6, 0 0 20px #0073e6; }
        50% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #0073e6, 0 0 40px #0073e6; }
        100% { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #0073e6, 0 0 20px #0073e6; }
    }
    
    .animated-title {
        animation: titleGlow 2s ease-in-out infinite alternate;
        color: white !important;
        text-align: center;
        font-size: 2.5rem !important;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    
    /* Floating Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    /* Pulse Animation */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Gradient Button Animation */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
        background-size: 300% 300%;
        animation: gradientShift 3s ease infinite;
        border: none !important;
        border-radius: 25px !important;
        color: white !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px 0 rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 8px 25px 0 rgba(0,0,0,0.3);
    }
    
    /* Animated Cards */
    @keyframes slideInLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .slide-in-left {
        animation: slideInLeft 0.6s ease-out;
    }
    
    .slide-in-right {
        animation: slideInRight 0.6s ease-out;
    }
    
    /* Chat Message Animations */
    @keyframes messageAppear {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .message-appear {
        animation: messageAppear 0.5s ease-out;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Stats Cards */
    .stats-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
    }
    
    .stats-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        background: rgba(255,255,255,0.1) !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        border-radius: 15px !important;
        color: white !important;
        backdrop-filter: blur(10px);
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #4ecdc4 !important;
        box-shadow: 0 0 0 2px rgba(78, 205, 196, 0.3) !important;
    }
    
    /* Loading Animation */
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(255,255,255,.3);
        border-radius: 50%;
        border-top-color: #fff;
        animation: spin 1s ease-in-out infinite;
    }
    
    /* Success/Error Message Styling */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 15px !important;
        backdrop-filter: blur(10px);
    }
    
    /* Metric Styling */
    .metric-container {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.05));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.2);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-container:hover {
        transform: scale(1.05);
    }
    
    /* Header Animation */
    @keyframes headerSlide {
        from { transform: translateY(-50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    .header-slide {
        animation: headerSlide 0.8s ease-out;
    }
    
    /* Chat Container Styling */
    .chat-container {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Welcome Message Animation */
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .welcome-bounce {
        animation: bounce 2s ease-in-out infinite;
    }
    </style>
    """, unsafe_allow_html=True)

def display_animated_header():
    """Display animated header with floating elements"""
    st.markdown("""
    <div class="header-slide">
        <h1 class="animated-title">🚀 Ask Anything: Chat with Llama 3 (AWS Bedrock) 🌟</h1>
        <div style="text-align: center; margin-bottom: 2rem;">
            <div class="floating" style="display: inline-block;">
                <span style="font-size: 2rem;">🤖</span>
            </div>
            <div class="pulse" style="display: inline-block; margin: 0 20px;">
                <span style="font-size: 2rem;">⚡</span>
            </div>
            <div class="floating" style="display: inline-block;">
                <span style="font-size: 2rem;">🧠</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_animated_metrics(messages_count, conversation_count):
    """Display animated metric cards"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="metric-container slide-in-left">
            <h3 style="color: white; margin: 0;">💬 Messages</h3>
            <h2 style="color: #4ecdc4; margin: 10px 0 0 0;">{messages_count}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-container slide-in-right">
            <h3 style="color: white; margin: 0;">🔄 Conversations</h3>
            <h2 style="color: #ff6b6b; margin: 10px 0 0 0;">{conversation_count}</h2>
        </div>
        """, unsafe_allow_html=True)

def display_chat_history():
    """Display the conversation history with animations"""
    if st.session_state.messages:
        st.markdown("""
        <div class="chat-container">
            <h2 style="color: white; text-align: center; margin-bottom: 20px;">💬 Conversation History</h2>
        </div>
        """, unsafe_allow_html=True)
        
        for i, message in enumerate(st.session_state.messages):
            if message["role"] == "user":
                st.markdown(f"""
                <div class="message-appear" style="background: linear-gradient(135deg, rgba(78, 205, 196, 0.2), rgba(78, 205, 196, 0.1)); 
                     backdrop-filter: blur(10px); border-radius: 15px; padding: 15px; margin: 10px 0; 
                     border-left: 4px solid #4ecdc4;">
                    <h4 style="color: #4ecdc4; margin: 0;">👤 You ({message['timestamp']})</h4>
                    <p style="color: white; margin: 10px 0 0 0;">{message['content']}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="message-appear" style="background: linear-gradient(135deg, rgba(255, 107, 107, 0.2), rgba(255, 107, 107, 0.1)); 
                     backdrop-filter: blur(10px); border-radius: 15px; padding: 15px; margin: 10px 0; 
                     border-left: 4px solid #ff6b6b;">
                    <h4 style="color: #ff6b6b; margin: 0;">🤖 Llama 3 ({message['timestamp']})</h4>
                    <p style="color: white; margin: 10px 0 0 0;">{message['content']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            if i < len(st.session_state.messages) - 1:
                st.markdown('<hr style="border: 1px solid rgba(255,255,255,0.2); margin: 20px 0;">', unsafe_allow_html=True)

def display_welcome_message():
    """Display animated welcome message"""
    st.markdown("""
    <div class="welcome-bounce" style="text-align: center; padding: 40px; 
         background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1)); 
         backdrop-filter: blur(10px); border-radius: 20px; margin: 20px 0; 
         border: 1px solid rgba(255,255,255,0.3);">
        <h2 style="color: white; margin-bottom: 20px;">👋 Welcome to the AI Chat Experience!</h2>
        <p style="color: rgba(255,255,255,0.8); font-size: 1.2rem;">
            Start a conversation by asking a question above. I'm here to help with anything you need! 🚀
        </p>
        <div style="margin-top: 20px;">
            <span style="font-size: 1.5rem; margin: 0 10px;">🌟</span>
            <span style="font-size: 1.5rem; margin: 0 10px;">✨</span>
            <span style="font-size: 1.5rem; margin: 0 10px;">💫</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def clear_history():
    """Clear the conversation history"""
    st.session_state.messages = []
    st.session_state.conversation_count = 0

def main():
    st.set_page_config(
        page_title="🚀 AI Chat Experience",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Add custom animations
    add_custom_animations()
    
    # Display animated header
    display_animated_header()
    
    # Initialize session state
    initialize_session_state()
    
    # Sidebar for conversation management
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1)); 
             backdrop-filter: blur(10px); border-radius: 15px; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.3);">
            <h2 style="color: white; margin: 0;">🎛️ Control Panel</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Display animated metrics
        display_animated_metrics(len(st.session_state.messages), st.session_state.conversation_count)
        
        # Clear history button
        if st.button("🗑️ Clear History", use_container_width=True):
            clear_history()
            st.rerun()
        
        # Export conversation button
        if st.session_state.messages:
            if st.button("📁 Export Conversation", use_container_width=True):
                # Create export text
                export_text = ""
                for msg in st.session_state.messages:
                    role = "You" if msg["role"] == "user" else "Llama 3"
                    export_text += f"{role} ({msg['timestamp']}):\n{msg['content']}\n\n"
                
                st.download_button(
                    label="📥 Download as Text",
                    data=export_text,
                    file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
    
    # Main chat interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input section
        st.markdown("""
        <div class="slide-in-left" style="background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1)); 
             backdrop-filter: blur(10px); border-radius: 15px; padding: 20px; margin-bottom: 20px; 
             border: 1px solid rgba(255,255,255,0.3);">
            <h3 style="color: white; text-align: center; margin: 0;">💭 Ask Your Question</h3>
        </div>
        """, unsafe_allow_html=True)
        
        question = st.text_area(
            "Enter your question here:",
            height=100,
            placeholder="Type your question here...",
            label_visibility="collapsed"
        )
        
        # Submit button
        col_submit, col_example = st.columns([1, 1])
        
        with col_submit:
            submit_clicked = st.button("🚀 Submit", use_container_width=True, type="primary")
        
        with col_example:
            if st.button("💡 Example Question", use_container_width=True):
                st.session_state.example_question = "Explain the concept of artificial intelligence in simple terms."
        
        # Handle example question
        if hasattr(st.session_state, 'example_question'):
            question = st.session_state.example_question
            del st.session_state.example_question
            submit_clicked = True
        
        # Process the question
        if submit_clicked:
            if question.strip() == "":
                st.warning("⚠️ Please enter a question.")
            else:
                # Add user message to history
                add_message("user", question)
                
                with st.spinner("🤔 Generating answer..."):
                    try:
                        answer = ask_llama3(question)
                        
                        # Extract the actual response text if it's a dict
                        if isinstance(answer, dict) and 'text' in answer:
                            answer_text = answer['text']
                        else:
                            answer_text = str(answer)
                        
                        # Add assistant message to history
                        add_message("assistant", answer_text)
                        st.session_state.conversation_count += 1
                        
                        # Show success message
                        st.success("✅ Answer generated successfully!")
                        
                        # Auto-scroll to the latest response by rerunning
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"❌ Error generating response: {str(e)}")
    
    with col2:
        # Quick actions
        st.markdown("""
        <div class="slide-in-right" style="background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1)); 
             backdrop-filter: blur(10px); border-radius: 15px; padding: 20px; margin-bottom: 20px; 
             border: 1px solid rgba(255,255,255,0.3);">
            <h3 style="color: white; text-align: center; margin: 0;">⚡ Quick Actions</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 New Conversation", use_container_width=True):
            clear_history()
            st.rerun()
        
        # Show some stats
        if st.session_state.messages:
            st.markdown(f"""
            <div class="stats-card">
                <h4 style="color: white; margin: 0;">📊 Session Stats</h4>
                <p style="color: rgba(255,255,255,0.8); margin: 5px 0;">Total messages: {len(st.session_state.messages)}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Show last interaction time
            if st.session_state.messages:
                last_msg = st.session_state.messages[-1]
                st.markdown(f"""
                <div class="stats-card">
                    <h4 style="color: white; margin: 0;">🕒 Last Activity</h4>
                    <p style="color: rgba(255,255,255,0.8); margin: 5px 0;">{last_msg['timestamp']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Display conversation history or welcome message
    if st.session_state.messages:
        st.markdown("---")
        display_chat_history()
    else:
        display_welcome_message()

if __name__ == "__main__":
    main()
