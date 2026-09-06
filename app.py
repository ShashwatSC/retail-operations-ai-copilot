import streamlit as st
import pandas as pd
import os

from dotenv import load_dotenv
from google import genai

# ----------------------------
# configurating the basics details
# ----------------------------
MODEL_NAME = "gemini-3.6-flash"

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ----------------------------
# Stream lit web page for UI
# ----------------------------
st.set_page_config(
    page_title="RetailOps AI Copilot",
    page_icon="🏪",
    layout="wide"
)

st.title("🏪 RetailOps AI Copilot")

st.subheader("AI-Powered Decision Support for Retail Store Managers")

st.write(
    """
Upload a weekly retail operations CSV file to receive
AI-generated operational insights and recommendations.
"""
)

uploaded_file = st.file_uploader(
    "Upload Weekly Store Report (CSV)",
    type=["csv"]
)

# ----------------------------
# Process Uploaded File
# ----------------------------
if uploaded_file is not None:

    st.success("✅ File uploaded successfully!")

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Uploaded Store Data")
    st.dataframe(df, use_container_width=True)

    # Convert DataFrame into text
    store_data = ""

    for _, row in df.iterrows():
        store_data += f"{row['Metric']}: {row['Value']}\n"

    # Prompt
    prompt = f"""
You are an experienced retail operations analyst.

Analyze the following weekly retail KPI report.

Store Data:

{store_data}

Generate a professional report using the following format.

# Executive Summary

Briefly summarize overall store performance.

# Key Findings

Identify the most important operational insights.

# Operational Risks

Describe any potential concerns.

# Recommendations

Provide actionable recommendations for the store manager.

Keep the report concise and professional.
"""

    st.subheader("Retail Operations Analysis ")

    with st.spinner("🤖 Gemini is analyzing your store data..."):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            st.markdown(response.text)

        except Exception as e:

            st.warning("AI analysis is temporarily unavailable.")

            st.info("""
The uploaded retail data was processed successfully

The Google Gemini service is currently experiencing unusually high demand, so an AI-generated report could not be produced at this time.

Please wait a few minutes and click **Rerun** or refresh the page to try again.
""")

            with st.expander("Developer Error Details"):
                st.code(str(e))

                