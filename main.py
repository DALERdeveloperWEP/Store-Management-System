from app.ShowMenu import show_menu
from app.AddProduct import add_product
from app.ViewProducts import view_products
from app.EditProduct import edit_product
from app.DeleteProduct import delete_product
from app.SellProduct import sell_product
from app.PurchaseProduct import purchase_product
from app.ViewTransactions import view_transactions
from app.ReportTotal import report_total
from app.ExportTransactionsCSV import export_transactions_csv

import sys


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

    products: list[list[int, str, int, int]] = [
        [1221, "Sut", 12121342, 23234123],
        [1222, "limon", 12000, 1]
    ]

    while True:
        show_menu()

        choice = input("Amal tanlen: ")

        if choice.isdigit():
            if choice == '1':
                add_product(products)
            if choice == '2':
                view_products(products)
            if choice == '3':
                edit_product(products)
            if choice == '4':
                delete_product(products)
            if choice == '5':
                sell_product(products)
            if choice == '6':
                purchase_product(products)
            if choice == '7':
                view_transactions(products)
            if choice == '8':
                report_total(products)
            if choice == '9':
                export_transactions_csv(products)
            if choice == '0':
                sys.exit()


main()
