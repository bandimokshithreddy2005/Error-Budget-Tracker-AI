import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Error Budget Tracker AI")

genai.configure(api_key="YOUR_API_KEY")

st.title("🚨 Error Budget Tracker with AI")

uploaded_file = st.file_uploader("Upload Logs CSV", type=["csv"])

# =========================
# AI FUNCTION
# =========================
def generate_ai_report(success_rate, error_rate, burn_rate, top_service, remaining_budget):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Generate a professional SRE Weekly Error Budget Report.

    Success Rate: {success_rate:.2f}%
    Error Rate: {error_rate:.2f}%
    Burn Rate: {burn_rate:.2f}
    Top Failure Service: {top_service}
    Remaining Budget: {remaining_budget:.2f}%

    Format:
    - Summary
    - Risk Level
    - Recommendation
    """

    response = model.generate_content(prompt)
    return response.text


# =========================
# MAIN APP
# =========================
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # =========================
    # RAW DATA (STATUS TEXT COLOR ONLY)
    # =========================
    st.subheader("📄 Sample Data")

    def color_status(val):
        if str(val).strip().lower() == "success":
            return "color: green; font-weight: bold;"
        elif str(val).strip().lower() == "failed":
            return "color: red; font-weight: bold;"
        return ""

    styled_df = df.style.map(color_status, subset=["status"])

    st.dataframe(
        styled_df,
        width="stretch"
    )
    # =========================
    # FILTER
    # =========================
    st.subheader("🔍 Filter Data")

    services = ["All"] + sorted(df["service"].unique().tolist())

    selected_service = st.selectbox(
        "Select Service",
        services
    )

    if selected_service != "All":
        filtered_df = df[df["service"] == selected_service]
    else:
        filtered_df = df.copy()
    # =========================
    # Metrics Calculation
    # =========================
    total = len(filtered_df)

    success = len(filtered_df[filtered_df["status"] == "Success"])
    failed = len(filtered_df[filtered_df["status"] == "Failed"])

    # Success & Error Rate
    success_rate = (success / total) * 100 if total > 0 else 0
    error_rate = (failed / total) * 100 if total > 0 else 0

    # SLO = 99% (Allowed Error Budget = 1%)
    allowed_error_budget = 1.0

    # Budget Used
    budget_used = min((error_rate / allowed_error_budget) * 100, 100)

    # Remaining Budget
    remaining_budget = max(0, 100 - budget_used)

    # Burn Rate
    burn_rate = error_rate / allowed_error_budget

    failed_df = filtered_df[filtered_df["status"] == "Failed"]

    if not failed_df.empty:
        top_service = failed_df["service"].value_counts().idxmax()
    else:
        top_service = "No failures"



    # =========================
    # METRICS UI (CARD STYLE FIX)
    # =========================
    # =========================
    # METRICS UI
    # =========================
    st.subheader("📊 Metrics Dashboard")


    def card(title, value):
        st.markdown(f"""
        <div style="
            background-color: white;
            border: 2px solid black;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        ">
            <h4 style="color:black;">{title}</h4>
            <h2 style="color:black;">{value}</h2>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        card("Total Requests", total)

    with col2:
        card("Success Rate (%)", f"{success_rate:.1f}%")

    with col3:
        card("Failure Rate (%)", f"{error_rate:.1f}%")

    with col4:
        card("Budget Used (%)", f"{budget_used:.1f}%")
    # =========================
    # VISUALS
    # =========================
   # =========================
# VISUALS
# =========================
    st.subheader("📊 Visual Insights")

    graph_col1, graph_col2 = st.columns([1, 1])

    # Pie Chart
    with graph_col1:
        success = len(filtered_df[filtered_df["status"] == "Success"])
        failed = len(filtered_df[filtered_df["status"] == "Failed"])

        fig1, ax1 = plt.subplots(figsize=(6, 6))

        ax1.pie(
            [success, failed],
            labels=["Success", "Failed"],
            autopct="%1.1f%%",
            colors=["#003366", "#66B2FF"],
            textprops={"fontsize": 10}
        )

        ax1.set_title("Success vs Failure", fontsize=12)

        fig1.tight_layout()
        st.pyplot(fig1, width="stretch")
    # Bar Chart
    with graph_col2:
        service_status = (
            filtered_df.groupby(["service", "status"])
            .size()
            .unstack(fill_value=0)
        )

        service_status = service_status.reindex(
            columns=["Success", "Failed"],
            fill_value=0
        )

        fig2, ax2 = plt.subplots(figsize=(8, 6))

        service_status.plot(
            kind="bar",
            ax=ax2,
            color=["#003366", "#66B2FF"]
        )

        ax2.set_title("Success vs Failed by Service", fontsize=12)
        ax2.set_xlabel("Service")
        ax2.set_ylabel("Count")
        ax2.legend(title="Status")

        fig2.tight_layout()
        st.pyplot(fig2, width="stretch")

    # =========================
    # BUDGET UTILIZATION TREND (SERVICE WISE)
    # =========================
    st.subheader("📈 Budget Utilization Trend (Service Wise)")

    # Group by service
    service_trend = filtered_df.groupby("service").agg(
        total_requests=("status", "count"),
        failures=("status", lambda x: (x == "Failed").sum())
    ).reset_index()

    # Success & failure %
    service_trend["Success_Percentage"] = (
        (service_trend["total_requests"] - service_trend["failures"])
        / service_trend["total_requests"]
    ) * 100

    service_trend["Failure_Percentage"] = (
        service_trend["failures"] / service_trend["total_requests"]
    ) * 100

    # Budget Used %
    allowed_error_budget = 1.0

    service_trend["Budget_Used"] = (
        service_trend["Failure_Percentage"] / allowed_error_budget
    ) * 100

    # Plot
    fig3, ax3 = plt.subplots(figsize=(10, 5))

    # ONLY Budget Used % line (blue)
    ax3.plot(
        service_trend["service"],
        service_trend["Budget_Used"],
        marker="o",
        label="Budget Used %",
        color="blue"
    )

    ax3.set_title("Budget Utilization Trend by Service")
    ax3.set_xlabel("Services")
    ax3.set_ylabel("Percentage")
    ax3.legend()
    ax3.tick_params(axis='x', rotation=45)

    st.pyplot(fig3)
    # =========================
    # AI REPORT
    # =========================
    st.subheader("🧠 AI SRE Report")

    if st.button("Generate AI Report"):
        report = generate_ai_report(
            success_rate,
            error_rate,
            burn_rate,
            top_service,
            remaining_budget
        )

        st.success("AI Report Generated ✅")
        st.write(report)

    # =========================
    # STATUS
    # =========================

    st.write("Error Rate:", f"{error_rate:.2f}%")
    st.write("Burn Rate:", f"{burn_rate:.2f}")

    if burn_rate <= 1:
        st.success("System Healthy ✅")
    elif burn_rate <= 2:
        st.warning("Warning ⚠️ Burn rate increasing")
    else:
        st.error("Critical 🚨 Error budget burning fast")