import streamlit as st
import lightkurve as lk
import matplotlib.pyplot as plt
import pandas as pd
import io

# Set page configuration
st.set_page_config(
    page_title="Light Curve Explorer",
    page_icon="⭐",
    layout="centered"
)

# Add a title and description
st.title("⭐ Light Curve Explorer")
st.markdown("""
This app allows you to explore light curves from various space missions including:
- Kepler Mission
- TESS Mission
- K2 Mission
- KELT Survey
- UKIRT Survey

Enter a star name (e.g., 'Kepler-10', 'TOI-700', 'EPIC 201367065', 'KELT-9', or 'WASP-12') to fetch and visualize its light curve data.
""")

# Create a text input for the star name
star_name = st.text_input("Enter a star name:", "Kepler-10")

# Function to fetch and process light curve data
def fetch_light_curve(target_name):
    try:
        # Search for the target
        search_result = lk.search_lightcurve(target_name)
        
        if len(search_result) == 0:
            st.error(f"No light curve data found for {target_name}")
            st.info("""
            Tips for searching:
            - Kepler stars: Use 'Kepler-XXX' or 'KIC XXXXXXXX'
            - TESS stars: Use 'TOI-XXX'
            - K2 stars: Use 'EPIC XXXXXXXXX'
            - KELT stars: Use 'KELT-XX'
            - UKIRT/WASP stars: Use 'WASP-XX'
            """)
            return None
        
        # Download the first light curve
        lc = search_result[0].download()
        return lc
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Create a button to fetch data
if st.button("Fetch Light Curve"):
    with st.spinner("Fetching light curve data..."):
        light_curve = fetch_light_curve(star_name)
        
        if light_curve is not None:
            # Create a figure for the light curve
            fig, ax = plt.subplots(figsize=(10, 4))
            light_curve.plot(ax=ax)
            ax.set_title(f"Light Curve for {star_name}")
            ax.set_xlabel("Time (days)")
            ax.set_ylabel("Flux")
            st.pyplot(fig)
            
            # Convert light curve to DataFrame and display first 20 rows
            df = pd.DataFrame({
                'Time': light_curve.time.value,
                'Flux': light_curve.flux.value,
                'Flux Error': light_curve.flux_err.value
            })           
            # Create a download button for the CSV file
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download light curve as CSV",
                data=csv,
                file_name=f"{star_name}_light_curve.csv",
                mime="text/csv"
            ) 
