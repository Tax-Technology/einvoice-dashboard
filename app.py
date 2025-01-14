import streamlit as st
import pandas as pd

# ---------------------------
# 1) Data Preparation
# ---------------------------
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

# ---------------------------
# 2) Streamlit App Title
# ---------------------------
st.title("Global Overview of e-Invoicing & e-Reporting Regulations - Timeline")

# ---------------------------
# 3) Year Filter (Optional)
# ---------------------------
all_years = sorted(df["Year"].unique())
selected_years = st.multiselect("Filter by Year(s)", options=all_years, default=all_years)

# If nothing is selected, display everything
if selected_years:
    df = df[df["Year"].isin(selected_years)]

# ---------------------------
# 4) Custom CSS for Timeline
# ---------------------------
st.markdown(
    """
    <style>
    /* Timeline container */
    .timeline {
        position: relative;
        max-width: 800px;
        margin: 0 auto;
    }

    /* The vertical line */
    .timeline::after {
        content: '';
        position: absolute;
        width: 6px;
        background-color: #d4d4d4;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -3px;
    }

    /* Containers for the timeline items */
    .timeline-container {
        padding: 10px 40px;
        position: relative;
        background-color: inherit;
        width: 50%;
    }

    /* Place the container to the left or right of the timeline */
    .timeline-container.left {
        left: 0;
    }
    .timeline-container.right {
        left: 50%;
    }

    /* Create the circles on the timeline */
    .timeline-container::after {
        content: '';
        position: absolute;
        width: 25px;
        height: 25px;
        right: -17px;
        background-color: white;
        border: 4px solid #f77676;
        top: 15px;
        border-radius: 50%;
        z-index: 1;
    }

    /* Position the circle on the other side */
    .timeline-container.right::after {
        left: -17px;
    }

    /* Card-like container for content */
    .timeline-content {
        padding: 20px;
        background-color: #f9f9f9;
        position: relative;
        border-radius: 6px;
    }

    .timeline-content h3 {
        margin: 0;
        font-size: 18px;
        font-weight: bold;
    }

    .timeline-content p {
        margin: 5px 0 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# 5) Build the Timeline HTML
# ---------------------------
html_content = '<div class="timeline">'
for i, row in df.iterrows():
    side = "left" if i % 2 == 0 else "right"
    html_content += f"""
    <div class="timeline-container {side}">
        <div class="timeline-content">
            <h3>{row['Year']} - {row['Country']}</h3>
            <p>{row['Regulation']}</p>
        </div>
    </div>
    """
html_content += "</div>"

# ---------------------------
# 6) Render the Timeline
# ---------------------------
st.markdown(html_content, unsafe_allow_html=True)