import streamlit as st
import pandas as pd

# Funcția pentru a inițializa un DataFrame cu date predefinite
def load_data():
    return pd.DataFrame({
        "Avatar": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
        ],
        "Descriere": [
            "Echipament 1",
            "Echipament 2",
            "Echipament 3"
        ],
        "Preț": [
            "1000€",
            "1500€",
            "2000€"
        ],
        "Link": [
            "https://www.example.com/produs1",
            "https://www.example.com/produs2",
            "https://www.example.com/produs3"
        ]
    })

# Funcția pentru a afișa și edita tabelul
def display_table(df):
    edited_df = st.data_editor(
        df,
        column_config={
            "Avatar": st.column_config.ImageColumn(
                "Preview Image",
                help="Link către imaginea echipamentului sau software-ului",
            ),
            "Descriere": "Descriere",
            "Preț": "Preț",
            "Link": st.column_config.LinkColumn("Link"),
        },
        num_rows="dynamic",
        hide_index=True,
    )
    return edited_df

# Funcția principală
def main():
    st.title("Monitorizare Soluții Echipamente și Software")

    # Încarcă datele predefinite
    df = load_data()

    # Afișează tabelul și permite editarea
    display_table(df)

if __name__ == "__main__":
    main()




