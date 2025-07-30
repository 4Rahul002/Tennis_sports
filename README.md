# Tennis Analytics: Unlocking Tennis Data with SportRadar API

## Overview

This project aims to develop a comprehensive solution for managing, visualizing, and analyzing tennis competition and ranking data extracted from the SportRadar API. The application parses JSON data, stores structured information in a MySQL database, and provides intuitive insights into tournaments, competition hierarchies, and player rankings using an interactive Streamlit dashboard.

## Features

- Event Exploration: Navigate through competition and category hierarchies.
- Trend Analysis: Visualize distribution of competition types and gender.
- Performance Insights: Analyze player rankings, points, and movement.
- Country Breakdown: Explore competitor distribution across different countries.
- Decision Support: Data-driven insights for sports analysts and organizations.

## Technical Stack

- Language: Python
- Database: MySQL
- Application: Streamlit
- Data Visualization: Plotly
- API Integration: SportRadar Tennis API

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- MySQL server installed and running
- Access to SportRadar Tennis API (Trial or Production key)

### Installation

1. Clone the Repository:

   ```bash
   git clone <repository-url>
   cd Final_Major_Project
   ```

2. Set Up a Virtual Environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the Database:

   - Create a database named `tennis`
   - Run the SQL schema to create tables: `Competitor`, `Competitor_Rankings`, `Competitions`, `Categories`
   - Insert or load tennis data using SportRadar API

5. Run the Application:
   ```bash
   python -m streamlit run streamlitapp.py
   ```

## Project Structure

```
Final_Major_Project/
│
├── streamlitapp.py           # Main Streamlit dashboard
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation
└── data/                     # Data scripts or files
```

## Usage

- Extract tennis data from the SportRadar API in JSON format
- Convert and insert the structured data into a MySQL database
- Launch the Streamlit dashboard to visualize player rankings and competitions
- Filter and explore data by category, gender, and ranking

## Documentation

- SQL Queries: Stored in the `docs/` folder or inside your schema SQL file
- Project Report: Explains schema design, workflow, API usage, and results

## Author

Rahul Chavan – Sports Radar Project
