import streamlit as st

st.set_page_config(page_title="KAILAS Digester Simulator", layout="wide")

st.title("📊 KAILAS Mini-Digester - Real-Time Engineering Simulator")
st.subheader("Kinetic Automated Integrated Localized Anaerobic System")
st.markdown("*Developed by The Real Engineers (Sachin - Team Leader)*")

# Sidebar inputs
st.sidebar.header("🛠️ Input Operational Parameters")
waste_input = st.sidebar.slider("Daily Organic Waste Feedstock (kg)", min_value=100, max_value=2000, value=500, step=50)
electricity_tariff = st.sidebar.slider("Commercial Electricity Tariff (₹/kWh)", min_value=8, max_value=18, value=12, step=1)
manure_price = st.sidebar.slider("Bio-Manure Wholesale Price (₹/kg)", min_value=5, max_value=20, value=8, step=1)

# Engineering Formulas
daily_biogas = (waste_input / 1000.0) * 90.0 
daily_electricity = daily_biogas * 1.8 
daily_manure = waste_input * 0.25 

# Financial Matrix
logistics_savings = (waste_input / 1000.0) * 2000.0
electricity_savings = daily_electricity * electricity_tariff
manure_revenue = daily_manure * manure_price
total_daily_gross = logistics_savings + electricity_savings + manure_revenue
net_daily_profit = total_daily_gross - 472.0 
monthly_profit = net_daily_profit * 30
annual_profit = monthly_profit * 12

# Capital Investment Analysis
capex = 780000.0
payback_months = capex / monthly_profit if monthly_profit > 0 else 0

# UI Output layout
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="💨 Daily Scrubbed Biogas Yield", value=f"{daily_biogas:.2f} m³")
with col2:
    st.metric(label="⚡ Electrical Energy Generated", value=f"{daily_electricity:.2f} kWh (Units)")
with col3:
    st.metric(label="🌱 High-Grade Fertilizer Produced", value=f"{daily_manure:.2f} kg")

st.markdown("---")
st.header("💰 Financial Performance & Payback Matrix")

col4, col5, col6 = st.columns(3)
with col4:
    st.metric(label="💵 Total Daily Net Savings/Profit", value=f"₹{net_daily_profit:.2f}")
with col5:
    st.metric(label="📈 Estimated Annual Value Created", value=f"₹{annual_profit:.2f}")
with col6:
    st.metric(label="⏱️ Capital Payback Period", value=f"{payback_months:.1f} Months")

st.info("💡 Technical Insight: This system operates under a low-pressure fluid design (< 1 bar), minimizing structural fabrication costs and optimizing gas transport safety.")
