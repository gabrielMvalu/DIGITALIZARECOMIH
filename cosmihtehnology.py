import streamlit as st
import pandas as pd

# O listă pentru a stoca echipamentele/soluțiile
solutii = []

# Funcție pentru a adăuga o soluție
def adauga_solutie(nume, descriere):
    solutii.append({'nume': nume, 'descriere': descriere, 'aprobat': False})

# Funcție pentru a aproba o soluție
def aproba_solutie(index):
    solutii[index]['aprobat'] = True

# Funcție pentru a elimina o soluție
def elimina_solutie(index):
    del solutii[index]

# Funcție pentru a propune o altă soluție
def propune_solutie():
    st.sidebar.write("Propune o soluție nouă:")
    nume = st.sidebar.text_input("Nume soluție:")
    descriere = st.sidebar.text_area("Descriere soluție:")
    if st.sidebar.button("Propune"):
        adauga_solutie(nume, descriere)
        st.sidebar.success(f"Soluția {nume} a fost propusă.")

# Afișarea soluțiilor existente
def afisare_solutii():
    st.write("## Soluții propuse")
    for index, solutie in enumerate(solutii):
        st.write(f"### {solutie['nume']}")
        st.write(solutie['descriere'])
        if solutie['aprobat']:
            st.write("✅ Aprobat")
        else:
            if st.button(f"Aprobă {solutie['nume']}", key=f"aproba_{index}"):
                aproba_solutie(index)
            if st.button(f"Elimină {solutie['nume']}", key=f"elimina_{index}"):
                elimina_solutie(index)

# Structura aplicației
def main():
    st.title("Monitorizare Proiect Digitalizare")

    # Secțiunea pentru proiectanți
    propune_solutie()

    # Afișare soluții
    afisare_solutii()

if __name__ == "__main__":
    main()
