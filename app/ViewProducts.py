from rich.console import Console
from rich.table import Table

console = Console()

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
    product_table.add_column("Mahsulot code", style="green", justify="center")
    product_table.add_column("Nomi", style="yellow")
    product_table.add_column("Narxi", style="grey100")
    product_table.add_column("Miqdori (Dona/Kg)", style="grey100", justify="right")

    for index, l in enumerate(products, start=1):
        product_table.add_row(str(index), str(l[0]), l[1], str(l[2]), str(l[3]))
    console.print(product_table)
