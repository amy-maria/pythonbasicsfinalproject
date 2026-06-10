# Python Weather Forecast Tool

Initially a Python command-line application created in Replit, I added Flask to the program for more functionality. The app returns the weather inforamtion for a location and returns daily and future weather forecasts. The application also includes error catching for data failures. 

## 🚀 Features
*   **Data Validation** Real-time user input validation before hitting external network endpoints, reducing unnecessary API calls.
*   **API** Connects seamlessly to third-party REST APIs (SheCodes Weather API) utilizing the `requests` library to parse structured JSON weather data.
*   **Exception Handling** Implemented try-except error catching blocks to gracefully handle network dropouts, timeout anomalies, and invalid API response without crashing the runtime.
*   **Environment Isolation** Uses'python.dotenv' file handling to isolate private API keys and URI's.
*   **Enhanced UX Terminal Formatting** Utilized the `Rich` text library to render tabular multi-day forecast metrics, progress meters, and color-coded status elements directly inside the console as a CLI. To render the app in Render, I wrapped my code using Flask and made some modifations to generated HTML and minor CSS styling. 

## 🛠️ Tech Stack
*   **Core Engine:** Python 3
*   **Network Layer:** `requests` 
*   **Security & Configuration:** `python-dotenv`
*   **UI/UX Formatting:** `Rich` terminal text compilation

## 🌐 Live Demonstration & Portfolio

To protect secure API infrastructure and private environment credentials, local execution requires private access tokens. You can view a complete functional walkthrough directly on my professional portfolio:

👉 **[View Project Showcase on portfolio site] https://amyrowell.dev/ **

## 📝 Insights & Competencies
Developed this application as a sandbox to demonstrate key modern engineering practices.

Production-Grade File I/O: Managing runtime environments and file streams securely without compromising credential architecture.

Data Layout Serialization: Parsing, sorting, and transforming raw API JSON endpoints into human-readable data layouts.

