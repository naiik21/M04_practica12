import json as js

"""
Funcion que utilizamos para crear el archivo json y añadirle los valores de books
"""
def json():
    books= """
    {"book":[
        {
            "titol": "El seño de los anillos",
            "Cover": "Dura",
            "year": "1954",
            "pages": "673"
        }
        {
            "titol": "TODO LO QUE NUNCA TE DIJE",
            "Cover": "Blanda",
            "year": "2019",
            "pages": "176"
        }
        {
            "titol": "Así es la puta vida",
            "Cover": "Dura",
            "year": "2022",
            "pages": "300"
        }
        {
            "titol": "Kimetsu no yaiba 2",
            "Cover": "Blanda",
            "year": "2019",
            "pages": "192"
        }
    ]}
    """
    with open("jsonFile.json", "w") as file:
        js.dump(books,file)

"""
Funcion que utilizamos para imprimir los keys y values del archivo json
"""
def imprimir():
    with open("jsonFile.json", "r") as file1:
        result = js.load(file1)
        print(result)
