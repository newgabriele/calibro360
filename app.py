import streamlit as st

# Pagina configuratie
st.set_page_config(
    page_title="Calibro360™ | Biogas Predictive Control",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS voor een frisse, professionele B2B-uitstraling
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
        color: #212529;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #111827;
    }
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        color: #1f2937;
    }
    .contact-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        border-top: 1px solid #e5e7eb;
        border-right: 1px solid #e5e7eb;
        border-bottom: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-top: 30px;
        color: #1f2937;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HEADER ---
st.title("Calibro360™")
st.subheader(
    "The Next Generation in Biogas Predictive Control & Process Advisory"
)
st.markdown("---")

# --- INTRO ---
st.markdown(
    """
    In the biogas industry, software concepts frequently emerge. While these type of systems promise substantial increases in gas production, the harsh process 
    engineering reality is that these static concepts are merely a visual shell. They rely on theoretical methane percentages (CH₄) rather than actual, corrected gas 
    volumes. Without a continuous, dynamic calculation and validated formulas under the hood, they lack any operational substance for the boardroom.
    """
)

st.markdown("### The Engine of the Future: Process Optimization by - Machine Learning & Continuous Data Calibrating")
st.markdown(
    """
    **Calibro360™** has completely discarded these outdated, theoretical approaches. Our tailor made platform has been built from the ground up, based on the latest 
    insights in biochemical process engineering. Calibrated with real operational data (SCADA): Our predictive control model will be calibrated. This ensures 
    that predictions regarding H₂S reduction and gas kinetics are robust, stable, and accurate in real-time.
    """
)

st.markdown("---")

# --- BENEFITS ---
st.markdown("### Benefits")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="card">
        <h4>🎯 Precision & Stability</h4>
        <p><b>Exact dosing of additives, no spoil.</b> A stable process also after changes in the substrates.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
        <h4>📈 Maximum Yield</h4>
        <p><b>Demonstrates up to 20% higher volume of biogas.</b> From static monitoring to a dynamic, predictive feed-cycle synchronization.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="card">
    <h4>🔬 Methane Quality</h4>
    <p>Real field data demonstrates up to an <b>8% higher quality of methane</b> compared to standard, uncalibrated in situ desulfurization methods.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- BRAND INDEPENDENT ---
st.markdown("### 100% Brand-Independent")
st.markdown(
    """
    Every type of desulfurization additive on the market whether the different types, of iron oxide, iron hydroxide, or specific chemical blends from any manufacturer can 
    be inputted based on its exact chemical specifications to model the biological impact.
    
    *For major waste haulers and plant owners, this mass reduction yields a financial saving that often exceeds the value of the extra biomethane produced.*
    """
)

st.markdown("---")

# --- CONTACT & ADVISORY ---
st.markdown(
    """
    <div class="contact-box">
    <h3>Contact & Advisory Requests</h3>
    <p>For calibrated trial simulations, independent data analysis, or process control implementation, please contact:</p>
    <p><b>Ing. Gabriele Versolato</b><br>
    <i>Biochemical Process Consultant & Lead Architect</i></p>
    <p>📩 <b>Email:</b> ing.versolato@gmail.com<br>
    📞 <b>Phone:</b> +39 346 086 4380</p>
    </div>
    """,
    unsafe_allow_html=True,
)
