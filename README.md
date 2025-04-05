# Kepler Light Curve Explorer

A Streamlit application that allows users to explore light curves from various space missions including Kepler, TESS, K2, and more.

## Features

- Search for light curves by star name
- Visualize light curves using matplotlib
- View the first 20 rows of the dataset
- Download light curve data as CSV
- Error handling for invalid star names
- Loading spinner during data fetch

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser. Enter a star name (e.g., "Kepler-10") and click "Fetch Light Curve" to view its data.

## Example Star Names

### Kepler Mission Stars
- Kepler-10 (First rocky exoplanet discovered)
- Kepler-11 (System with 6 planets)
- Kepler-22 (First confirmed habitable zone planet)
- Kepler-186 (First Earth-sized planet in habitable zone)
- Kepler-452 (Earth's "cousin" planet)
- Kepler-438 (Super-Earth in habitable zone)
- Kepler-442 (Potentially habitable planet)
- Kepler-62 (System with 5 planets)
- Kepler-444 (Ancient system with 5 planets)
- Kepler-90 (System with 8 planets)

### Other Interesting Kepler Stars
- KIC 8462852 (Tabby's Star, famous for unusual dimming)
- Kepler-444 (One of the oldest known planetary systems)
- Kepler-16 (First confirmed circumbinary planet)
- Kepler-47 (First multi-planet circumbinary system)
- Kepler-64 (Quadruple star system with planet)

### TESS Mission Stars
- TOI-700 (First Earth-sized planet in habitable zone)
- TOI-1338 (First circumbinary planet discovered by TESS)
- TOI-1690 (System with multiple planets)
- TOI-270 (System with three small planets)
- TOI-849 (First exposed planetary core discovered)

### K2 Mission Stars
- EPIC 201367065 (System with three super-Earths)
- EPIC 201912552 (System with multiple planets)
- EPIC 211945201 (System with six planets)
- EPIC 246393474 (System with multiple planets)
- EPIC 201505350 (System with multiple planets)

### KELT Survey Stars
- KELT-9 (Hottest known exoplanet host)
- KELT-11 (Bright star with transiting planet)
- KELT-16 (Hot Jupiter with short orbital period)
- KELT-20 (Hot Jupiter with inflated atmosphere)
- KELT-24 (Hot Jupiter with high metallicity)

### UKIRT Survey Stars
- WASP-12 (Hot Jupiter with extreme atmosphere)
- WASP-33 (First planet discovered around a Delta Scuti star)
- WASP-43 (Hot Jupiter with well-characterized atmosphere)
- WASP-76 (Ultra-hot Jupiter with iron rain)
- WASP-121 (Hot Jupiter with stratosphere)

Note: Some stars might have multiple light curves available from different quarters of their respective missions. The app supports searching across multiple missions, but availability may vary. 