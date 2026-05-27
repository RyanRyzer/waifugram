import streamlit as st
import pandas as pd
from utils.database import cursor

st.set_page_config(page_title="History")

st.title("📜 Prediction History")

cursor.execute(
    "SELECT * FROM history"
)

rows = cursor.fetchall()

if rows:

    df = pd.DataFrame(
        rows,
        columns=[
            'ID',
            'Username',
            'Prediction',
            'Confidence',
            'Image Path'
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.warning("Belum ada history")