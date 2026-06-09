# Python Weather Forecast Tool

A Python command-line application, initially created in Replit, that queries the user for a location and returns daily and future weather forecasts. The application also includes error catching for data failures. 

## 🚀 Features
*   **Data Validation** Real-time user input validation before hitting external network endpoints, reducing unnecessary API calls.
*   **API** Connects seamlessly to third-party REST APIs (SheCodes Weather API) utilizing the `requests` library to parse structured JSON weather 
*   **Exception Handling** Implemented try-except error catching blocks to gracefully handle network dropouts, timeout anomalies, and invalid API response without crashing the runtime.
*   **Environment Isolation** Uses'python.dotenv' file handling to isolate private API keys and URI's.
*   **Enhanced UX Terminal Formatting:** Utilizes the `Rich` text library to render tabular multi-day forecast metrics, progress meters, and color-coded status elements directly inside the console.

## 🛠️ Tech Stack
*   **Core Engine:** Python 3
*   **Network Layer:** `requests` 
*   **Security & Configuration:** `python-dotenv`
*   **UI/UX Formatting:** `Rich` terminal text compilation

## 🌐 Live Demonstration & Portfolio

To protect secure API infrastructure and private environment credentials, local execution requires private access tokens. You can view a complete functional walkthrough, system architecture documentation, and the live interface directly on my professional portfolio:

👉 **[View Project Showcase on portfolio site] https://amyrowell.dev/ **

## 📝 Insights & Competencies
Developing this application served as a sandbox to demonstrate key modern engineering practices:

Production-Grade File I/O: Managing runtime environments and file streams securely without compromising credential architecture.

Data Layout Serialization: Parsing, sorting, and transforming raw API JSON endpoints into human-readable data layouts.

