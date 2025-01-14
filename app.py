import streamlit as st
import pandas as pd

# Data
data = [
    ["2023", "Jordan", "B2B, B2C, B2G e-Invoicing"],
    ["2023", "Egypt", "Mandatory e-Invoicing (fully implemented in April)"],
    ["2023", "Japan", "Qualified Invoice System (October)"],
    ["2024", "Romania", "e-Book Keeping Phase 1"],
    ["2024", "Denmark", "e-Transport Obligation"],
    ["2024", "Malaysia", "B2B, B2C, B2G e-Invoicing Phase 1"],
    ["2024", "China", "Mandatory e-Fapiao Rollout"],
    ["2025", "France", "B2B & B2G e-Invoicing Pilot Program"],
    ["2025", "Ukraine", "SAF-T for Large Taxpayers"],
    ["2025", "Romania", "SAF-T All Taxpayers"],
    ["2025", "Germany", "B2B e-Invoicing"],
    ["2025", "Malaysia", "B2B, B2C, B2G e-Invoicing Phase 2"],
    ["2025", "Hungary", "B2B e-Invoicing (Energy Sector)"],
    ["2025", "Denmark", "e-Book Keeping Phase 2"],
    ["2026", "Oman", "B2B e-Invoicing"],
    ["2026", "Spain", "Verifactu Reporting Phase 2"],
    ["2026", "Latvia", "SAF-T Major Changes"],
    ["2026", "Belgium", "SAF-T"],
    ["2026", "Croatia", "SAF-T"],
    ["2026", "Bulgaria", "SAF-T"],
    ["2026", "Denmark", "e-Book Keeping Phase 3"],
    ["2026", "Poland", "B2B e-Invoicing"],
    ["2026", "Slovenia", "B2B e-Invoicing"],
    ["2027", "UAE", "B2B, B2C, B2G e-Invoicing"],
    ["2027", "France", "B2B & B2G e-Invoicing"],
    ["2028-2030", "Portugal", "SAF-T"],
    ["2028-2030", "Slovakia", "B2B e-Invoicing"],
]

# Convert data to DataFrame
df = pd.DataFrame(data, columns=["Year", "Country", "Regulation"])

# Streamlit app
st.title("Global Overview of e-Invoicing & e-Reporting Regulations")

# Filters
st.sidebar.header("Filters")
selected_year = st.sidebar.multiselect("Select Year", options=df["Year"].unique(), default=df["Year"].unique())
selected_country = st.sidebar.multiselect("Select Country", options=df["Country"].unique(), default=df["Country"].unique())

# Filter data based on user input
filtered_data = df[(df["Year"].isin(selected_year)) & (df["Country"].isin(selected_country))]

# Display the filtered data
st.write("### Filtered Data")
st.dataframe(filtered_data)

# Download option for filtered data
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_data.to_csv(index=False),
    file_name="filtered_e_invoicing_data.csv",
    mime="text/csv"
)

# Display a summary of regulations by year
st.write("### Regulations Count by Year")
regulations_by_year = filtered_data["Year"].value_counts().reset_index()
regulations_by_year.columns = ["Year", "Regulation Count"]
st.bar_chart(regulations_by_year.set_index("Year"))