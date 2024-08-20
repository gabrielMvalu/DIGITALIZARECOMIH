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

        # Prima ofertă pentru Windows
        st.image("https://s13emagst.akamaized.net/products/42022/42021954/images/res_d497184c433aa52544254dc3ff7772e6.png", width=150)
        st.write("Sistem Desktop PC Powerup AQUA Intel Core i9 14900K")
        st.write("Preț: 36.533 RON")
        st.write("[Detalii Produs](https://www.emag.ro/sistem-desktop-pc-powerup-aqua-intel-core-i9-14900k-24core-6-0ghz-rtx-4090-24gb-gddr6-384bit-64gb-ddr5-6000mhz-ssd-4tb-m-2-1000w-custom-watercooling-336699/pd/DRNGCTYBM/?X-Search-Id=2d2a3f29c4a3e5cd2dc8&X-Product-Id=156269361&X-Search-Page=1&X-Search-Position=7&X-Section=search&X-MB=0&X-Search-Action=view)")

        # A doua ofertă pentru Windows
        st.image("https://s13emagst.akamaized.net/products/42022/42021954/images/res_d497184c433aa52544254dc3ff7772e6.png", width=150)
        st.write("Sistem Powerup ROG AMD Ryzen 9 7950X 16Core 5.7Ghz, RTX 4090 24GB GDDR6X 384bit, 64GB DDR5, SSD 2TB M.2, 1000W, Custom Watercooling, Windows 11 PRO")
        st.write("Preț: 32.999 RON")
        st.write("[Detalii Produs](https://www.emag.ro/sistem-powerup-rog-amd-ryzen-9-7950x-16core-5-7ghz-rtx-4090-24gb-gddr6x-384bit-64gb-ddr5-ssd-2tb-m-2-1000w-custom-watercooling-windows-11-pro/pd/DKB02YBBM/)")

    # Coloana pentru sistemele Apple
    with col2:
        st.subheader("Sisteme Apple")

        # Prima ofertă pentru Apple
        st.image("https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-24-green-selection-hero-202104?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1617479510000", width=150)
        st.write("Apple iMac 24-inch with Retina 4.5K display")
        st.write("Preț: 10.999 RON")
        st.write("[Detalii Produs](https://www.apple.com/imac-24/)")

        # A doua ofertă pentru Apple
        st.image("https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-finishes-hero-202206?wid=4000&hei=3072&fmt=jpeg&qlt=90&.v=1653493200207", width=150)
        st.write("Apple MacBook Air 13-inch M2")
        st.write("Preț: 8.499 RON")
        st.write("[Detalii Produs](https://www.apple.com/macbook-air-m2/)")

    # Coloana pentru sistemele hardware NAS
    with col3:
        st.subheader("Sisteme NAS (Back Solutions)")

        # Prima ofertă pentru NAS
        st.image("https://static.synology.com/en-global/products/DS920+/images/1_2000x2000.png", width=150)
        st.write("Synology DiskStation DS920+ NAS")
        st.write("Preț: 2.800 RON")
        st.write("[Detalii Produs](https://www.synology.com/en-global/products/DS920+)")

        # A doua ofertă pentru NAS
        st.image("https://static.qnap.com/images/products/hs-453dx_1.png", width=150)
        st.write("QNAP HS-453DX Silent NAS")
        st.write("Preț: 3.200 RON")
        st.write("[Detalii Produs](https://www.qnap.com/en/product/hs-453dx)")

with tab2:
    st.header("Soluții Software")

    # Trei coloane pentru diferite soluții software
    col1, col2, col3 = st.columns(3)

    # Soluțiile software propuse în col1
    with col1:
        st.subheader("Internet și Conectivitate")
        
        # Prima soluție
        st.write("**Acces la Internet pentru 50% din angajați**")
        st.write("Preț: 1.000 RON")
        st.write("[Detalii Produs](https://www.example.com/produs4)")

        # A doua soluție
        st.write("**Acces la Internet de mare viteză (cel puțin 30 Mbps)**")
        st.write("Preț: 1.200 RON")
        st.write("[Detalii Produs](https://www.example.com/produs5)")

    # Soluțiile software propuse în col2
    with col2:
        st.subheader("Contracte IT și Servicii")

        # Prima soluție
        st.write("**Contracte încheiate cu specialiști IT**")
        st.write("Preț: 3.000 RON")
        st.write("[Detalii Produs](https://www.example.com/produs6)")

        # A doua soluție
        st.write("**Achiziționarea de servicii de cloud computing de nivel mediu-mare**")
        st.write("Preț: 2.500 RON")
        st.write("[Detalii Produs](https://www.example.com/produs7)")

    # Soluțiile software propuse în col3
    with col3:
        st.subheader("E-commerce și Publicitate Online")

        # Prima soluție
        st.write("**Număr soluții pentru publicitatea plătită online**")
        st.write("Preț: 1.500 RON")
        st.write("[Detalii Produs](https://www.example.com/produs8)")

        # A doua soluție
        st.write("**Realizarea de vânzări prin intermediul comerțului electronic**")
        st.write("Preț: 4.000 RON")
        st.write("[Detalii Produs](https://www.example.com/produs9)")





