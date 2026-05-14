import streamlit as st
import pandas as pd
import joblib
import io

# 1. Model Load karein
@st.cache_resource
def load_model():
    return joblib.load('banking_model.pkl')

model = load_model()

# 2. Explanation Logic Function
def explain_risk(row):
    reasons = []
    if row['Debt_to_Income_Ratio'] > 0.45:
        reasons.append(f"High Debt Ratio ({row['Debt_to_Income_Ratio']})")
    if row['Credit_Score'] < 550:
        reasons.append(f"Low Credit Score ({row['Credit_Score']})")
    if row['Savings_Balance'] < 5000:
        reasons.append("Insufficient Savings")
    if row['Missed_Payments_Last_Year'] > 0:
        reasons.append(f"{int(row['Missed_Payments_Last_Year'])} Missed Payments")
    
    return " | ".join(reasons) if reasons else "High overall risk profile"

# --- UI Setup ---
st.set_page_config(page_title="Bank Risk Analyzer", layout="wide")
st.title("🏦 Credit Risk Assessment Portal")
st.markdown("Is application ke zariye aap manually ya bulk (CSV) mein loan risk check kar sakte hain.")

tabs = st.tabs(["Individual Check (Manual)", "Bulk Analysis (CSV Upload)"])

# --- Tab 1: Manual Entry ---
with tabs[0]:
    st.subheader("Manual Customer Details")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", 18, 100, 30)
        income = st.number_input("Monthly Income", 0, 1000000, 50000)
        credit_score = st.number_input("Credit Score", 300, 850, 600)
        experience = st.number_input("Years of Experience", 0, 50, 5)
    
    with col2:
        dti = st.slider("Debt to Income Ratio", 0.0, 1.0, 0.3)
        savings = st.number_input("Savings Balance", 0, 10000000, 10000)
        missed_pmt = st.number_input("Missed Payments (Last Year)", 0, 12, 0)
        loans_count = st.number_input("Existing Loans Count", 0, 20, 1)

    # Naye features calculate karein (Training ke mutabiq)
    debt_stress = credit_score * dti
    monthly_debt = income * dti

    if st.button("Analyze Risk"):
        # Dataframe banayein (Ensure column order is same as training)
        input_data = pd.DataFrame([[age, income, credit_score, dti, experience, loans_count, savings, missed_pmt, debt_stress, monthly_debt]], 
                                 columns=['Age', 'Income_Monthly', 'Credit_Score', 'Debt_to_Income_Ratio', 'Experience_Years', 'Existing_Loans_Count', 'Savings_Balance', 'Missed_Payments_Last_Year', 'Debt_Stress_Index', 'Monthly_Debt_Amount'])
        
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.error(f"❌ Result: HIGH RISK (Probability: {prob:.2%})")
            st.warning(f"**Reason for Risk:** {explain_risk(input_data.iloc[0])}")
        else:
            st.success(f"✅ Result: SAFE (Probability: {prob:.2%})")
            st.info("Reason: Customer profile meets safety benchmarks.")

# --- Tab 2: CSV Upload ---
with tabs[1]:
    st.subheader("Bulk Assessment via CSV")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file:
        df_bulk = pd.read_csv(uploaded_file)
        
        # Auto-calculate internal features if missing
        if 'Debt_Stress_Index' not in df_bulk.columns:
            df_bulk['Debt_Stress_Index'] = df_bulk['Credit_Score'] * df_bulk['Debt_to_Income_Ratio']
        if 'Monthly_Debt_Amount' not in df_bulk.columns:
            df_bulk['Monthly_Debt_Amount'] = df_bulk['Income_Monthly'] * df_bulk['Debt_to_Income_Ratio']

        # Predictions
        # Make sure to drop non-feature columns if any (like Name or ID) before predicting
        preds = model.predict(df_bulk)
        probs = model.predict_proba(df_bulk)[:, 1]
        
        df_bulk['Risk_Prediction'] = ["High Risk" if p == 1 else "Safe" for p in preds]
        df_bulk['Risk_Probability'] = probs
        df_bulk['Explanation'] = df_bulk.apply(lambda row: explain_risk(row) if row['Risk_Prediction'] == "High Risk" else "Stable Profile", axis=1)
        
        st.write("Results Preview:", df_bulk.head())
        
        # Download button for results
        csv = df_bulk.to_csv(index=False).encode('utf-8')
        st.download_button("Download Processed Results", csv, "loan_results.csv", "text/csv")