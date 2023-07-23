import random
import pandas as pd
import streamlit as st

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 5) for _ in range(3)],
        "sales": [200, 550, 1000]    }
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
        "sales": st.column_config.ProgressColumn(
            "Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000
        ),
    },
    hide_index=True,
)

