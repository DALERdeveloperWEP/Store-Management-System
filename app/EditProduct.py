from rich.console import Console

console = Console()


def edit_product(products: list) -> None:
    """Mahsulotni tahrirlash.

    Args:
        products (list): Mahsulotlar ro'yxati.
        product_id: Tahrirlanishi kerak bo'lgan mahsulot identifikatori (index yoki id).

    Behavior to implement:
        - Berilgan `product_id` bo'yicha mahsulotni topadi.
        - Foydalanuvchidan yangilanish kerak bo'lgan maydonlarni oladi va o'zgartiradi.
        - O'zgartirish muvaffaqiyati/hatolik xabarini beradi.
    """
    getProductCode = int(input("Mahsulot kodini kiring: "))
    for index, getCode in enumerate(products, start=0):
        if str(getProductCode) not in getCode:
            console.print("Bunday kodda mahsulot mavjud emas.", style="bold red")
            return
        else:
            getProductName = input("Mahsulot Nomi: ")
            getProductPrice = float(input("Mahsulot Narxi: "))
            getProductQuantity = float(input("Mahsulot Miqdori: "))

            products.append({ getProductCode: [getProductName, float(getProductPrice), float(getProductQuantity)]})
            console.print("Mahsulot Qo'shildi!", style="bold green")

    
