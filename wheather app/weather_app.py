import streamlit as st
import requests

# --- Configuration ---
API_KEY = "01417b4cac694bfe9ae115124251005" 

# Set Streamlit page configuration to match HTML title and favicon, and layout
st.set_page_config(
    page_title="Weather App", # Matches <title>Weather App</title>
    page_icon="☀️",          # Placeholder for favicon. You can use an emoji or a path to an accessible image.
    layout="centered",       # Centers the main content block
    # initial_sidebar_state="collapsed" # Optional: Hide the default sidebar menu if present
)

# --- Custom CSS for Styling (Directly translated from style.css) ---
st.markdown("""
<style>
/* Hide the Streamlit header and footer */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; } /* Hides the top-right Streamlit header/deploy button */

/* RESET DEFAULT SPACES (from style.css) */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* BODY STYLES (Applied to Streamlit's main content area - .stApp is Streamlit's body) */
.stApp {
    background: linear-gradient(to right, #00c6ff, #0072ff, #fceabb); /* From style.css body */
    font-family: 'Poppins', sans-serif; /* From style.css body */
    color: white; /* From style.css body */
    display: flex; /* From style.css body */
    justify-content: center; /* From style.css body */
    align-items: center; /* From style.css body */
    min-height: 100vh; /* Use min-height to ensure it covers viewport and expands if content is long */
    width: 100%; /* Ensure it takes full width */
    overflow: auto; /* Allow scrolling if content overflows */
}

/* CONTAINER STYLES (Mapped from #container in style.css to Streamlit's .block-container) */
.block-container {
    /* Remove Streamlit's default padding to prevent it from affecting our custom container padding */
    padding-top: 0rem; 
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;

    width: 90% !important; /* From style.css #container */
    max-width: 500px !important; /* From style.css #container */
    margin: auto; /* From style.css #container - helps center block horizontally */
    background: rgba(0, 0, 0, 0.4); /* From style.css #container */
    padding: 40px 30px; /* From style.css #container */
    border-radius: 15px; /* From style.css #container */
    box-shadow: 0px 4px 30px rgba(0, 0, 0, 0.3); /* From style.css #container */
    backdrop-filter: blur(5px); /* From style.css #container */
    border: 1px solid rgba(255, 255, 255, 0.2); /* From style.css #container */
    text-align: center; /* From style.css #container */
    position: relative; /* Added for z-index if needed later */
    z-index: 1; /* Added for z-index if needed later */
}


/* Heading styles (from style.css h1, mapped to Streamlit's h1 output by st.title) */
.stApp h1 { 
    font-size: 2.5em; /* From style.css h1 */
    margin-bottom: 20px; /* From style.css h1 */
    color: white; /* Ensure heading is white */
}

/* Paragraph styles (from implicit p tags and st.write) */
.stApp p { 
    color: white; /* Explicitly set color for paragraphs */
    margin-bottom: 20px; /* Spacing below the paragraph (replaces <br>) */
    text-align: center; /* Ensure paragraph is centered */
}

/* Input field styles (from style.css input[type="text"]) */
/* Target the div that wraps the input field to control its width and centering */
.stTextInput > div:first-child { 
    width: 80% !important; /* From style.css input[type="text"] */
    margin: 0 auto 20px auto; /* Centers the input field horizontally and adds bottom margin */
}

/* Target the actual input element for specific styling */
.stTextInput > div > div > input {
    padding: 10px; /* From style.css input[type="text"] */
    border: none; /* From style.css input[type="text"] */
    border-radius: 20px; /* From style.css input[type="text"] */
    font-size: 1em; /* From style.css input[type="text"] */
    outline: none; /* From style.css input[type="text"] */
    text-align: center; /* From style.css input[type="text"] */
    
    /* Ensure typed text is black and background is white */
    color: black !important; 
    background-color: white !important; 
    /* For placeholder text color (cross-browser compatibility) */
    -webkit-text-fill-color: black !important; /* For webkit browsers (Chrome, Safari) */
    opacity: 1 !important; /* Ensure placeholder is not faded */
}
/* For Firefox placeholder */
.stTextInput > div > div > input::placeholder {
    color: black !important;
    opacity: 1 !important;
}

/* Button styles (from style.css button) */
.stButton > button {
    padding: 10px 25px; /* From style.css button */
    background-color: #fcfcfc !important; /* Default button background (white) */
    border: none; /* From style.css button */
    border-radius: 20px; /* From style.css button */
    font-size: 1em; /* From style.css button */
    cursor: pointer; /* From style.css button */
    transition: 0.3s ease; /* From style.css button */
    
    /* Centering the button itself and its text */
    text-align: center !important; /* Ensures button text is horizontally centered */
    display: flex !important; /* Make it a flex container to center content inside */
    justify-content: center !important; /* Center content horizontally within the flex container */
    align-items: center !important; /* Center content vertically within the flex container */
    width: fit-content; /* Make the button only as wide as its content + padding */
    margin-left: auto; /* For centering the button element itself */
    margin-right: auto; /* For centering the button element itself */
}

/* Target the span *inside* the button for text color */
.stButton > button span {
    color: rgb(0, 0, 0) !important; /* Ensure button text is black */
}

/* Button hover styles (from style.css button:hover) */
.stButton > button:hover {
    background-color: #00ffae !important; /* Hover background color */
}

/* Also ensure text remains black on hover */
.stButton > button:hover span {
    color: rgb(0, 0, 0) !important; /* Ensure text remains black on hover */
}


/* Weather data display styles (from style.css .weather-data) */
.weather-data {
    margin-top: 20px; /* From style.css .weather-data */
    font-size: 1.2em; /* From style.css .weather-data */
    color: white; /* From style.css .weather-data */
    text-align: center; /* Ensure weather data is centered */
}
.weather-data h2 {
    margin-bottom: 10px; /* From style.css .weather-data h2 */
    color: white; /* Ensure h2 in weather data is white */
}
.weather-data p {
    margin: 5px 0; /* From style.css .weather-data p */
    color: white; /* Ensure p in weather data is white */
}

/* Adjust image size within weather data (missing in original CSS, but present in HTML JS output) */
.weather-data img {
    width: 70px !important; /* Explicitly set width */
    height: 70px !important; /* Explicitly set height */
    display: block; /* Make it a block element to center with margin: auto */
    margin: 10px auto; /* Center the image */
}
</style>
""", unsafe_allow_html=True)


# --- Weather Data Fetching Function (Converted from script.js) ---
def get_weather_data(city_name):
    """Fetches weather data from WeatherAPI."""
    if not city_name:
        return "Please enter a city name." # Matches alert in JS

    try:
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}"
        response = requests.get(url)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json() # Matches response.json() in JS

        if "error" in data: # Matches data.error check in JS
            return f"Cannot find city: {data['error']['message']}" # Matches "Cannot find city" in JS
        
        location = data["location"]
        current = data["current"]

        # Dynamically construct HTML content (matches weatherInfo.innerHTML in JS)
        weather_html = f"""
        <div class="weather-data">
            <h2>The weather in {location["name"]}, {location["country"]}:</h2>
            <p><img src="https:{current["condition"]["icon"]}" alt="{current["condition"]["text"]}" style="width: 70px; height: 70px;"></p>
            <p><strong>Temperature:</strong> {current["temp_c"]} °C</p>
            <p><strong>Weather:</strong> {current["condition"]["text"]}</p>
            <p><strong>Humidity:</strong> {current["humidity"]}%</p>
            <p><strong>Wind Speed:</strong> {current["wind_kph"]} kph</p>
        </div>
        """
        return weather_html

    except requests.exceptions.RequestException as e: # Catches network errors
        return f"An error occurred while fetching weather data: {e}" # Matches console.error in JS
    except Exception as e: # Catches any other unexpected errors
        return f"An unexpected error occurred: {e}"

# --- Streamlit App Layout (Mirrors HTML structure and JS logic) ---

# Replicates <h1>Weather Information</h1>
st.title("Weather Information") 
# Replicates <p>Enter city name to get the weather information</p>
st.write("Enter city name to get the weather information") 

# Replicates <input type="text" id="cityName">
# The label is hidden for visual consistency with original design, but present for accessibility
city = st.text_input("City Name Input", placeholder="e.g., London, New York, Tokyo", key="city_input", label_visibility="hidden")

# Replicates <button id="searchButton">Get Information</button> and its click handler
if st.button("Get Information"):
    with st.spinner("Fetching weather data..."): # Provides feedback during API call
        weather_result = get_weather_data(city)
        # Display results based on the return from get_weather_data
        if weather_result.startswith("Cannot find city") or weather_result.startswith("An error occurred"):
            st.error(weather_result) 
        elif weather_result.startswith("Please enter a city name"):
            st.warning(weather_result) 
        else:
            st.markdown(weather_result, unsafe_allow_html=True) # Displays the generated HTML weather data