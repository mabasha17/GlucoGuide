# Generative Diabetic Assistant Chatbot

A Gemini (Google Generative AI)-based chatbot for diabetes-related queries, supporting multiple Indian languages and structured conversations via Streamlit UI.

## Features

- Multi-turn Q&A with Gemini (Google Generative AI)
- Input and response in local languages (Hindi, Telugu, Tamil, etc.)
- Predefined prompts/personas (e.g., diabetes dietician)
- Export chat as a report
- (Optional) Save chat history

## Tech Stack

- **Frontend:** Streamlit
- **LLM:** Gemini (Google Generative AI)
- **Framework:** Custom (no LangChain needed for Gemini)
- **Translation:** Google Translate API or indic-trans

## Setup

1. Clone the repo
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Get a Gemini API Key:**
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Generate an API key (requires Google account)
   - Add it to a `.env` file in your project root:
     ```env
     GEMINI_API_KEY=your-key-here
     ```
4. Run the app:
   ```bash
   streamlit run app/main.py
   ```

## Usage

- Select your language
- Ask diabetes-related questions
- Download/export chat as needed
