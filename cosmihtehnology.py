import streamlit as st

# Definim tab-urile principale pentru categorii de soluții
tab1, tab2 = st.tabs(["Soluții Hardware", "Soluții Software"])

with tab1:
    st.header("Soluții Hardware")

    # Soluțiile hardware propuse
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://s13emagst.akamaized.net/products/42022/42021954/images/res_d497184c433aa52544254dc3ff7772e6.png", width=150)
        st.write("Sistem Desktop PC Powerup AQUA Intel Core i9 14900K")
        st.write("Preț: 36.533 RON")
        st.write("[Detalii Produs](https://www.emag.ro/sistem-desktop-pc-powerup-aqua-intel-core-i9-14900k-24core-6-0ghz-rtx-4090-24gb-gddr6-384bit-64gb-ddr5-6000mhz-ssd-4tb-m-2-1000w-custom-watercooling-336699/pd/DRNGCTYBM/?X-Search-Id=2d2a3f29c4a3e5cd2dc8&X-Product-Id=156269361&X-Search-Page=1&X-Search-Position=7&X-Section=search&X-MB=0&X-Search-Action=view)")

    with col2:
        st.image("https://static.streamlit.io/examples/dog.jpg", width=150)  # Schimbă imaginea cu cea corespunzătoare
        st.write("Laptop XYZ Model")
        st.write("Preț: 7.000 RON")
        st.write("[Detalii Produs](https://www.example.com/produs2)")

    with col3:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=150)  # Schimbă imaginea cu cea corespunzătoare
        st.write("Router 30Mbps")
        st.write("Preț: 500 RON")
        st.write("[Detalii Produs](https://www.example.com/produs3)")

with tab2:
    st.header("Soluții Software")

    # Soluțiile software propuse
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Acces la Internet pentru 50% din angajați**")
        st.write("Preț: 1.000 RON")
        st.write("[Detalii Produs](https://www.example.com/produs4)")

    with col2:
        st.write("**Contracte încheiate cu specialiști IT**")
        st.write("Preț: 3.000 RON")
        st.write("[Detalii Produs](https://www.example.com/produs5)")

    st.write("**Achiziția de servicii cloud computing de nivel mediu-mare**")
    st.write("Preț: 2.500 RON")
    st.write("[Detalii Produs](https://www.example.com/produs6)")






