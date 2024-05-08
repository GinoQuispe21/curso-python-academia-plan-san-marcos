import json

# Lectura de archivo:

with open("Archivos/jsons/example.json") as stream_json_read:
    dict_example = json.load(stream_json_read)
    #print(dict_example, type(dict_example))
    print(dict_example["correo"])
    print(dict_example["metodosPago"][0])
    print(dict_example["carritoCompra"][1])
    print(dict_example["carritoCompra"][0]["nombreProducto"])

# Escritura de archivo

data = {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipitsuscipit recusandae consequuntur expedita et cumreprehenderit molestiae ut ut quas totannostrum rerum est autem sunt rem eveniet architecto"
}

with open("Archivos/jsons/post_1.json", mode = "w") as stream_json_write:
    json.dump(data, stream_json_write, indent = 2)