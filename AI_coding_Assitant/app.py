import streamlit as st
import requests
import json

# Set a random background image from Unsplash
background_url = "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?..."

# Custom CSS for styling
st.markdown(
    f"""
    <style>
    /* Set the background image */
    .stApp {{
        background-image: url({background_url});
        background-size: cover;
    }}
    
    /* Change the Streamlit header (h1) color to white */
    h1 {{
        color: white !important;
    }}

    /* Change the label color to white */
    label {{
        color: white !important;
    }}

    /* Apply styles to all text within text areas to ensure black text and selection */
    textarea {{
        color: black !important;
        user-select: text !important; /* Allows text to be selected */
    }}
    
    /* Override Streamlit's disabled textarea style to make text black and selectable */
    textarea[disabled] {{
        color: black !important;
        user-select: text !important; /* Allows text to be selected */
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)

# Define API details
url = "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}
history = []

def generate_response(prompt):
    with st.spinner('Wait for it...'):
        history.append(prompt)
        final_prompt = "\n".join(history)
        data = {
            "model": "rohiths_AI_Assistant",
            "prompt": final_prompt,
            "stream": False
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response = response.text
            data = json.loads(response)
            actual_response = data['response']
            return actual_response
        else:
            return "Error: " + response.text

# Set up Streamlit interface
st.title("Rohith's AI Assistant")

user_input = st.text_area("Enter your Prompt", height=150)
if st.button("Generate"):
    output = generate_response(user_input)
    # Use a color attribute to ensure text in this box is black
    st.markdown(f'<style>.stTextArea>div>div>textarea {{color: black !important;}}</style>', unsafe_allow_html=True)
    st.text_area("Response", value=output, height=300, disabled=True)
