import xml
import xml.etree
import xml.etree.ElementTree as ET
import rich
from pathlib import Path


def str_to_float(price: str) -> float:
    return float(price.replace(",", "."))


def get_invoice_rows(filepath) -> list[ET.Element]:
    tree = ET.parse(filepath)
    xml_tree = tree.getroot()
    return xml_tree.findall("./LIST_DOKUMENT/DOKUMENT/LIST_POZYCJE/POZYCJE")


def code_for(invoice_row: ET.Element) -> str:
    return invoice_row.find("KOD_TOWARU").text


def quantity_for(invoice_row: ET.Element) -> int:
    qty: str = invoice_row.find("ILE").text
    return int(qty)


def price_for(invoice_row: ET.Element):
    price: str = invoice_row.find("TOW_CEN_BON").text
    return str_to_float(price)


if __name__ == "__main__":
    result = []
    # filepath = Path(__file__).parent / "tests" / "data" / "autos_invoice.xml"
    filepath = "/mnt/c/users/tarmos/koik/FUEX_8121_CN_2024.xml"
    for row in get_invoice_rows(filepath):
        result.append(
            {
                "code": code_for(row),
                "qty": quantity_for(row),
                "price": price_for(row),
            }
        )

    rich.print(result)
