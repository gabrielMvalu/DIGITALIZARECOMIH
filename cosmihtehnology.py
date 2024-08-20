import streamlit as st
import pandas as pd

# Funcția pentru a inițializa un DataFrame gol sau a-l încărca dintr-o sursă externă
def load_data():
    return pd.DataFrame(columns=["Avatar", "Descriere", "Preț", "Link"])

# Funcția pentru a afișa și edita tabelul
def display_table(df):
    edited_df = st.data_editor(
        df,
        column_config={
            "Avatar": st.column_config.ImageColumn("Avatar"),
            "Descriere": "Descriere",
            "Preț": st.column_config.NumberColumn("Preț", format="€{:,.2f}"),
            "Link": st.column_config.LinkColumn("Link"),
        },
        num_rows="dynamic",
    )
    return edited_df

# Funcția principală
def main():
    st.title("Monitorizare Soluții Echipamente și Software")

    # Inițializează sau încarcă datele
    if "df" not in st.session_state:
        st.session_state.df = load_data()

    # Afișează tabelul și permite editarea
    st.session_state.df = display_table(st.session_state.df)

    # Buton pentru a adăuga un rând gol
    if st.button("Adaugă un rând gol"):
        st.session_state.df = st.session_state.df.append(
            pd.Series(["", "", 0, ""], index=st.session_state.df.columns), ignore_index=True
        )

    # Buton pentru a salva datele (în sesiune, local sau în alt loc)
    if st.button("Salvează modificările"):
        st.success("Modificările au fost salvate!")

if __name__ == "__main__":
    main()
