import streamlit as st

# Definim preturile pentru fiecare solutie
preturi_hardware = {
    "Sistem Desktop PC Powerup AQUA Intel Core i9 14900K": 36533,
    "Sistem Powerup ROG AMD Ryzen 9 7950X": 32989,
    "Mac Studio, Apple M2 Ultra": 21999,
    "Sistem Mini Apple Mac Studio, M2 Ultra": 28865,
    "QNAP hibrid NAS": 3822,
    "Asustor NAS": 4103
}

preturi_software = {
    "Autodesk AEC Collection": 4102 * 4.9,  # convertit in RON
    "Website de prezentare": 1490 * 4.9,  # convertit in RON
    "Publicitate Online": 2500
}

# Sidebar pentru calculator
st.sidebar.header("Calculator Total Soluții")

# Selectează un calculator
calculator_selectat = st.sidebar.selectbox(
    "Selectează un calculator",
    list(preturi_hardware.keys())[:4]
)

# Selectează un NAS
nas_selectat = st.sidebar.selectbox(
    "Selectează o soluție NAS",
    list(preturi_hardware.keys())[4:6]
)

# Selectează soluția software
software_selectat = st.sidebar.selectbox(
    "Selectează soluția software",
    list(preturi_software.keys())
)

# Afișează totalul
pret_total = preturi_hardware[calculator_selectat] + preturi_hardware[nas_selectat] + preturi_software[software_selectat]
st.sidebar.write(f"**Cost Total:** {pret_total:.2f} RON")

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
        st.write("Sistem Desktop PC Powerup AQUA Intel Core i9 14900K 24Core 6.0Ghz, RTX 4090 24GB GDDR6 384bit, 64GB DDR5 6000Mhz, SSD 4TB M.2, 1000W, Custom Watercooling")
        st.write("Preț: 36.533 RON")
        st.write("[Detalii Produs](https://www.emag.ro/sistem-desktop-pc-powerup-aqua-intel-core-i9-14900k-24core-6-0ghz-rtx-4090-24gb-gddr6-384bit-64gb-ddr5-6000mhz-ssd-4tb-m-2-1000w-custom-watercooling-336699/pd/DRNGCTYBM/?X-Search-Id=2d2a3f29c4a3e5cd2dc8&X-Product-Id=156269361&X-Search-Page=1&X-Search-Position=7&X-Section=search&X-MB=0&X-Search-Action=view)")

        # A doua ofertă pentru Windows
        st.image("https://s13emagst.akamaized.net/products/28486/28485377/images/res_ae7bed7e7ffd9a706e2f7f869d4aae08.jpg", width=150)
        st.write("Sistem Powerup ROG AMD Ryzen 9 7950X 16Core 5.7Ghz, RTX 4090 24GB GDDR6X 384bit, 64GB DDR5, SSD 2TB M.2, 1000W, Custom Watercooling, Windows 11 PRO")
        st.write("Preț: 32.989 RON")
        st.write("[Detalii Produs](https://www.emag.ro/sistem-powerup-rog-amd-ryzen-9-7950x-16core-5-7ghz-rtx-4090-24gb-gddr6x-384bit-64gb-ddr5-ssd-2tb-m-2-1000w-custom-watercooling-windows-11-pro/pd/DKB02YBBM/)")

    # Coloana pentru sistemele Apple
    with col2:
        st.subheader("Sisteme Apple")

        # Prima ofertă pentru Apple
        st.image("https://istyle.ro/media/catalog/product/cache/image/e9c3970ab036de70892d86c6d221abfe/m/a/mac_studio_pdp_image_position-1__wwen_2_2_2_1.jpg", width=150)
        st.write("Mac Studio, procesor Apple M2 Ultra, 24 nuclee CPU and 60 nuclee GPU, 64GB, 1TB")
        st.write("Preț: 21.999 RON")
        st.write("[Detalii Produs](https://istyle.ro/mac-studio-procesor-apple-m2-ultra-24-nuclee-cpu-and-60-nuclee-gpu-64gb-1tb.html)")

        # A doua ofertă pentru Apple
        st.image("https://cdn.forit.ro/images/products/img_202306241139/458188/full/sistem-mini-apple-mac-studio-procesor-m2-ultra-64gb-ram-1tb-ssd-60-cores-gpu-macos-int-755639.jpg", width=150)
        st.write("Sistem Mini Apple Mac Studio, Procesor M2 Ultra, 64GB RAM, 1TB SSD, 60 cores GPU, macOS, INT")
        st.write("Preț: 28.865 RON")
        st.write("[Detalii Produs](https://www.forit.ro/sisteme-mini/apple/458188-mac-studio-procesor-m2-ultra-64gb-ram-1tb-ssd-60-cores-gpu-macos-int/?gad_source=1&gbraid=0AAAAADHLg72siqybntl7-cMBbIZ1YFv77&gclid=CjwKCAjw_ZC2BhAQEiwAXSgClrLP5G2j-UPBB2Aputg-k1oHF0f3c2Yeft3Oo09oGV7xYWBKAIDDrRoC1y8QAvD_BwE)")

    # Coloana pentru sistemele hardware NAS
    with col3:
        st.subheader("Sisteme NAS (Back Solutions)")

        # Prima ofertă pentru NAS
        st.image("https://s13emagst.akamaized.net/products/37892/37891461/images/res_35e15b3fc1818673c5fb4ae488919a1d.jpg", width=150)
        st.write("Unitate NAS, QNAP hibrid 2 sertare+2x slot SSD, HS-453DX-8G 4x1,8 GHz, 8 GB RAM, 1x100/1000, 1 x 10GBASE-T, 3xUSB3.2, 2xUSB2.0")
        st.write("Preț: 3.822 RON")
        st.write("[Detalii Produs](https://www.emag.ro/unitate-nas-qnap-hibrid-2-sertare-2x-slot-ssd-4x1-8-ghz-8-gb-ram-1x100-1000-1-x-10gbase-t-3xusb3-2-2xusb2-0-hs-453dx-8g/pd/DDD8B0MBM/?X-Search-Id=2859ed51ada888339b40&X-Product-Id=122646789&X-Search-Page=1&X-Search-Position=32&X-Section=search&X-MB=0&X-Search-Action=view)")

        # A doua ofertă pentru NAS
        st.image("https://s13emagst.akamaized.net/products/64235/64234525/images/res_c2ad6bc4273a8732257d17d515150d49.jpg", width=150)
        st.write("Unitate de stocare in retea, Asustor, 4GB, 6xM.2 NVMe")
        st.write("Preț: 4.103 RON")
        st.write("[Detalii Produs](https://www.emag.ro/unitate-de-stocare-in-retea-asustor-4gb-6xm-2-nvme-fs6706t/pd/DN7KTTYBM/?ref=embedding_similar_model_1_1&provider=rec&recid=rec_88_cd062cb5bed572d1adaaa7342540037b364b51b4c0c99a31e49d86503f2bae1a_1724173712&scenario_ID=88)")

with tab2:
    st.header("Soluții Software")

    # Trei coloane pentru diferite soluții software
    col1, col2, col3 = st.columns(3)

    # Soluțiile software propuse în col1
    with col1:
        st.subheader("Software CAD și BIM")

        # Prima soluție
        st.write("**Autodesk Architecture, Engineering & Construction Collection**")
        st.write("Preț: 4.102 Euro/an")
        st.write("[Detalii Produs](https://www.autodesk.com/eu/collections/architecture-engineering-construction/overview?term=1&tab=subscription)")

        # Cursuri pentru soluția Autodesk
        st.write("**Cursuri pentru Autodesk Architecture, Engineering & Construction**")
        st.write("Preț: momentan nu avem oferta de preț!")
        st.write("[Detalii Cursuri](https://www.autodesk.com/eu/collections/architecture-engineering-construction/overview?term=1&tab=subscription)")

    # Soluțiile software propuse în col2
    with col2:
        st.subheader("Site web de prezentare / site web functii complexe")

        # Prima soluție
        st.write("**Website**")
        st.write("Preț: de la 1490€ euro")
        st.write("[Detalii Produs](https://www.example.com/produs6)")

        # A doua soluție
        st.write("**Achiziționarea de servicii de cloud computing de nivel mediu-mare**")
        st.write("Preț: 2.500 RON")
        st.write("[Detalii Produs](https://webage.ro/pret-site-web/?gad_source=1&gbraid=0AAAAADqflNLcPYkwBIhaNQtdlrvKakCCr&gclid=CjwKCAjw_ZC2BhAQEiwAXSgClgTokNiyMRYoSDsg9_PrL9EhKfhp2kVtKE4eiA9mru-1qrtxH9haABoC7i8QAvD_BwE#preturi)")

    # Soluțiile software propuse în col3
    with col3:
        st.subheader("Sisteme de calcul structural")

        # Prima soluție
        st.write("**Arxiv de la Consoft**")
        st.write("Preț: momentan nu avem oferta de preț!")
        st.write("[Detalii Produs](https://www.consoft.ro/axisvm/info/x7/)")

        # Soluția pentru E-commerce și Publicitate Online
        st.write("**soluții pentru publicitate**")
        st.write("Preț: 1.500 - 2500 RON")
        st.write("[Detalii Produs](https://generator.adroltenia.ro)")





