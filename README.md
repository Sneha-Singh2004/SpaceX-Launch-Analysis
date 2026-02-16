SpaceX Launch Analysis & Dashboard

Overview

This project analyzes historical SpaceX launch data to understand launch trends, mission success patterns, and performance improvements over time.
The project follows a complete data workflow:
• Data Collection from API
• Data Cleaning & Wrangling
• Exploratory Data Analysis (EDA)
• SQL-based Analysis
• Predictive Modeling
• Interactive Dashboard using Dash
The goal is to combine data analysis, visualization, SQL querying, and machine learning into one structured pipeline.

## Project Structure

SpaceX-Launch-Analysis/
│
├── data/
│ ├── spacex_launch_data.csv
│ └── cleaned_spacex_data.csv
│
├── notebooks/
│ ├── 1_data_collection.ipynb
│ ├── 2_data_wrangling.ipynb
│ ├── 3_eda_visualization.ipynb
│ ├── 4_sql_analysis.ipynb
│ ├── 5_predictive_modeling.ipynb
│ └── 6_folium_map.ipynb
│
├── scripts/
│ └── app.py
│
├── sql/
│ └── spacex.db
│
├── requirements.txt
└── README.md

Features Implemented

1️. Data Collection
• Fetched SpaceX launch data from the SpaceX public API
• Converted JSON response into structured DataFrame
• Saved raw dataset as CSV

2️. Data Cleaning
• Handled missing values
• Converted data types
• Extracted useful features (year, success flag, etc.)
• Exported cleaned dataset

3️. Exploratory Data Analysis
• Launch count over years
• Success rate trend
• Success vs flight number
• Distribution analysis

4️. SQL Analysis
• Created SQLite database
• Executed SQL queries for yearly success rate
• Aggregation and grouping using SQL

5️. Predictive Modeling
• Feature selection
• Train-test split
• Random Forest classifier
• Model evaluation (accuracy, confusion matrix, classification report)

6️. Interactive Dashboard
• Built using Dash & Plotly
• Success distribution visualization
• Success vs flight number scatter plot
• Local deployment on 127.0.0.1:8050

Technologies Used:

• Python
• Pandas
• NumPy
• Matplotlib
• Seaborn
• SQLite
• Scikit-learn
• Plotly
• Dash

How to Run the Project

1️. Clone the repository
git clone <your-repo-link>
cd SpaceX-Launch-Analysis

2️. Install dependencies
pip install -r requirements.txt

3️. Run the Dashboard
python scripts/app.py
Then open:
http://127.0.0.1:8050

Model Performance:

The Random Forest classifier achieved high accuracy on the test dataset.
Evaluation metrics include:
• Accuracy
• Precision
• Recall
• F1-Score
• Confusion Matrix

Future Improvements:

• Add more feature engineering
• Hyperparameter tuning
• Deploy dashboard to cloud (Render / Heroku / AWS)
• Add interactive filters (launch site, year range, payload type)

Author

Sneha Singh
Data Science & Analytics
