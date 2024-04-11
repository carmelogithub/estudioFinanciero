# coding: iso-8859-1 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos=pd.read_csv("ventas.csv")
print(datos.head())
print(datos.info())


#promedio del precio de venta
promedio_precio=datos['PRECIO'].mean()
print(promedio_precio)

#muestra la cantidad total por producto (agrupado si hubiera repeticiones)
#cuidado que deberás agrupar por nombre producto
cantidad_total_por_producto=datos.groupby("PRODUCTO")['CANTIDAD'].sum()
print(cantidad_total_por_producto)



cantidad_ordenada=datos.sort_values(by="CANTIDAD",ascending=False)
cantidad_top_5=cantidad_ordenada.head(5)
print(cantidad_top_5)
producto=cantidad_top_5["PRODUCTO"]
cantidad=cantidad_top_5["CANTIDAD"]
#gráfico de barras la cantidad total por producto
grafico=sns.barplot(x=producto,y=cantidad)
plt.title("Unidades vendidas por producto")
grafico.set_xticklabels(producto,rotation=45)
plt.show()

#muestre la evolución de cantidad vendida para el producto ALIVIOL
producto_elegido=datos[datos['PRODUCTO']=='ALIVIOL 3000']
print(producto_elegido)
cantidad_elegida=producto_elegido['CANTIDAD']
print(cantidad_elegida)

plt.scatter(producto_elegido['PRODUCTO'],producto_elegido['CANTIDAD'])
plt.xlabel("Producto")
plt.ylabel("cantidad")
plt.xticks(rotation=45)
plt.show()

#diseña un histograma para mostrar las cantidades. método plt.hist
plt.hist(datos['CANTIDAD'])
plt.title('precio de ventas')
plt.show()
