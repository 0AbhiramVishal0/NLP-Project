# Emergency Crisis Coordination Analytics

This project aims to use social media analytics for emergency crisis coordination, focusing on Twitter data related to disasters or emergencies in Australia. The project includes data collection, preprocessing, NLP analysis, geographical analysis, and visualization.

## Folder Structure

- `data/`: Contains datasets and shapefiles.
- `notebooks/`: Contains Jupyter notebooks for different stages of the project.
- `app/`: Contains files for the Flask application.
- `utils/`: Contains utility scripts for data management and analysis.
- `dash_app.py`: Main script for the Dash application.
- `requirements.txt`: Lists all the required Python packages.
- `README.md`: Project description and setup instructions.

## Setup Instructions

1. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the data collection notebook:
    ```bash
    jupyter notebook scripts/data_collection.ipynb
    ```

3. Run the data preprocessing notebook:
    ```bash
    jupyter notebook scripts/data_preprocessing.ipynb
    ```

4. Run the NLP analysis notebook:
    ```bash
    jupyter notebook scripts/nlp_analysis.ipynb
    ```

5. Run the geographical analysis notebook:
    ```bash
    jupyter notebook scripts/geographical_analysis.ipynb
    ```

6. Run the visualization notebook:
    ```bash
    jupyter notebook scripts/visualization.ipynb
    ```

7. Start the Flask app:
    ```bash
    export FLASK_APP=app
    flask run
    ```

8. Start the Dash app:
    ```bash
    python dash_app.py
    ```

## Project Description

This project provides a comprehensive tool for social media analytics focused on emergency crisis coordination using Twitter data, with enhanced visualization and an advanced user interface.
