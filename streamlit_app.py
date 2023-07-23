import random
import pandas as pd
import streamlit as st

data = {
    "product_name": [
        "Commercial Espresso Machine", 
        "Commercial Espresso Machine"
    ],
    "supplier_name": [
        "Espresso Parts", 
        "Espresso Zone"
    ],
    "address": [
        "4315 Lacey Blvd. SE Lacey, WA 98503", 
        "6911 Washington Ave, Philadelphia, PA 19142"
    ],
    "price": [
        "$5000-$8000", 
        "$2000-$15000"
    ],
    "quality": [
        "Medium", 
        "High"
    ],
    "environmental_score": [
        4.5, 
        3
    ],
    "ETA": [
        "750",
        "2900"
    ]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

st.dataframe(
    df,
    column_config={
        "product_name": "Product Name",
        "supplier_name": "Supplier Name",
        #"address": "Address",
        "price": "Price",
        "quality": "Quality",
        "environmental_score": st.column_config.NumberColumn(
            "Environmental Score",
            help="Stars",
            format="%d ⭐",
        ),
        "ETA": st.column_config.ProgressColumn(
            "ETA",
            help="ETA",
            format="$%f",
            min_value=0,
            max_value=3000
        ),
    },
    hide_index=True,
)
