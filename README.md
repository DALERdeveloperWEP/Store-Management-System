# Store-Management-System

## 🏪 Do‘kon Boshqaruv Tizimi

Bu oddiy **do‘kon mahsulot boshqaruv dasturi** bo‘lib, Python tilida yozilgan.  
Dastur orqali siz mahsulotlarni, zaxirani, sotuv va xaridlarni boshqarishingiz mumkin.  
Barcha ma’lumotlar **JSON** faylga saqlanadi va tranzaksiyalarni **CSV** faylga eksport qilish mumkin.

---
## 📋 Menu
```
=== DO'KON BOSHQARUV ===

 1. Mahsulot qo'shish
 2. Mahsulotlarni ko'rish
 3. Mahsulotni tahrirlash
 4. Mahsulot o'chirish
 5. Sotuv (kirim)
 6. Xarid (chiqim / zaxiraga qo'shish)
 7. Tranzaksiyalarni ko'rish
 8. Hisobot (jami)
 9. Tranzaksiyalarni CSV ga eksport
 0. Chiqish
```

---

## 📖 Menyudagi bo‘limlar

### 1. Mahsulot qo‘shish
Do‘konga yangi mahsulot qo‘shish (nomi, narxi, boshlang‘ich miqdori).

### 2. Mahsulotlarni ko‘rish
Barcha mahsulotlarni jadval shaklida ko‘rish (nomi, narxi, mavjud zaxirasi).

### 3. Mahsulotni tahrirlash
Tanlangan mahsulot ma’lumotlarini o‘zgartirish (narx, nom, miqdor).

### 4. Mahsulotni o‘chirish
Mahsulotni butunlay tizimdan o‘chirish.

### 5. Sotuv yozish
Sotuvni qayd etish: mahsulotdan qancha sotilgani va summasi hisoblanadi, zaxira kamayadi.

### 6. Xarid yozish
Xaridni qayd etish: mahsulot omborga qo‘shiladi (zaxira ortadi).

### 7. Tranzaksiyalarni ko‘rish
Oxirgi sotuv va xarid yozuvlarini ko‘rish (sana, mahsulot, miqdor, narx).

### 8. Hisobot
Jami sotuvlar, jami xaridlar va sof foyda haqida qisqa hisobot chiqaradi.

### 9. Tranzaksiyalarni CSV ga eksport qilish
Barcha tranzaksiyalarni **CSV** faylga saqlash (Excel’da ochib ishlatish mumkin).

### 0. Chiqish
Dasturdan chiqish.

---

## 📌 Xususiyatlari

- Mahsulot qo‘shish, ko‘rish, tahrirlash, o‘chirish

- Sotuvni qayd qilish (zaxira kamayadi)

- Xaridni qayd qilish (zaxira ortadi)

- Tranzaksiyalar tarixini ko‘rish

- Jami hisobot chiqarish (sotuv, xarid, foyda)

- CSV faylga eksport qilish imkoniyati

## 🚀 Ishga tushirish

1. Python 3.8+ o‘rnating  
2. Kodni `store_manager.py` nomi bilan saqlang  
3. Terminalda ishga tushiring:  
   ```bash
   python main.py
