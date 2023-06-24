from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json


def suma2(x: int, y: int) -> int:
    res: int = x + y
    return res


def avanzarFila(fila: Queue, min: int):
    c1 = False
    c2 = False
    c3 = False
    t1 = 0
    t2 = 0
    t3 = 0
    f = fila.qsize()
    for i in range(min + 1):
        if t1 == 10:
            t1 = 0
            c1 = False
        if c1:
            t1 += 1

        if t2 == 4:
            t2 = 0
            c2 = False
        if c2:
            t2 += 1

        if t3 == 4:
            t3 = 0
            c3 = False
        if c3:
            t3 += 1

        if t3 == 3:
            fila.put(vuelve)

        if not c1 and i > 0 and fila.qsize() != 0:
            c1 = True
            fila.get()
        elif not c2 and i > 2 and fila.qsize() != 0:
            c2 = True
            fila.get()
        elif not c3 and i > 1 and fila.qsize() != 0:
            c3 = True
            vuelve = fila.get()
        if i % 4 == 0:
            fila.put(f + 1)
            f += 1


fila = [1, 2, 3]
# print(avanzarFila(fila, 20))
# print(fila)


# my_list = [1, 2, 3, 4, 5]

my_queue = Queue()

# Enqueue each item from the list into the queue
for item in fila:
    my_queue.put(item)

print(my_queue.queue)

avanzarFila(my_queue, 5)
print(my_queue.queue)


def procesamiento_pedidos(
    pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]
) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    for i, pedido in enumerate(pedidos):
        pedido["precio_total"] = 0
        pedido["estado"] = "completo"
        for key, value in pedido["productos"].items():
            if value > stock_productos[key]:

                pedido["productos"][key] = stock_productos[key]
                pedido["precio_total"] += stock_productos[key] * precios_productos[key]
                stock_productos[key] = 0
                pedido["estado"] = "incompleto"

            else:
                stock_productos[key] -= value
                pedido["precio_total"] += value * precios_productos[key]

        if pedido["estado"] != "incompleto":
            pedido["estado"] = "completo"
    return pedidos


pedidos = [
    {"id": 21, "cliente": "Gabriela", "productos": {"Manzana": 2}},
    {"id": 1, "cliente": "Juan", "productos": {"Manzana": 2, "Pan": 4, "Factura": 6}},
]

stock_productos = {"Manzana": 10, "Leche": 5, "Pan": 3, "Factura": 0}

precio_productos = {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.5, "Factura": 5}

# print(procesamiento_pedidos(pedidos, stock_productos, precio_productos))
# print(stock_productos)
