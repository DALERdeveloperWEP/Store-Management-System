# DO'KON BOSHQARUV - Funktsiyalar skeleti
# Har bir funktsiyaning tanasida faqat docstring va pass mavjud bo'ladi.

from rich.console import Console
from rich.table import Table
import sys

console = Console()

def show_menu():
    table = Table(title="DO'KON BOSHQARUV", title_style="bold white on blue",)

    table.add_column("№", style="blue")
    table.add_column("Name", style="yellow")

    table.add_row("1", "Mahsulot qo'shish")
    table.add_row("2", "Mahsulotlarni ko'rish")
    table.add_row("3", "Mahsulotni tahrirlash")
    table.add_row("4", "Mahsulot o'chirish")
    table.add_row("5", "Sotuv (kirim)")
    table.add_row("6", "Xarid (chiqim / zaxiraga qo'shish)")
    table.add_row("7", "Tranzaksiyalarni ko'rish")
    table.add_row("8", "Hisobot (jami)")
    table.add_row("9", "Tranzaksiyalarni CSV ga eksport")
    table.add_row("0", "Chiqish")

    console.print(table)


def is_valid_product(products: list) -> bool:
    if (products[1].isdigit() 
        and products[2].isdigit()):
        return True
    else:
        return False
        


def add_product(products: list) -> None:
    """Mahsulot qo'shish.

    Args:
        products (list): Mahsulotlar ro'yxati (har bir mahsulot dict yoki obyekt).

    Behavior to implement:
        - Foydalanuvchidan mahsulot nomi, narxi, miqdori va kerakli maydonlarni so'raydi.
        - Yangi mahsulotni `products` ro'yxatiga qo'shadi.
        - Qo'shish muvaffaqiyati yoki xatolik haqida qaytaradi yoki log qiladi.
    """
    getProductName = input("Mahsulot Nomi: ")
    getProductPrice = input("Mahsulot Narxi: ")
    getProductQuantity = input("Mahsulot Miqdori: ")

    if is_valid_product([getProductName, getProductPrice, getProductQuantity]):
        console.print("Mahsulot Qo'shildi!", style="bold green")
        products.append( [getProductName, float(getProductPrice), float(getProductQuantity)] )
    else:
        console.print("Siz notogri mahsulot Kiritdingiz", style="bold red")

        if not getProductName.isalpha():
            console.print("Iltimos mahsulot nomini harf korinishda yozin: Sut", style="yellow")
        if not getProductPrice.isdigit():
            console.print(f"Iltimos mahsulot narxini raqam korinishda yozin: {12_000}", style="yellow")
        if not getProductQuantity.isdigit():
            console.print(f"Iltimos mahsulot miqdorini raqam korinishda yozin (Dona/kg): {12}", style="yellow")

def view_products(products: list) -> None:
    """Mahsulotlarni ko'rish.

    Args:
        products (list): Mahsulotlar ro'yxati.

    Behavior to implement:
        - Ro'yxatdagi mahsulotlarni chiroyli formatda chiqaradi (jadval yoki ro'yxat).
        - Agar mahsulotlar yo'q bo'lsa, mos xabar beradi.
    """
    product_table = Table(title="Mahsulotlar", title_style="bold blue on plum2")
    # product_table = Table(title="Mahsulotlar", title_style="bold red on blue")

    product_table.add_column("№", style="blue")
    product_table.add_column("Nomi", style="yellow")
    product_table.add_column("Narxi", style="grey100")
    product_table.add_column("Miqdori (Dona/Kg)", style="grey100")

    for index, l in enumerate(products, start=1):
        product_table.add_row(str(index), l[0], str(l[1]), str(l[2]))
    console.print(product_table)


def edit_product(products: list, product_id) -> None:
    """Mahsulotni tahrirlash.

    Args:
        products (list): Mahsulotlar ro'yxati.
        product_id: Tahrirlanishi kerak bo'lgan mahsulot identifikatori (index yoki id).

    Behavior to implement:
        - Berilgan `product_id` bo'yicha mahsulotni topadi.
        - Foydalanuvchidan yangilanish kerak bo'lgan maydonlarni oladi va o'zgartiradi.
        - O'zgartirish muvaffaqiyati/hatolik xabarini beradi.
    """
    pass


def delete_product(products: list, product_id) -> None:
    """Mahsulotni o'chirish.

    Args:
        products (list): Mahsulotlar ro'yxati.
        product_id: O'chirilishi kerak bo'lgan mahsulot identifikatori.

    Behavior to implement:
        - Mahsulotni ro'yxatdan o'chiradi (yoki `archived` flag qo'yadi).
        - O'chirishdan oldin tasdiqlash so'ralishi mumkin.
        - Natija haqida xabar beradi.
    """
    pass


def sell_product(products: list, transactions: list, product_id, quantity: int) -> None:
    """Sotuv (kirim).

    Args:
        products (list): Mahsulotlar ro'yxati.
        transactions (list): Tranzaksiyalar ro'yxati, yangi tranzaksiya shu yerga qo'shiladi.
        product_id: Sotilishi kerak bo'lgan mahsulot identifikatori.
        quantity (int): Sotilayotgan miqdor.

    Behavior to implement:
        - Mahsulot mavjudligini va yetarli zaxirani tekshiradi.
        - Miqdorni kamaytiradi va tranzaksiya yozuvi qo'shadi (sana, narx, jami, tur="sale").
        - Agar zaxira yetarli bo'lmasa, xatolik yoki ogohlantirish beradi.
    """
    pass


def purchase_product(products: list, transactions: list, product_id, quantity: int, cost: float) -> None:
    """Xarid (chiqim / zaxiraga qo'shish).

    Args:
        products (list): Mahsulotlar ro'yxati.
        transactions (list): Tranzaksiyalar ro'yxati.
        product_id: Xarid qilinadigan mahsulot identifikatori.
        quantity (int): Qo'shilayotgan miqdor.
        cost (float): Bir birlik uchun xarid narxi yoki umumiy xarajat.

    Behavior to implement:
        - Mahsulotni zaxiraga qo'shadi yoki yangi mahsulot sifatida yaratadi.
        - Tranzaksiya yozuvi qo'shadi (sana, narx, jami, tur="purchase").
        - Hisob-kitob va muomala loglarini yangilaydi.
    """
    pass


def view_transactions(transactions: list) -> None:
    """Tranzaksiyalarni ko'rish.

    Args:
        transactions (list): Tranzaksiyalar ro'yxati.

    Behavior to implement:
        - Barcha tranzaksiyalarni yoki filtrlanganlarni (sana, tur, mahsulot) ko'rsatadi.
        - Tranzaksiyalarni tartiblash (so'nggi birinchi) va qidirish imkoniyati bo'lishi mumkin.
    """
    pass


def report_total(products: list, transactions: list) -> dict:
    """Hisobot (jami).

    Args:
        products (list): Mahsulotlar ro'yxati.
        transactions (list): Tranzaksiyalar ro'yxati.

    Returns:
        dict: Umumiy hisobot ma'lumotlari, masalan {"total_sales": float, "total_purchases": float, "inventory_value": float}

    Behavior to implement:
        - Sotuvlar va xaridlarning umumiy summasini hisoblaydi.
        - Joriy zaxiraning umumiy qiymatini hisoblaydi.
        - Kerak bo'lsa, to'liq breakdown (mahsulot bo'yicha) qaytaradi.
    """
    pass


def export_transactions_csv(transactions: list, filepath: str) -> None:
    """Tranzaksiyalarni CSV ga eksport.

    Args:
        transactions (list): Tranzaksiyalar ro'yxati.
        filepath (str): Saqlash yo'li (masalan 'transactions.csv').

    Behavior to implement:
        - Tranzaksiyalarni CSV formatiga serialize qiladi va `filepath` ga yozadi.
        - Fayl yozilishidagi xatoliklarni tutib, mos xabar beradi.
    """
    pass


def exit_app() -> None:
    """Chiqish.

    Behavior to implement:
        - Dasturdan chiqish oldidan kerakli saqlash va tozalash ishlarini bajaradi.
        - Foydalanuvchiga tasdiqlash so'rashi mumkin.
    """
    pass


def main() -> None:
    """Asosiy menyu va boshqaruv oqimini ishlatish.

    Behavior to implement:
        - Mahsulotlar va tranzaksiyalar uchun bo'sh ro'yxatlar yaratadi.
        - Menyuni ko'rsatadi va foydalanuvchidan tanlov oladi.
        - Tanlovga qarab tegishli funksiyani chaqiradi.
        - 0 ni tanlasa, `exit_app()` funksiyasini chaqiradi va dasturdan chiqadi.
        - Noto'g'ri tanlovda ogohlantirish chiqaradi.
    """
    pass

    products: list[ list[str, str, str] ] = [
        ["Sut", 12121342, 23234123]
    ]

    while True:
        show_menu()

        choice = input("Amal tanlen: ")

        if choice.isdigit():
            if choice == '1':add_product(products)
            if choice == '2':view_products(products)
            if choice == '3':edit_product(products)
            if choice == '4':delete_product(products)
            if choice == '5':sell_product(products)
            if choice == '6':purchase_product(products)
            if choice == '7':view_transactions(products)
            if choice == '8':report_total(products)
            if choice == '9':export_transactions_csv(products)
            if choice == '0':sys.exit()

main()