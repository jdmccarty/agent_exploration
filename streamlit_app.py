import random
import pandas as pd
import streamlit as st

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 5) for _ in range(3)],
        "views_history": [[random.randint(0, 30) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "Supplier Name",
        "stars": st.column_config.NumberColumn(
            "Product Rateing",
            help="Number of Review Stars",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "shipping time": st.column_config.BarChartColumn(
            "Shipping Days", y_min=0, y_max=30
        ),
    },
    hide_index=True,
)

