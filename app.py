import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# Streamlit page config
st.set_page_config(page_title="Smart Sprinkler System", layout="centered")

st.markdown("""
    <style>
        .sprinkler-on {color: green; font-weight: bold;}
        .sprinkler-off {color: red; font-weight: bold;}
        .footer {font-size: 12px; text-align: center; margin-top: 50px; color: gray;}
    </style>
""", unsafe_allow_html=True)

st.title("Smart Sprinkler Prediction System")
st.caption("A predictive system to automate water sprinkling using sensor data.")

with st.expander("About This App"):
    st.write("""
    This app uses a machine learning model to predict the ON/OFF status of sprinklers across 20 parcels
    based on scaled sensor data. All inputs range from 0 (low) to 1 (high).
    """)

st.subheader("Enter Scaled Sensor Values")
sensor_values = []
cols = st.columns(4)

# Display sliders in grid
for i in range(20):
    with cols[i % 4]:
        val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sensor_values.append(val)

# Predict
if st.button("🔍 Predict Sprinkler Status"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.success("Prediction Completed ✅")
    st.markdown("### 💧 Sprinkler Status Visualization:")

    grid = ""
    for i, status in enumerate(prediction):
        status_label = f"<span class='sprinkler-on'>ON</span>" if status == 1 else f"<span class='sprinkler-off'>OFF</span>"
        grid += f"• Parcel {i}: {status_label}<br>"

    st.markdown(grid, unsafe_allow_html=True)

    

# Footer
st.markdown("<div class='footer'>Developed by Kajal Singh | Aug 2025</div>", unsafe_allow_html=True)

