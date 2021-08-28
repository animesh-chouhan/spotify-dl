import requests

URL = "https://api.spotify.com/v1/me/player"

header = {"Authorization": "Bearer BQBlPS_XLG_E3GBvMlHFDH1N1KgNwGdx1LFh4sliusSTFxl4zOoi_tLOu6vqJhtUYIe6Osixi8GSFaqzDAflP39KejFmctKVMsliCtVo9htfrMouOt1ix_kUJsmghjZFfqKFp0TN9N6NmZKHkR0PPNWz2upTX_Nq2NGvDaI2mpk"}

response = requests.get(URL, headers=header)
# json = response.json()
print(response.text)


# external_url = json["item"]["album"]["external_urls"]["spotify"]
# print(external_url)
