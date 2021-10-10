from os import name
import requests
import json
import ctypes
import time


parent_dir = "C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\python\\tokpedz\\1_query_get_product_store\\"

f = open(parent_dir + "1_kode_toko.txt", 'r+', encoding='utf-8-sig')
importKodeToko = [line for line in f.read().splitlines()]
f.close()

if len(importKodeToko) > 0: #if list in notepad not null

  hitung = range(len(importKodeToko)) #count all list of kode_toko

  for i in hitung: #will iterate as many as the counted list
    trigger = True #set trigger. Because store have more than 240items. So we need to loop until no data could be fetch. 
    page_iterate = 1 #for page iterating

    while trigger == True:

      headers = {
          'content-type': 'application/json',
      }

      data = {
          "operationName": "ShopProducts",
          "variables": {
              "sid": "652660",
              "page": 8,
              "perPage": 240,
              "etalaseId": "etalase",
              "sort": 1
          },
          "query": "query ShopProducts($sid: String!, $page: Int, $perPage: Int, $keyword: String, $etalaseId: String, $sort: Int, $user_districtId: String, $user_cityId: String, $user_lat: String, $user_long: String) {\n  GetShopProduct(shopID: $sid, filter: {page: $page, perPage: $perPage, fkeyword: $keyword, fmenu: $etalaseId, sort: $sort, user_districtId: $user_districtId, user_cityId: $user_cityId, user_lat: $user_lat, user_long: $user_long}) {\n    status\n    errors\n    links {\n      prev\n      next\n      __typename\n    }\n    data {\n      name\n      product_url\n      product_id\n      price {\n        text_idr\n        __typename\n      }\n      primary_image {\n        original\n        thumbnail\n        resize300\n        __typename\n      }\n      flags {\n        isSold\n        isPreorder\n        isWholesale\n        isWishlist\n        __typename\n      }\n      campaign {\n        discounted_percentage\n        original_price_fmt\n        start_date\n        end_date\n        __typename\n      }\n      label {\n        color_hex\n        content\n        __typename\n      }\n      label_groups {\n        position\n        title\n        type\n        url\n        __typename\n      }\n      badge {\n        title\n        image_url\n        __typename\n      }\n      stats {\n        reviewCount\n        rating\n        __typename\n      }\n      category {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
      }

      data["variables"]["sid"] = importKodeToko[i] #will gonna use this for kode toko
      data["variables"]["page"] = page_iterate #will gonna use this for looping page

      response = requests.post('https://gql.tokopedia.com/',
                              headers=headers, data=json.dumps(data))
      print("Now processing: " + importKodeToko[i] + " page: " + str(page_iterate))
      print(response.status_code, response.reason)
      # print(response.text)
      # print(type(response))

      parsed = json.loads(response.text)
      print(type(parsed))

      dir_tulis = parent_dir + "_result\\"
      nameJson = importKodeToko[i] + "_" + str(page_iterate) + ".json"

      nameSimpanJson = dir_tulis + nameJson  

      if len(parsed["data"]["GetShopProduct"]["data"]) == 0: #will gonna use this for page checking, get data or not?
        print("Cancel to write page: " + str(page_iterate) + "\nEmpty data.")
        trigger = False
      
      else:
        with open(nameSimpanJson, 'w', encoding='utf-8') as f:
          parsed = json.loads(response.text)
          json.dump(parsed, f, ensure_ascii=False, indent=4)
          print("\nFile written!")

        page_iterate = page_iterate + 1 #cycle to the next page

else: #if empty list
  ctypes.windll.user32.MessageBoxW(0, "List kosong! Mohon check kembali ya", "Error", 0)

exportSukses = "Done!!!"
ctypes.windll.user32.MessageBoxW(0, exportSukses, "Exported", 0)

#def getStoreCode():
  