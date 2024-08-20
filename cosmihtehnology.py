import streamlit as st

# Definim tab-urile principale pentru categorii de soluții
tab1, tab2 = st.tabs(["Soluții Hardware", "Soluții Software"])

with tab1:
    st.header("Soluții Hardware")

    # Trei coloane: Windows, Apple, NAS
    col1, col2, col3 = st.columns(3)

    # Coloana pentru sistemele Windows
    with col1:
        st.subheader("Sisteme Windows")
        st.image("https://s13emagst.akamaized.net/products/42022/42021954/images/res_d497184c433aa52544254dc3ff7772e6.png", width=150)
        st.write("Sistem Desktop PC Powerup AQUA Intel Core i9 14900K")
        st.write("Preț: 36.533 RON")
        st.write("[Detalii Produs](https://www.emag.ro/sistem-desktop-pc-powerup-aqua-intel-core-i9-14900k-24core-6-0ghz-rtx-4090-24gb-gddr6-384bit-64gb-ddr5-6000mhz-ssd-4tb-m-2-1000w-custom-watercooling-336699/pd/DRNGCTYBM/?X-Search-Id=2d2a3f29c4a3e5cd2dc8&X-Product-Id=156269361&X-Search-Page=1&X-Search-Position=7&X-Section=search&X-MB=0&X-Search-Action=view)")

    # Coloana pentru sistemele Apple
    with col2:
        st.subheader("Sisteme Apple")
        st.image("https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-24-green-selection-hero-202104?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1617479510000", width=150)
        st.write("Apple iMac 24-inch with Retina 4.5K display")
        st.write("Preț: 10.999 RON")
        st.write("[Detalii Produs](https://www.apple.com/imac-24/)")

    # Coloana pentru sistemele hardware NAS
    with col3:
        st.subheader("Sisteme NAS (Back Solutions)")
        st.image("https://static.synology.com/en-global/products/DS920+/images/1_2000x2000.png", width=150)
        st.write("Synology DiskStation DS920+ NAS")
        st.write("Preț: 2.800 RON")
        st.write("[Detalii Produs](https://www.synology.com/en-global/products/DS920+)")

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






