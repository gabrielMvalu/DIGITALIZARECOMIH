import streamlit as st
import pandas as pd

# Stil CSS personalizat pentru a face tabelul să ocupe întreaga lățime și să împacheteze textul
st.markdown(
    """
    <style>
    .dataframe-container {
        max-width: 100%;
    }
    .data-editor .st-DataFrame td {
        white-space: normal;
        word-wrap: break-word;
    }
    .stApp {
        max-width: 100%;
        padding: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Funcția pentru a inițializa un DataFrame cu date predefinite
def load_data():
    return pd.DataFrame({
        "Avatar": [
            "https://s13emagst.akamaized.net/products/42022/42021954/images/res_d497184c433aa52544254dc3ff7772e6.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
        ],
        "Descriere": [
            "Sistem Desktop PC Powerup AQUA Intel Core i9 14900K 24Core 6.0Ghz, RTX 4090 24GB GDDR6 384bit, 64GB DDR5 6000Mhz, SSD 4TB M.2, 1000W, Custom Watercooling",
            "Echipament 2",
            "Echipament 3"
        ],
        "Preț": [
            "36.533RON",
            "1500€",
            "2000€"
        ],
        "Link": [
            "https://www.emag.ro/sistem-desktop-pc-powerup-aqua-intel-core-i9-14900k-24core-6-0ghz-rtx-4090-24gb-gddr6-384bit-64gb-ddr5-6000mhz-ssd-4tb-m-2-1000w-custom-watercooling-336699/pd/DRNGCTYBM/?X-Search-Id=2d2a3f29c4a3e5cd2dc8&X-Product-Id=156269361&X-Search-Page=1&X-Search-Position=7&X-Section=search&X-MB=0&X-Search-Action=view",
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





