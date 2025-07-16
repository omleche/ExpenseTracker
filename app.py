import streamlit as st
from database import init_db, add_expense, get_expenses
from pdf_utils import generate_pdf
from translator import t
import pandas as pd

# Initialize DB
init_db()

# --- Sidebar Language Selection ---
st.session_state.lang = st.sidebar.selectbox("Select Language / Selecciona el Idioma", options=["en", "es"], index=0)
lang = st.session_state.lang

st.title("Personal Expense Tracker")
st.header(t("add_expense", lang))

# --- Expense Input Form ---
description = st.text_input(t("description", lang))
amount = st.number_input(t("amount", lang), min_value=0.0, format="%.2f")
category = st.text_input(t("category", lang))
date = st.date_input(t("date", lang))
vat_type = st.selectbox(t("vat_type", lang), ["21%", "9%", "0%"])
is_business = st.checkbox(t("business_expense", lang))

if st.button(t("submit", lang)):
    add_expense(description, amount, category, date.isoformat(), vat_type, is_business)
    st.success("Saved!")

# --- Expenses Table ---
st.header(t("expenses_list", lang))
data = get_expenses()
df = pd.DataFrame(data, columns=["ID", t("description", lang), t("amount", lang), t("category", lang), t("date", lang), t("vat_type", lang), t("business_expense", lang)])
st.dataframe(df.drop(columns=["ID"]))

# --- PDF Report Download ---
st.header(t("download_pdf", lang))

if st.button(t("download_pdf", lang)):
    # HTML template
    html_content = f"""
    <html>
    <head><style>
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid black; padding: 8px; }}
    </style></head>
    <body>
    <h1>{t('expenses_list', lang)}</h1>
    <table>
        <tr>
            <th>{t('description', lang)}</th>
            <th>{t('amount', lang)}</th>
            <th>{t('category', lang)}</th>
            <th>{t('date', lang)}</th>
            <th>{t('vat_type', lang)}</th>
            <th>{t('business_expense', lang)}</th>
        </tr>
    """
    for row in data:
        html_content += f"""
        <tr>
            <td>{row[1]}</td>
            <td>{row[2]:.2f}</td>
            <td>{row[3]}</td>
            <td>{row[4]}</td>
            <td>{row[5]}</td>
            <td>{'Yes' if row[6] else 'No'}</td>
        </tr>
        """
    html_content += "</table></body></html>"

    filename = "expense_report.pdf"
    generate_pdf(html_content, filename)
    with open(filename, "rb") as file:
        st.download_button(
            label="Download PDF",
            data=file,
            file_name=filename,
            mime="application/pdf"
        )
