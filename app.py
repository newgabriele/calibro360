import streamlit as st

# Pagina configuratie
st.set_page_config(
    page_title="Calibro360™ | Biogas Predictive Control",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS voor een levendig, high-tech B2B dashboard
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
    .indicator-group {
        display: flex;
        gap: 15px;
        align-items: center;
    }
    .indicator {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 0.75rem;
    }
    .led-green {
        width: 10px;
        height: 10px;
        background-color: #2e7d32;
        border-radius: 50%;
        box-shadow: 0 0 8px #2e7d32;
        animation: pulse-green 2s infinite;
    }
    .led-red {
        width: 10px;
        height: 10px;
        background-color: #c62828;
        border-radius: 50%;
        box-shadow: 0 0 8px #c62828;
        animation: pulse-red 3s infinite;
    }
    @keyframes pulse-green {
        0% { opacity: 0.4; transform: scale(0.9); }
        50% { opacity: 1; transform: scale(1.15); box-shadow: 0 0 12px #2e7d32; }
        100% { opacity: 0.4; transform: scale(0.9); }
    }
    @keyframes pulse-red {
        0% { opacity: 0.3; transform: scale(0.9); }
        50% { opacity: 0.9; transform: scale(1.1); box-shadow: 0 0 10px #c62828; }
        100% { opacity: 0.3; transform: scale(0.9); }
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
            <div class="indicator-group">
                <div class="indicator"><div class="led-green" id="sys-led"></div><span>SYS SYNC</span></div>
                <div class="indicator"><div class="led-red" id="alert-led"></div><span>DOSING TRIM</span></div>
            </div>
        </div>
        <div class="telemetry-row" id="line1">&gt; Biogas Flow Rate: <b>500 m³/h</b> | Feed-cycle synchronization: <b>Optimized</b></div>
        <div class="telemetry-row" id="line2">&gt; H₂S Inlet / Outlet: <b>380 ppm / &lt; 5 ppm</b> (Fe₂O₃ / FeO Matrix Active)</div>
        <div class="telemetry-row" id="line3">&gt; Methane Purity Vector: <b>54.6% CH₄</b> (+8.2% Efficiency Delta)</div>
    </div>

    <script>
    const payloads = [
        {
            flow: "500 m³/h", sync: "Optimized", h2sIn: "380 ppm", h2sOut: "< 5 ppm", ch4: "54.6%", alertColor: "#2e7d32", alertShadow: "0 0 8px #2e7d32"
        },
        {
            flow: "505 m³/h", sync: "Recalibrating...", h2sIn: "395 ppm", h2sOut: "< 4 ppm", ch4: "55.1%", alertColor: "#c62828", alertShadow: "0 0 8px #c62828"
        },
        {
            flow: "498 m³/h", sync: "Stable Core", h2sIn: "370 ppm", h2sOut: "< 5 ppm", ch4: "54.9%", alertColor: "#2e7d32", alertShadow: "0 0 8px #2e7d32"
        },
        {
            flow: "502 m³/h", sync: "Synchronized", h2sIn: "385 ppm", h2sOut: "< 3 ppm", ch4: "55.3%", alertColor: "#e65100", alertShadow: "0 0 8px #e65100"
        }
    ];

    let index = 0;
    setInterval(() => {
        index = (index + 1) % payloads.length;
        const p = payloads[index];
        
        const l1 = document.getElementById("line1");
        const l2 = document.getElementById("line2");
        const l3 = document.getElementById("line3");
        const alertLed = document.getElementById("alert-led");

        if(l1 && l2 && l3) {
            l1.style.opacity = 0.2;
            l2.style.opacity = 0.2;
            l3.style.opacity = 0.2;

            setTimeout(() => {
                l1.innerHTML = `&gt; Biogas Flow Rate: <b>${p.flow}</b> | Feed-cycle synchronization: <b>${p.sync}</b>`;
                l2.innerHTML = `&gt; H₂S Inlet / Outlet: <b>${p.h2sIn} / ${p.h2sOut}</b> (Fe₂O₃ / FeO Matrix Active)`;
                l3.innerHTML = `&gt; Methane Purity Vector: <b>${p.ch4} CH₄</b> (+8.2% Efficiency Delta)`;
                
                if(alertLed) {
                    alertLed.style.backgroundColor = p.alertColor;
                    alertLed.style.boxShadow = p.alertShadow;
                }

                l1.style.opacity = 1;
                l2.style.opacity = 1;
                l3.style.opacity = 1;
            }, 300);
        }
    }, 5000);
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
