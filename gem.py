import time
import random

# ASCII Art
PEDANG = r"""
    /\_/\
   ( o.o )
    > ^ <
   /|   |\
  (_|   |_)
🗡️  ANDA MENANG! 🗡️
"""

TENGKORAK = r"""
    ☠️  SKULL  ☠️
   (o  )  (  o)
    \ • /
     \_/
     | |
    /| |\
   | | | |
  🏴 ANDA KALAH! 🏴
"""

# Tantangan untuk Lembah Coding
TANTANGAN_LEMBAH = {
    "tutorial": {
        "nama": "📚 TUTORIAL DASAR",
        "cerita": "Anda masuk ke perpustakaan kode dengan tutorial Python dasar.",
        "pertanyaan": "Apa output dari: print('Hello' + ' World')?",
        "jawaban_benar": ["hello world", "hello  world"],
        "hint": "Gunakan operator + untuk string concatenation",
        "hadiah": 15
    },
    "latihan": {
        "nama": "🎯 LATIHAN SOAL",
        "cerita": "Anda menemukan papan soal coding yang menantang.",
        "pertanyaan": "Berapa hasil dari: 2 ** 3 (2 pangkat 3)?",
        "jawaban_benar": ["8"],
        "hint": "** adalah operator pangkat di Python",
        "hadiah": 20
    },
    "mentor": {
        "nama": "👨‍💼 MENTOR BERPENGALAMAN",
        "cerita": "Anda bertemu dengan mentor berpengalaman yang siap membimbing.",
        "pertanyaan": "Apa nama struktur data yang menyimpan pasangan key-value?",
        "jawaban_benar": ["dictionary", "dict"],
        "hint": "Dalam Python, struktur ini menggunakan { }",
        "hadiah": 25
    }
}

# Tantangan untuk Gunung Bug
TANTANGAN_GUNUNG = {
    "debug_simple": {
        "nama": "🐛 DEBUG SEDERHANA",
        "cerita": "Anda menemukan kode dengan bug kecil yang mudah diperbaiki.",
        "pertanyaan": "Perbaiki: x = 10, jika ingin x berkurang 5, perintah apa yang benar?",
        "jawaban_benar": ["x = x - 5", "x -= 5", "x=x-5"],
        "hint": "Gunakan operator -= atau pengurangan biasa",
        "hadiah": 0
    },
    "debug_complex": {
        "nama": "🔴 DEBUG KOMPLEKS",
        "cerita": "Anda menghadapi logika kode yang sangat rumit dan membingungkan.",
        "pertanyaan": "Apa output dari: print(len('Python'))?",
        "jawaban_benar": ["6"],
        "hint": "Hitung jumlah karakter dalam string 'Python'",
        "hadiah": 0
    },
    "race_time": {
        "nama": "⏱️ BALAP WAKTU",
        "cerita": "Anda harus menemukan dan memperbaiki bug dalam waktu terbatas!",
        "pertanyaan": "List comprehension dengan 1 karakter pertama: [x[0] for x in ['apple', 'banana']]",
        "jawaban_benar": ["['a', 'b']"],
        "hint": "Ambil karakter pertama (index 0) dari setiap string",
        "hadiah": 0
    }
}

def tampilkan_teks(text):
    """Fungsi untuk menampilkan teks dengan jeda 0.5 detik"""
    print(text)
    time.sleep(0.5)

def tampilkan_status(nama, nyawa, skor=0):
    """Tampilkan status pemain"""
    tampilkan_teks(f"\n{'='*50}")
    tampilkan_teks(f"Nama: {nama} | Nyawa: {nyawa} ❤️ | Skor: {skor} ⭐")
    tampilkan_teks(f"{'='*50}\n")

def pilih_jalur_utama():
    """Pemain memilih jalur utama"""
    tampilkan_teks("═" * 50)
    tampilkan_teks("Anda memasuki persimpangan jalan di dunia pemrograman...")
    tampilkan_teks("Ada dua pilihan di hadapan Anda:\n")
    tampilkan_teks("1️⃣  LEMBAH CODING 🏞️ - Jalur aman, penuh belajar dan latihan")
    tampilkan_teks("2️⃣  GUNUNG BUG 🏔️ - Jalur berbahaya, penuh error yang mengganggu\n")
    
    while True:
        pilihan = input("Pilih jalur (1 atau 2): ").strip()
        if pilihan in ['1', '2']:
            return pilihan
        else:
            tampilkan_teks("❌ Input tidak valid! Pilih 1 atau 2.")

def pilih_cabang_lembah():
    """Memilih cabang di Lembah Coding"""
    tampilkan_teks("\n🏞️  Anda memasuki LEMBAH CODING...")
    tampilkan_teks("Tiga jalan terbentang di hadapan Anda:\n")
    tampilkan_teks("A) 📚 TUTORIAL DASAR - Belajar fundamental pemrograman")
    tampilkan_teks("B) 🎯 LATIHAN SOAL - Mengerjakan soal-soal programming")
    tampilkan_teks("C) 👨‍💼 MENTOR BERPENGALAMAN - Berdiskusi dengan mentor hebat\n")
    
    while True:
        pilihan = input("Pilih cabang (A, B, atau C): ").strip().upper()
        if pilihan in ['A', 'B', 'C']:
            if pilihan == 'A':
                return 'tutorial'
            elif pilihan == 'B':
                return 'latihan'
            else:
                return 'mentor'
        else:
            tampilkan_teks("❌ Input tidak valid! Pilih A, B, atau C.")

def pilih_cabang_gunung():
    """Memilih cabang di Gunung Bug"""
    tampilkan_teks("\n🏔️  Anda memasuki GUNUNG BUG...")
    tampilkan_teks("Tiga terusan berbahaya terbentang di hadapan Anda:\n")
    tampilkan_teks("A) 🐛 DEBUG SEDERHANA - Bug kecil tapi mengecewakan")
    tampilkan_teks("B) 🔴 DEBUG KOMPLEKS - Error yang sangat rumit")
    tampilkan_teks("C) ⏱️  BALAP WAKTU - Perbaiki bug sebelum time out!\n")
    
    while True:
        pilihan = input("Pilih terusan (A, B, atau C): ").strip().upper()
        if pilihan in ['A', 'B', 'C']:
            if pilihan == 'A':
                return 'debug_simple'
            elif pilihan == 'B':
                return 'debug_complex'
            else:
                return 'race_time'
        else:
            tampilkan_teks("❌ Input tidak valid! Pilih A, B, atau C.")

def proses_tantangan(tantangan_dict):
    """Proses tantangan dan berikan feedback"""
    tampilkan_teks(f"\n{tantangan_dict['nama']}")
    tampilkan_teks("═" * 50)
    tampilkan_teks(tantangan_dict['cerita'])
    time.sleep(1)
    
    tampilkan_teks(f"\n❓ {tantangan_dict['pertanyaan']}")
    tampilkan_teks(f"💡 Hint: {tantangan_dict['hint']}")
    
    jawaban = input("\n🎯 Jawaban Anda: ").strip().lower()
    
    # Cek jawaban
    jawaban_benar = [j.lower() for j in tantangan_dict['jawaban_benar']]
    
    if jawaban in jawaban_benar:
        tampilkan_teks("\n✅ JAWABAN BENAR!")
        tampilkan_teks(f"⭐ Anda mendapat +{tantangan_dict['hadiah']} bonus skor!")
        return tantangan_dict['hadiah'], 0  # Bonus, tidak berkurang nyawa
    else:
        tampilkan_teks("\n❌ JAWABAN SALAH!")
        tampilkan_teks(f"Jawaban yang benar: {berikan_jawaban_acak(tantangan_dict)}")
        tampilkan_teks("💔 Nyawa berkurang 15!")
        return 0, 15  # Tidak ada bonus, nyawa berkurang

def berikan_jawaban_acak(tantangan_dict):
    """Berikan satu jawaban yang benar"""
    return random.choice(tantangan_dict['jawaban_benar'])

def proses_lembah_coding(nama, nyawa, skor, cabang):
    """Proses perjalanan di Lembah Coding"""
    tantangan = TANTANGAN_LEMBAH[cabang]
    bonus, nyawa_berkurang = proses_tantangan(tantangan)
    
    skor += bonus
    nyawa -= nyawa_berkurang
    
    # Keberuntungan tambahan di Lembah
    if random.random() < 0.3:
        tampilkan_teks("\n✨ BONUS: Anda menemukan ekstra nyawa!")
        nyawa = min(100, nyawa + 10)
        tampilkan_teks("Nyawa +10")
    
    return nyawa, skor

def proses_gunung_bug(nama, nyawa, skor, cabang):
    """Proses perjalanan di Gunung Bug"""
    tantangan = TANTANGAN_GUNUNG[cabang]
    bonus, nyawa_berkurang = proses_tantangan(tantangan)
    
    skor += bonus
    nyawa -= nyawa_berkurang
    
    # Di Gunung Bug, kesalahan lebih berat
    if nyawa_berkurang > 0:
        dampak_tambahan = random.randint(5, 10)
        nyawa -= dampak_tambahan
        tampilkan_teks(f"\n⚡ ERROR KRITIS! Nyawa berkurang tambahan {dampak_tambahan}!")
    
    return nyawa, skor

def game_utama():
    """Fungsi utama game"""
    while True:  # Game loop untuk main lagi
        tampilkan_teks("\n" + "🎮 " * 15)
        tampilkan_teks("PETUALANGAN PROGRAMMER PEMULA")
        tampilkan_teks("🎮 " * 15)
        
        nama = input("\n👤 Siapa namamu? ").strip()
        if not nama:
            nama = "Programmer Misterius"
        
        nyawa = 100
        skor = 0
        putaran = 1
        
        tampilkan_teks(f"\n🎯 Selamat datang, {nama}!")
        tampilkan_teks("Mulailah petualanganmu di dunia pemrograman...")
        time.sleep(1)
        
        # Game loop - pemain bermain sampai nyawa habis
        while nyawa > 0:
            tampilkan_status(nama, nyawa, skor)
            tampilkan_teks(f"📍 PUTARAN {putaran}\n")
            
            # Pilih jalur utama
            jalur = pilih_jalur_utama()
            
            if jalur == '1':
                # Lembah Coding
                cabang = pilih_cabang_lembah()
                nyawa, skor = proses_lembah_coding(nama, nyawa, skor, cabang)
            else:
                # Gunung Bug
                cabang = pilih_cabang_gunung()
                nyawa, skor = proses_gunung_bug(nama, nyawa, skor, cabang)
            
            nyawa = max(0, nyawa)  # Nyawa tidak boleh negatif
            putaran += 1
            time.sleep(1)
        
        # Game selesai
        tampilkan_teks("\n" + "="*50)
        if skor >= 50:
            tampilkan_teks("🎉 SELAMAT! ANDA TELAH MENYELESAIKAN PETUALANGAN! 🎉")
            print(PEDANG)
            tampilkan_teks(f"Total Putaran: {putaran - 1}")
            tampilkan_teks(f"Skor Akhir: {skor} ⭐")
        else:
            tampilkan_teks("😢 GAME OVER! NYAWA ANDA HABIS! 😢")
            print(TENGKORAK)
            tampilkan_teks(f"Putaran Bertahan: {putaran - 1}")
            tampilkan_teks(f"Skor Akhir: {skor} ⭐")
        
        tampilkan_teks("="*50)
        
        # Pertanyaan main lagi
        time.sleep(1)
        main_lagi = input("\n🎮 Main lagi? (y/n): ").strip().lower()
        if main_lagi != 'y':
            tampilkan_teks("\n👋 Terima kasih telah bermain!")
            tampilkan_teks("Sampai jumpa lagi, Programmer! 🚀")
            break
        
if __name__ == "__main__":
    game_utama()