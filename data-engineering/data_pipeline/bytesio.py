import requests
from io import BytesIO
from zipfile import ZipFile

url = "https://www.ers.usda.gov/webdocs/DataFiles/81475/LivestockMeatTrade.zip"

try:
    response = requests.get(url)
except:  # noqa: E722
    print("Problem downloading zip file.")
if response.status_code == 200:
    in_memory_zip = BytesIO(response.content)
    with ZipFile(in_memory_zip) as zippy:
        for item in zippy.infolist():
            if "Exports" in item.filename:
                with zippy.open(item.filename) as export_file:
                    for row in export_file:
                        print(row.decode("utf-8"))
