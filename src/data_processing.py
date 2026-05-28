# src/data_processing.py

import pandas as pd
import numpy as np


# -----------------------------
# LOAD DATA
# -----------------------------
def load_data(path):
    df = pd.read_csv(path)
    return df


# -----------------------------
# CLEAN DATA
# -----------------------------
def clean_data(df):

    # Remove unnecessary columns
    drop_cols = ["HDI for year", "suicides/100k pop"]
    df = df.drop(columns=drop_cols)

    # Rename columns
    df = df.rename(columns={
        "gdp_for_year ($)": "gdp_for_year",
        "gdp_per_capita ($)": "gdp_per_capita",
        "country-year": "country_year"
    })

    # Remove 2016
    df = df[df["year"] != 2016]

    # Remove countries with <= 3 years of data
    counts = df.groupby("country").size() / 12
    bad_countries = counts[counts <= 3].index
    df = df[~df["country"].isin(bad_countries)]

    # Tidy age column
    df["age"] = df["age"].str.replace(" years", "")

    # Clean sex column
    df["sex"] = df["sex"].replace({
        "male": "Male",
        "female": "Female"
    })

    return df


# -----------------------------
# ADD CONTINENTS
# -----------------------------
def add_continent(df):

    continent_map = {
        "United States": "North America",
        "France": "Europe",
        "Japan": "Asia"
    }

    df["continent"] = df["country"].map(continent_map)

    return df


# -----------------------------
# CALCULATE GLOBAL AVERAGE
# -----------------------------
def global_average(df):

    avg = (
        df["suicides_no"].sum() /
        df["population"].sum()
    ) * 100000

    return avg


# -----------------------------
# SAVE DATA
# -----------------------------
def save_data(df, path):
    df.to_csv(path, index=False)


# -----------------------------
# MAIN PIPELINE
# -----------------------------
if __name__ == "__main__":

    df = load_data("data/master.csv")

    df = clean_data(df)

    df = add_continent(df)

    save_data(df, "data/cleaned_suicide_data.csv")

    print("Data preprocessing complete.")
