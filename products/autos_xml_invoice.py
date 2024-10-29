import xml
import xml.etree
import xml.etree.ElementTree as ET


def get_invoice_rows(filepath) -> list[ET.Element]:
    tree = ET.parse(filepath)
    xml_tree = tree.getroot()
    return xml_tree.findall("./LIST_DOKUMENT/DOKUMENT/LIST_POZYCJE/POZYCJE")


def code_for(invoice_row: ET.Element) -> str:
    return invoice_row.find("KOD_TOWARU").text


def quantity_for(invoice_row: ET.Element):
    return invoice_row.find("ILE").text


def price_for(invoice_row: ET.Element):
    return invoice_row.find("TOW_CEN_BON").text
