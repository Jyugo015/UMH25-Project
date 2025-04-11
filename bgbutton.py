import streamlit as st
import base64
import streamlit.components.v1 as components

# Function to convert image to base64 for embedding as background
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64("grabbg.png")  # Path to your background image

# Custom CSS for styling background and chat button
st.markdown(
    f"""
    <style>
    [data-testid="stApp"] {{
        background-image: url("data:image/png;base64,{bg_image}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
    }}

    header {{
        visibility: hidden;
    }}

    [data-testid="stToolbar"] {{
        display: none;
    }}

    footer {{
        visibility: hidden;
    }}
    a:link {{
        text-decoration: none;
        color: black;
    }}

    a:hover, a:active {{
        color: black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Embed Dialogflow Messenger chat component in your Streamlit app
components.html(
    """
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
    <df-messenger
        intent="WELCOME"
        chat-title="Grabot"
        agent-id="e326991e-1e77-43e9-9c9b-4aa3f25bde60"
        language-code="en"
        chat-icon="https://cdn-icons-png.flaticon.com/512/4712/4712039.png"
        style="--df-messenger-bot-message: #e6ffe6; --df-messenger-button-titlebar-color: #91e391; --df-messenger-chat-background-color: #ffffff; --df-messenger-font-color: black; --df-messenger-send-icon: #000000; position: fixed; bottom: 20px; right: 20px; z-index: 1000; width: 100%; max-width: 700px; height: 500px;"
    ></df-messenger>
    """,
    height=700,
    width=600
)
