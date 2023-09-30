import random

datas = [
            {
                "id": 29467,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Outer Material",
                "value": "Synthetic",
                "product": 2
            },
            {
                "id": 29468,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Inner Material",
                "value": "Synthetic",
                "product": 2
            },
            {
                "id": 29469,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Sole",
                "value": "Rubber",
                "product": 2
            },
            {
                "id": 29470,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Closure",
                "value": "Strap",
                "product": 2
            },
            {
                "id": 29471,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Heel Height",
                "value": "2 centimetres",
                "product": 2
            },
            {
                "id": 29472,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Heel Type",
                "value": "Flat",
                "product": 2
            },
            {
                "id": 29473,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Shoe Width",
                "value": "Medium",
                "product": 2
            },
            {
                "id": 29481,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Package Dimensions",
                "value": "31.2 x 21.4 x 11.4 cm; 820 Grams",
                "product": 2
            },
            {
                "id": 29482,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Date First Available",
                "value": "22 Jun. 2020",
                "product": 2
            },
            {
                "id": 29483,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Manufacturer",
                "value": "Geox",
                "product": 2
            },
            {
                "id": 29484,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "ASIN",
                "value": "B08BLP231K",
                "product": 2
            },
            {
                "id": 29485,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Item model number",
                "value": "J1524B02214",
                "product": 2
            },
            {
                "id": 29486,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Country of origin",
                "value": "Vietnam",
                "product": 2
            },
            {
                "id": 29487,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "Department",
                "value": "Boys",
                "product": 2
            },
            {
                "id": 29474,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "images_0",
                "value": "products/B08BLP231K/41OuvqjhaqL.jpg",
                "product": 2
            },
            {
                "id": 29475,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "images_1",
                "value": "products/B08BLP231K/51zt+Bb48FL.jpg",
                "product": 2
            },
            {
                "id": 29476,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "images_2",
                "value": "products/B08BLP231K/51EXdVtkpAL.jpg",
                "product": 2
            },
            {
                "id": 29477,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "images_3",
                "value": "products/B08BLP231K/41u3T2DxWkL.jpg",
                "product": 2
            },
            {
                "id": 29478,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "images_4",
                "value": "products/B08BLP231K/41ZOt3pgbSL.jpg",
                "product": 2
            },
            {
                "id": 29479,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "images_5",
                "value": "products/B08BLP231K/41FEYlXQNFL.jpg",
                "product": 2
            },
            {
                "id": 29480,
                "creation_date": "2023-08-04T20:25:49.387509+07:00",
                "key": "images_6",
                "value": "products/B08BLP231K/41Nqt4ULBUL.jpg",
                "product": 2
            }
        ]

filtered_data = list(filter(lambda x: "images" in x["key"], datas))
random_image = random.choice(filtered_data)["value"] 

print(random_image)