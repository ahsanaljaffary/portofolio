import requests
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portfolio Ahsan",
    page_icon="♨️",
    layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

with st.container():
    st.subheader("Hai, Saya Ahsan :wave:")
    st.title("PRAKTEK STREAMLIT PORTFOLIO PRIBADI")
    st.write("Halaman web ini dibuat untuk memenuhi tugas Mata Kuliah *Paket Aplikasi Data Mining*")
    st.caption("Dosen Pengampu : Muklisin, S.Kom")

tab1, tab2, tab3, tab4 = st.tabs(["Tentang", "Riwayat Pendidikan", "Pengalaman", "Hubungi Saya"])

with tab1:
    col1, col2 = st.columns((1, 2))
    with col1:
        st.header("Tentang Ahsan")
        st.image("Ahsan.jpeg", caption='Foto : Muhammad Ahsan Jamil', width=300)
    with col2:
        st.title("BIODATA")
        st.write("---")
        st.subheader("Nama : Muhammad Ahsan Jamil")
        st.caption("NIM : 0402201085")
        st.write(
            """
            - Tempat Tanggal Lahir : Jepara, 19 Februari 2002
            - Alamat : Ds. Bategede Kec. Nalumsari Kab. Jepara
            - Hobi : Tidur
            - Cita-cita : Kaya Dunia Akhirat
            - Hal yang disukai : Ngopi
            - Status : Belum Menikah
            """
        )
        st.subheader("*Better Late Than Never*")
        st.caption("_Lebih Baik Terlambat Daripada Tidak Sama Sekali_")

with tab2:
    st.title("Riwayat Pendidikan")
    st.write("Berikut ini adalah urutan jenjang pendidikan yang ditempuh oleh Muhammad Ahsan Jamil selama hidupnya. Terhitung ada 5 lembaga pendidikan yang dilaluinya, diantaranya sebagai berikut:")
    with st.container():
        st.write("---")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.header("1️⃣ MI Nurul Ilmi Bategede")
        with col2:
            st.header("2️⃣ Pesantren Al Bukhori")
        with col3:
            st.header("3️⃣ MTs Plus Al Bukhori")
        with col4:
            st.header("4️⃣ MA Plus Al Bukhori")
        with col5:
            st.header("5️⃣ UNU Rombel Al Bukhori")
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.caption("Alamat : Jl. Sreni Indah Rt. 09 Rw. 03, Bategede, Kec. Nalumsari, Kab. Jepara.")
        with col2:
            st.caption("Alamat : Jl. Cemara Gg. At Taubah Rt. 06 Rw. 03, Sengon - Tanjung - Brebes")
        with col3:
            st.caption("Alamat : Jl. Cemara Gg. At Taubah Rt. 06 Rw. 03, Sengon - Tanjung - Brebes")
        with col4:
            st.caption("Alamat : Jl. Cemara Gg. Al Bukhori Rt. 07 Rw. 03, Sengon - Tanjung - Brebes")
        with col5:
            st.caption("Alamat : Gedung BLKK Pesantren Al Bukhori, Jl. Cemara Gg. At Taubah Rt. 07 Rw. 03, Sengon - Tanjung - Brebes")
    with st.container():
        st.write("---")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image("mi.png", width=200) 
            st.caption("MI Nurul Ilmi adalah jenjang pendidikan pertama yang saya tempuh. Saya lulus dari MI Nurul Ilmi pada tahun 2013.") 
        with col2:
            st.image("pondok.png", width=200)
            st.caption("Usai lulus MI, saya melanjutkan studi sambil mesantren di Pesantren AL Bukhori. Terhitung dari tahun 2013 - sekarang.")
        with col3:
            st.image("mts.png", width=200)
            st.caption("Saat pertama masuk Pesantren, saya melanjutkan pendidikan formal di MTs Plus Al Bukhori. Saya lulus pada tahun 2016") 
        with col4:
            st.image("ma.png", width=190)
            st.caption("MA Plus Al Bukhori menjadi pilihan saya untuk melanjutkan studi usai lulus dari MTs. Meskipun baru berumur 2 tahun pada saat itu, di MA Plus Al Bukhori sudah mengusung 2 jurusan, yaitu IPA dan IPS.")
        with col5:
            st.image("unuu.png", width=195)
            st.caption("Lulus dari MA Plus Al Bukhori, saya berhenti sekolah selama satu tahun, baru melanjutkan studi ke jenjang perkuliahan. UNU Rombel Al Bukhori merupakan cabang dari Kampus Pusat UNU, yang bertempat di Kab. Cirebon.")
        
with tab3:
    st.title("Pengalaman Organisasi")
    st.caption("Tab ini membahas tentang pengalaman organisasi yang dimiliki oleh Ahsan. Dari jenjang MI sampai sekarang. Rinciannya adalah sebagai berikut :")

    with st.container():
        col1, col2 = st.columns((0.2, 0.8))
        with col1:
            st.image("pondok.png", width=130, caption='Logo Pesantren')
        with col2:
            st.write("2015 - Sekarang")
            st.header("Sekretaris Pesantren Al Bukhori")
            st.write("*Bertugas melakukan pendataan santri, persuratan, EMIS Pesantren dan berbagai Berkas Administrasi Pesantren lainnya.*")
    with st.container():
        st.write("---")
        col1, col2 = st.columns((0.2, 0.8))
        with col1:
            st.image("isim.png", width=130, caption='Logo ISIM')
        with col2:
            st.write("2018 - 2019")
            st.header("Mandataris FPS ISIM Masa Bhakti 2018-2019")
            st.write("*Bertanggungjawab atas kegiatan Madrasah selama Masa Bhakti.*")
    with st.container():
        st.write("---")
        col1, col2 = st.columns((0.2, 0.8))
        with col1:
            st.image("pmr.png", width=100, caption='Logo PMR Wira')
        with col2:
            st.write("2016 - 2018")
            st.header("Anggota PMR Wira MA Plus Al Bukhori")
            st.write("*Mengikuti ekstrakulikuler Palang Merah Remaja Wira MA Plus Al Bukhori.*")
    with st.container():
        st.write("---")
        col1, col2 = st.columns((0.2, 0.8))
        with col1:
            st.image("jurnalis.png", width=130, caption='Ilustrasi Jurnalis')
        with col2:
            st.write("2016 - 2018")
            st.header("Pemimpin Redaksi Plural Yayasan Al Bukkhori")
            st.write("*Mengatur jalannya Penerbitan Bulletin Plural Yayasan Al Bukhori*")
    with st.container():
        st.write("---")
        col1, col2 = st.columns((0.2, 0.8))
        with col1:
            st.image("ma.png", width=130, caption='Logo MA')
        with col2:
            st.write("2019 - Sekarang")
            st.header("Tim Tata Usaha MA Plus Al Bukhori")
            st.write("*Membantu Waka Kurikulum dalam menjalankan tugas Kurikulum di MA Plus Al Bukhori*")

with tab4:
    st.title("HUBUNGI SAYA")
    with st.container():
        st.subheader("Sosial Media Saya")
        st.write("Berikut ini Daftar Media Sosial saya yang bisa dihubungi :")
        fb, ig, twitter, yutub, wa = st.columns(5, gap="small")
        with fb:
            st.image("image.png", width=100, caption='@kalemajabro')
        with ig:
            st.image("instagram.png", width=97, caption='@ahsanjpr')
        with twitter:
            st.image("tw.png", width=100, caption='@ahsanaljaffary')  
        with yutub:
            st.image("youtube.png", width=100, caption='@ahsanaljaffary8577')
        with wa:
            st.image("whatsapp.png", width=100, caption='0882003071960')
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("---")
            st.subheader("Atau bisa hubungi saya dengan mengisi kolom dibawah ini:")

            contact_form = """
            <form action="https://formsubmit.co/ahsanaljaffary.02@email.com" method="POST">
                <input type="hidden" name="_captca" value="false">
                <input type="text" name="name" placeholder="Masukkan Nama" required>
                <input type="email" name="email" placeholder="Masukkan Email"required>
                <textarea name="message" placeholder="Pesanmu disini" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)
        with col2:
            st.empty()
