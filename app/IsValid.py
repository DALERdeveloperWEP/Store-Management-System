# TODO: Keyinchalik korib chiqiladi
def is_valid_product(products: list) -> bool:
    # [code, name, price, count]
    if (products[2].isdigit() # FIXME: mahsulotda pul kiritishda muamo boladi (sabab: isdigit faqat 13421 tekshiradi agar pul 12.12 kiritsa unda error)
        and products[3].isdigit()):
        return True
    else:
        return False
