import os
import requests
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Calibro360™ | Biogas Process Control & Digital Twin",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS STYLING (SCADA & INDUSTRIAL THEME) ---
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #c9d1d9;
    }
    .scada-monitor {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Courier New', Courier, monospace;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .scada-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #30363d;
        padding-bottom: 8px;
        margin-bottom: 10px;
        font-size: 14px;
    }
    .scada-dots {
        display: flex;
        gap: 6px;
    }
    .scada-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    .dot-red { background-color: #ff5f56; }
    .dot-yellow { background-color: #ffbd2e; }
    .dot-green { background-color: #27c93f; }
    .scada-body {
        font-size: 13px;
        line-height: 1.6;
        color: #8b949e;
    }
    .highlight-cyan { color: #58a6ff; font-weight: bold; }
    .highlight-green { color: #3fb950; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HEADER & SCADA MONITOR PANEL WITH TOP-RIGHT IMAGE ---
col_title, col_img = st.columns([3, 1])

with col_title:
  st.title("Calibro360™")
  st.subheader(
      "The New Generation - Predictive Control & Process Advisory System"
  )

with col_img:
  st.image(
      "https://atwell.com/wp-content/uploads/2024/05/AdobeStock_552777398-scaled-1.jpeg",
      use_container_width=True,
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
            <div>&gt; Biogas Flow Rate: <span class="highlight-cyan">500.0 m³/h</span> | Feed-cycle sync: <span class="highlight-green">OPTIMIZED</span></div>
            <div>&gt; H₂S Inlet / Outlet: <span class="highlight-cyan">380 ppm / &lt; 5 ppm</span> (Fe₂O₃ / FeO Matrix Active)</div>
            <div>&gt; Methane Purity Vector: <span class="highlight-cyan">54.6% CH₄</span> (<span class="highlight-green">+8.2% Efficiency Delta</span>)</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image(
    "https://atwell.com/wp-content/uploads/2024/05/AdobeStock_552777398-scaled-1.jpeg",
    use_container_width=True,
)
st.sidebar.title("Navigation")
menu_option = st.sidebar.radio(
    "Select Module:",
    ["Dashboard & Telemetry", "Process Optimization", "About Founder"],
)

# --- MAIN CONTENT LOGIC ---
if menu_option == "Dashboard & Telemetry":
  st.markdown("### 📊 Operational Overview & CSTR Parameters")
  col1, col2, col3 = st.columns(3)
  with col1:
    st.metric(
        label="Biogas Flow Rate", value="500.0 m³/h", delta="+12.4 m³/h"
    )
  with col2:
    st.metric(label="H₂S Outlet Concentration", value="< 5 ppm", delta="-375 ppm")
  with col3:
    st.metric(label="Methane Purity", value="54.6%", delta="+1.8%")

  st.info(
      "Welcome to Calibro360™. Use the sidebar to navigate between operational"
      " modules and founder background information."
  )

elif menu_option == "Process Optimization":
  st.markdown("### ⚙️ Biochemical Process & Desulfurization Optimization")
  st.write(
      "Detailed modeling for CSTR reactors, magnetite ($Fe_3O_4$) Direct"
      " Interspecies Electron Transfer (DIET), and iron oxide complex dosing"
      " routines."
  )
  digester_temp = st.slider("Digester Temperature (°C)", 35.0, 42.0, 38.5)
  organic_load = st.slider(
      "Organic Loading Rate (kg VS / m³·d)", 2.0, 6.5, 4.2
  )
  st.success(
      f"Current simulation parameters: {digester_temp}°C at {organic_load} kg"
      " VS/m³·d are within optimal biological thresholds."
  )

elif menu_option == "About Founder":
  st.markdown("### 👨‍💻 Founder Biography")
  # Dynamically load founder info from about_founder.md
  if os.path.exists("about_founder.md"):
    with open("about_founder.md", "r", encoding="utf-8") as f:
      founder_content = f.read()
    st.markdown(founder_content)
  else:
    st.warning(
        "`about_founder.md` not found in repository root. Please ensure the"
        " file has been created and committed."
    )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #8b949e; font-size: 12px;'>© 2026"
    " Calibro360™ — Advanced Biogas Process Control & Engineering. All rights"
    " reserved.</div>",
    unsafe_allow_html=True,
)
