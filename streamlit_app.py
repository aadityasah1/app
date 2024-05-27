import requests

# Replace with your actual Hugging Face API key
hf_api_key = "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"
hf_api_url = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {hf_api_key}"}

def generate_text(prompt):
    response = requests.post(hf_api_url, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Something went wrong. Check your API key and input."}

# Test the function
print(generate_text("Once upon a time"))
import streamlit as st

def main():
    st.title("Generative AI Application")
    user_input = st.text_input("Enter your text:")
    if st.button("Generate"):
        result = generate_text(user_input)
        st.write(result)

if __name__ == "__main__":
    main()
