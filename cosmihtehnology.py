import streamlit as st
import tabula
import json
import os
import psutil

# Titlul aplicației
st.title("Extragere Tabele din PDF folosind Tabula")

# Monitorizare resurse
def get_resource_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info().rss / 1024 ** 2  # Convert to MB
    cpu_percent = psutil.cpu_percent(interval=1)
    return memory_info, cpu_percent

# Afiseaza utilizarea resurselor
memory, cpu = get_resource_usage()
st.sidebar.header("Utilizare Resurse")
st.sidebar.write(f"Memorie utilizată: {memory:.2f} MB")
st.sidebar.write(f"Utilizare CPU: {cpu:.2f}%")

# Incarcă fișierul PDF
uploaded_file = st.file_uploader("Încarcă PDF-ul", type="pdf")

if uploaded_file is not None:
    # Salvează fișierul PDF încărcat
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extragere date utilizând metoda "stream"
    tables_stream = tabula.read_pdf("temp.pdf", pages='all', multiple_tables=True, stream=True)
    json_output_stream = [table.to_dict(orient='records') for table in tables_stream]
    json_stream = json.dumps(json_output_stream, indent=4)

    # Extragere date utilizând metoda "lattice"
    tables_lattice = tabula.read_pdf("temp.pdf", pages='all', multiple_tables=True, lattice=True)
    json_output_lattice = [table.to_dict(orient='records') for table in tables_lattice]
    json_lattice = json.dumps(json_output_lattice, indent=4)

    # Afișează JSON-ul și oferă opțiunea de descărcare
    st.subheader("JSON extras folosind metoda 'Stream'")
    st.json(json_stream)

    st.download_button(
        label="Descarcă JSON (Stream)",
        data=json_stream,
        file_name='output_stream.json',
        mime='application/json'
    )

    st.subheader("JSON extras folosind metoda 'Lattice'")
    st.json(json_lattice)

    st.download_button(
        label="Descarcă JSON (Lattice)",
        data=json_lattice,
        file_name='output_lattice.json',
        mime='application/json'
    )

    # Șterge fișierul temporar
    os.remove("temp.pdf")
