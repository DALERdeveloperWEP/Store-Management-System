from rich.console import Console
from rich.table import Table
# TODO: from app.IsValid import is_valid_product

console = Console()


def add_product(products: list) -> None:
    """Mahsulot qo'shish.

    Args:
        products (list): Mahsulotlar ro'yxati (har bir mahsulot dict yoki obyekt).

    Behavior to implement:
        - Foydalanuvchidan mahsulot nomi, narxi, miqdori va kerakli maydonlarni so'raydi.
        - Yangi mahsulotni `products` ro'yxatiga qo'shadi.
        - Qo'shish muvaffaqiyati yoki xatolik haqida qaytaradi yoki log qiladi.
    """
    
    getProductCode = int(input("Mahsulot code: ").strip())
    
    for getCode in products:
        if int(getProductCode) == getCode[0]:
            console.print("Bunday kodda mahsulot mavjud.", style="bold red")
            return

    getProductName = input("Mahsulot Nomi: ")
    getProductPrice = float(input("Mahsulot Narxi: "))
    getProductQuantity = float(input("Mahsulot Miqdori: "))


    products.append([getProductCode,getProductName, float(getProductPrice), float(getProductQuantity)])
    console.print("Mahsulot Qo'shildi!", style="bold green")

    ## TODO: Keyinchalik korib chiqiladi
    # if is_valid_product([getProductCode,getProductName, getProductPrice, getProductQuantity]):
    #     products.append([getProductCode,getProductName, float(getProductPrice), float(getProductQuantity)])
    #     console.print("Mahsulot Qo'shildi!", style="bold green")
    # else:
    #     console.print("Siz notogri mahsulot Kiritdingiz", style="bold red")

    #     if not getProductName.isalpha():
    #         console.print("Iltimos mahsulot nomini harf korinishda yozin: Sut", style="yellow")
    #     if not getProductPrice.isdigit():
    #         console.print(f"Iltimos mahsulot narxini raqam korinishda yozin: {12_000}", style="yellow")
    #     if not getProductQuantity.isdigit():
    #         console.print(f"Iltimos mahsulot miqdorini raqam korinishda yozin (Dona/kg): {12}", style="yellow")
