import streamlit as st

# Pagina configuratie
st.set_page_config(
    page_title="Calibro360™ | Biogas Predictive Control",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS met een echte "SCADA Screen / Monitor" look
st.markdown(
    """
    <style>
    .stApp {
        background-color: #edf4f0;
        color: #212529;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #111827;
    }
    /* SCADA Monitor Scherm Look */
    .scada-monitor {
        background-color: #0d131f;
        border: 2px solid #2d3748;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15), inset 0 0 15px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
        overflow: hidden;
        font-family: 'Courier New', Courier, monospace;
    }
    .scada-header {
        background-color: #1a202c;
        padding: 8px 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #2d3748;
        font-size: 0.85rem;
        color: #a0aec0;
        letter-spacing: 1px;
    }
    .scada-dots {
        display: flex;
        gap: 6px;
    }
    .scada-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
    }
    .dot-red { background-color: #fc8181; }
    .dot-yellow { background-color: #f6ad55; }
    .dot-green { background-color: #68d391; box-shadow: 0 0 6px #68d391; }
    
    .scada-body {
        padding: 20px;
        font-size: 0.85rem;
        color: #e2e8f0;
        line-height: 1.6;
    }
    .scada-row {
        margin: 6px 0;
    }
    .highlight-green {
        color: #68d391;
        font-weight: bold;
    }
    .highlight-cyan {
        color: #63b3ed;
        font-weight: bold;
    }

    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #d4e2d8;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        color: #1f2937;
        height: 100%;
    }
    .contact-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        border-top: 1px solid #d4e2d8;
        border-right: 1px solid #d4e2d8;
        border-bottom: 1px solid #d4e2d8;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-top: 30px;
        color: #1f2937;
    }
    .btn-contact {
        display: inline-block;
        background-color: #2e7d32;
        color: white !important;
        padding: 12px 24px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: background-color 0.2s;
    }
    .btn-contact:hover {
        background-color: #235d26;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HEADER & SCADA MONITOR PANEL ---
st.title("Calibro360™")
st.subheader(
    "The New Generation - Predictive Control & Process Advisory System"
)

st.markdown(
    """
    <div class="scada-monitor">
        <div class="scada-header">
            <div class="scada-dots">
                <div class="scada-dot dot-red"></div>
                <div class="scada-dot dot-yellow"></div>
                <div class="scada-dot dot-green"></div>
            </div>
            <span style="color: #ffffff; font-weight: bold;">CALIBRO360™ // LIVE TELEMETRY & SCADA CORE</span>
            <span>STATUS: ONLINE</span>
        </div>
        <div class="scada-body">
            <div class="scada-row">&gt; Biogas Flow Rate: <span class="highlight-cyan">500.0 m³/h</span> | Feed-cycle sync: <span class="highlight-green">OPTIMIZED</span></div>
            <div class="scada-row">&gt; H₂S Inlet / Outlet: <span class="highlight-cyan">380 ppm / &lt; 5 ppm</span> (Fe₂O₃ / FeO Matrix Active)</div>
            <div class="scada-row">&gt; Methane Purity Vector: <span class="highlight-cyan">54.6% CH₄</span> (<span class="highlight-green">+8.2% Efficiency Delta</span>)</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
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

st.markdown("### Process Optimization by - Machine Learning & Continuous Data Calibrating")
st.markdown(
    """
    **Calibro360™** has completely discarded these outdated, theoretical approaches. Our tailor made platform has been built from the ground up, based on the latest 
    insights in biochemical process engineering. Calibrated with real operational data (SCADA): Our predictive control model will be calibrated. This ensures 
    that predictions regarding H₂S reduction and gas kinetics are robust, stable, and accurate in real-time.
    """
)

st.markdown("---")

# --- BENEFITS (2x2 GRID) ---
st.markdown("### Benefits")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="card">
        <h4>🎯 Precision & Stability</h4>
        <p><b>Predictive dosing of additives, no spoil.</b> Maintaining a stable process also after changes in the substrates.</p>
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

col3, col4 = st.columns(2)

with col3:
    st.markdown(
        """
        <div class="card">
        <h4>🔬 Methane Quality</h4>
        <p>Real field data demonstrates up to an <b>8% higher quality of methane</b> compared to standard, uncalibrated in situ desulfurization methods.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        """
        <div class="card">
        <h4>🔧 Lower Maintenance costs</h4> 
        <p><b>Extended oil change interval CHP.</b> Longer service life for the carbon filters.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

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

# --- FROM OPERATIONS TO THE BOARDROOM ---
st.markdown("### From operations to the boardroom")
st.markdown(
    """
    Modern operations are no longer just about "gut feeling" - they are driven by raw efficiency, strict environmental compliance, and shareholder value. 
    When operators are equipped with clear, actionable guidelines, they can run the plant safely and more comfortably, and the results naturally follow.
    """
)

st.markdown("---")

# --- CONTACT & ADVISORY ---
st.markdown("### Contact & Advisory Requests")
st.markdown(
    """
    <div class="contact-box">
    <p>For calibrated trial simulations, independent data analysis, or process control implementation, please contact:</p>
    </div>
    """,
    unsafe_allow_html=True,
)

img_col, txt_col = st.columns([1, 4])

with img_col:
    st.image("foto 063023.jpg", use_container_width=True)

with txt_col:
    st.markdown(
        """
        <div style="padding-top: 5px;">
        <p><b>Ing. Gabriele Versolato</b><br>
        <i>Biochemical Process Consultant & Lead Architect</i></p>
        <p>📩 <b>Email:</b> ing.versolato@gmail.com<br>
        📞 <b>Phone:</b> +39 346 086 4380</p>
        <a href="mailto:ing.versolato@gmail.com?subject=Inquiry%20regarding%20Calibro360™" class="btn-contact">✉ Request Information / Direct Contact</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
