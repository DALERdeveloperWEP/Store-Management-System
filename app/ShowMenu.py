from rich.console import Console
from rich.table import Table

console = Console()

def show_menu():
    table = Table(title="DO'KON BOSHQARUV", title_style="bold white on blue",)

    table.add_column("№", style="blue") 
    table.add_column("Name", style="turquoise2")

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
