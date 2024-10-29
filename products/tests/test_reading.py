import xml.etree.ElementTree as ET
import pytest
from pathlib import Path
import pdb
from products import autos_xml_invoice


@pytest.fixture(scope="session")
def xml_file():
    file_path = Path(__file__).parent / "data" / "autos_invoice.xml"
    return file_path


@pytest.fixture(scope="session")
def xml_tree(xml_file) -> ET.Element:
    tree = ET.parse(xml_file)
    return tree.getroot()


@pytest.fixture(scope="session")
def invoice_rows(xml_tree) -> ET.Element:
    return xml_tree.findall("./LIST_DOKUMENT/DOKUMENT/LIST_POZYCJE/POZYCJE")


# "KOD_TOWARU",
# "TOW_KOD",
# "ILE",
# "NR_KAT",
# "NR_D",
# "TOW_NAZ_KONW",
# "TOW_CEN_BON",
def test_get_invoice_rows(xml_file):
    invoice_rows = autos_xml_invoice.get_invoice_rows(xml_file)
    assert len(invoice_rows) == 2


def test_code_for(invoice_rows):
    invoice_row = invoice_rows[0]
    assert autos_xml_invoice.code_for(invoice_row) == "0002965"


def test_quantity_for(invoice_rows):
    invoice_row = invoice_rows[0]
    assert autos_xml_invoice.quantity_for(invoice_row) == "5"


def test_price_for(invoice_rows):
    invoice_row = invoice_rows[0]
    assert autos_xml_invoice.price_for(invoice_row) == "19999,00"
