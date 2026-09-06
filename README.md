# 🏪 RetailOps AI Copilot

RetailOps AI Copilot is an AI-powered decision support system designed to help retail store managers analyze weekly operational KPI reports. The application accepts a CSV file containing store performance metrics and generates an AI-based operations report with key findings and recommendations.

This project was developed as the runnable baseline for the CSE 598 Capstone Project.

---

## Features

- Upload retail KPI data as a CSV file
- Display uploaded store metrics
- Generate an AI-powered retail operations analysis using Google Gemini
- Gracefully handles temporary AI service outages

---

## Technologies

- Python 3.13
- Streamlit
- Pandas
- Google Gemini API
- python-dotenv

---

## Project Structure

```
retail-operations-ai-copilot/

│── app.py
│── requirements.txt
│── README.md
│── .env.example

├── examples/
│     sample_store_data.csv

├── output/

└── screenshots/
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/ShashwatSC/retail-operations-ai-copilot.git

cd retail-operations-ai-copilot
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## API Key

Create a `.env` file in the project root.

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

API keys can be created from:

https://aistudio.google.com/

---

## Running the Application

```bash
streamlit run app.py
```

---

## Sample Test Case

The repository includes:

```
examples/sample_store_data.csv
```

Upload this file after launching the application.

Expected behavior:

- Store data is displayed
- Gemini generates an operations report
- If Gemini is temporarily unavailable, the application displays a user-friendly message instead of crashing.

---

## Future Improvements

- Multi-agent retail analysis
- Sales Agent
- Inventory Agent
- Labor Agent
- Customer Experience Agent
- KPI trend visualization
- Dashboard analytics
- Retrieval-Augmented Generation (RAG)

---

## Author

Shashwat Chauhan 1237282932

CSE 598 Capstone Project