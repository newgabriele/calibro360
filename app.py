import streamlit as st

# Pagina configuratie
st.set_page_config(
    page_title="Calibro360™ | Biogas Predictive Control",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS voor een levendig, dynamisch B2B dashboard
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
    .telemetry-container {
        background-color: #ffffff;
        border: 1px solid #d4e2d8;
        border-radius: 10px;
        padding: 20px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.85rem;
        color: #1f2937;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.03);
    }
    .telemetry-title {
        font-weight: bold;
        color: #1b5e20;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .telemetry-row {
        margin: 6px 0;
        transition: opacity 0.3s ease;
    }
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #d4e2d8;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        color: #1f2937;
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

# --- HEADER & LIVE DYNAMIC TELEMETRY PANEL ---
st.title("Calibro360™")
st.subheader(
    "The Next Generation in Biogas Predictive Control & Process Advisory"
)

st.markdown(
    """
    <div class="telemetry-container">
        <div class="telemetry-title">
            <span>⚙️ LIVE SCADA & KINEMATICS TELEMETRY STREAM</span>
            <span id="status-badge" style="color: #2e7d32; font-weight: bold;">● SYSTEM OPTIMIZED</span>
        </div>
        <div class="telemetry-row" id="line1">&gt; Biogas Flow Rate: <b id="val-flow">500.0 m³/h</b> | Feed-cycle sync: <span id="val-sync" style="color: #2e7d32; font-weight: bold;">OPTIMIZED</span></div>
        <div class="telemetry-row" id="line2">&gt; H₂S Inlet / Outlet: <b id="val-h2s">380 ppm / &lt; 5 ppm</b> (Fe₂O₃ / FeO Matrix Active)</div>
        <div class="telemetry-row" id="line3">&gt; Methane Purity Vector: <b id="val-ch4">54.6% CH₄</b> (<span id="val-delta" style="color: #2e7d32; font-weight: bold;">+8.2% Efficiency Delta</span>)</div>
    </div>

    <script>
    function updateTelemetry() {
        // Genereer dynamische variatie rond de 500 m³/h
        const flowVal = (495 + Math.random() * 10).toFixed(1);
        const h2sInVal = Math.floor(375 + Math.random() * 25);
        const h2sOutVal = Math.floor(3 + Math.random() * 3);
        const ch4Val = (54.0 + Math.random() * 1.5).toFixed(1);

        // Lijst met statussen en hun bijbehorende kleuren (groen, oranje, rood)
        const states = [
            { text: "OPTIMIZED", color: "#2e7d32" },      // Groen
            { text: "RECALIBRATING", color: "#e65100" }, // Oranje
            { text: "PEAK STABLE", color: "#2e7d32" },   // Groen
            { text: "HIGH LOAD TRIM", color: "#c62828" } // Rood
        ];

        const deltas = [
            { text: "+8.2% Efficiency Delta", color: "#2e7d32" },
            { text: "+7.6% Efficiency Delta", color: "#e65100" },
            { text: "+8.5% Efficiency Delta", color: "#2e7d32" },
            { text: "+5.9% Efficiency Delta", color: "#c62828" }
        ];

        const randomState = states[Math.floor(Math.random() * states.length)];
        const randomDelta = deltas[Math.floor(Math.random() * deltas.length)];

        // Update de DOM elementen vloeiend
        document.getElementById("val-flow").innerText = flowVal + " m³/h";
        document.getElementById("val-h2s").innerText = h2sInVal + " ppm / < " + h2sOutVal + " ppm";
        document.getElementById("val-ch4").innerText = ch4Val + "% CH₄";

        const syncEl = document.getElementById("val-sync");
        syncEl.innerText = randomState.text;
        syncEl.style.color = randomState.color;

        const deltaEl = document.getElementById("val-delta");
        deltaEl.innerText = randomDelta.text;
        deltaEl.style.color = randomDelta.color;

        const badgeEl = document.getElementById("status-badge");
        badgeEl.innerText = "● SYSTEM " + randomState.text;
        badgeEl.style.color = randomState.color;
    }

    // Elke 4 seconden verversen
    setInterval(updateTelemetry, 4000);
    </script>
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
