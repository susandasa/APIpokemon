import requests
import json

# Ambil data dari REST API
url_api = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url_api)

# Periksa apakah permintaan berhasil
if response.status_code == 200:
    data_api = response.json()

    # Simpan data ke file .json
    with open("Pokemon-API.json", "w") as file:
        json.dump(data_api, file)
        print("Data berhasil disimpan ke file lokal.")
else:
    print(f"Gagal mengambil data. Kode status: {response.status_code}")
