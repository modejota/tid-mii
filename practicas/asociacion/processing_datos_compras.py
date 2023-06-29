import csv, sys
from tkinter import Tk, filedialog
from collections import defaultdict

# Listas de elementos agrupados por categorías de acuerdo a analisis previo
dict = {
    "pescado": ["shrimp", "salmon", "fresh tuna"],
    "carne": ["burgers", "meatballs", "turkey", "chicken", "ham", "ground beef", "escalope", "hot dogs", "bacon"],
    "verdura": ["vegetables mix", "yams", "salad", "spinach", "shallot", "pickles", "zucchini", "frozen vegetables", "tomatoes", "pepper", " asparagus", "asparagus", "carrots", "eggplant", "cauliflower", "green beans"],    # Asparagus tiene un espacio al principio
    "fruta": ["avocado", "green grapes", "strawberries", "corn", "blueberries", "melons", "bramble"],
    "lacteos": ["low fat yogurt", "frozen smoothie", "milk", "light cream", "nonfat milk", "cream", "butter"],
    "quesos": ["cottage cheese", "grated cheese", "parmesan cheese", "strong cheese", "fromage blanc"],
    "salsas_condimentos": ["tomato sauce", "light mayo", "barbecue sauce", "mayonnaise", "mushroom cream sauce", "chili", "ketchup", "burger sauce", "honey", "chutney", "herb & pepper", "flax seed", "mint", "salt"],
    "zumos": ["tomato juice", "antioxydant juice"],
    "chocolate": ["chocolate", "extra dark chocolate"],
    "postres_desayunos": ["pancakes", "cookies", "cake", "brownies", "cereals", "muffins", "yogurt cake", "chocolate bread", "oatmeal"],
    "refrescos": ["energy drink", "soda"],
    "alcohol": ["champagne", "red wine", "white wine", "cider", "french wine", "dessert wine"],
    "aceites": ["olive oil", "cooking oil", "oil"],
    "arroz": ["whole wheat rice", "rice"],
    "agua": ["mineral water", "sparkling water", "water spray"],
    "te": ["green tea", "black tea", "tea", "mint green tea"],
    "barritas": ["energy bar", "protein bar", "candy bars", "gluten free bar", "hand protein bar"],
    "pasta": ["whole wheat pasta", "spaghetti", "pasta"],
    "aseo": ["shampoo", "body spray", "toothpaste"],
    "patatas": ["french fries", "mashed potato"],
    "panaderia": ["whole weat flour", "fresh bread"],
    "otros":  ["babies food", "pet food", "magazines", "clothes accessories", "bug spray", "gums", "napkins"]
}
# Hay elementos suficientemente importantes, como los huevos, que no se han agrupado en ninguna categoría.
# Luego, hay otros que no sé muy bien en que categoría meterlos, por lo que se dejan en la original.

Tk().withdraw()
try:
    cfg = filedialog.askopenfilename(initialdir="./", title="Seleccione fichero",
                                        filetypes=[("CSV Files", ".csv")])
except(OSError, FileNotFoundError):
    print(f'No se ha podido abrir el fichero seleccionado.')
    sys.exit(100)
except Exception as error:
    print(f'Ha ocurrido un error: <{error}>')
    sys.exit(101)
if len(cfg) == 0 or cfg is None:
    print(f'No se ha seleccionado ningún archivo.')
    sys.exit(102)

counter_original = defaultdict(int) # "Tablas hash" para contar los elementos
counter_modified = defaultdict(int)

with open(cfg, newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('datos_compras_modified.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in reader:
            new_row = []
            for element in row:
                counter_original[element] += 1

                # Si el elemento está en alguna de las categorías, se cambia por la categoría
                for key, value in dict.items():
                    if element in value:
                        element = key
                        break


                counter_modified[element] += 1

                new_row.append(element)
            writer.writerow(new_row)

with open('resultados_analisis_agrupacion.txt', 'w', newline='') as filew:
    filew.write("Núnero de elementos originales: " + str(len(counter_original)) + "\n")
    filew.write(', '.join('{}: {}'.format(key, value) for key, value in sorted(counter_original.items(), key=lambda item: item[1], reverse=True)))
    filew.write("\n\nNúnero de nuevas categorías: " + str(len(counter_modified)) + "\n")
    filew.write(', '.join('{}: {}'.format(key, value) for key, value in sorted(counter_modified.items(), key=lambda item: item[1], reverse=True)))
    
print("Done!")

