# Reproducible Research Term Project

## Setup

1. Clone the repository

2. Create a virtual environment
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux

3. Install dependencies
   pip install -r requirements.txt

## Data

You can either download master.csv from the link below or in the file named data:
https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016

Place it in the data folder

## Running the analysis

1. Run the data processing pipeline first:
   python src/data_processing.py

2. Open the notebook:
   jupyter notebook notebooks/suicide_rates.ipynb

3. Run all cells top to bottom
