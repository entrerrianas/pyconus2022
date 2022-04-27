import pandas as pd

datos = pd.read_excel('LAQUIACA-2019-JUNIO.xlsx')

print(list(datos.columns.values))
print(datos)

COLEGIOS = datos['ESCUELA']

print ("---------------------------------------------------------------")
print ("Colegios : ", COLEGIOS)

print ("---------------------------------------------------------------")
print ("Existen ", str(len(COLEGIOS)), " colegios.")
print ("---------------------------------------------------------------")

#from matplotlib import pyplot as plt

##CONSULTA = pd.value_counts(datos['ESCUELA']) #Digamos que Categorizo... o Cuento las veces que un valor se repite en una columna.
##print ("---------------------------------------------------------------")
##print (CONSULTA)
##print ("---------------------------------------------------------------")
##print ("Registros (Filas) : ", len(CONSULTA))
##print ("---------------------------------------------------------------")
##
####---------------------------------------------------------------
#### GRAFICA MODO BARRAS HORIZONTALES por eso es: BARH
####plot_barras = datos['ESCUELA'].value_counts().plot(kind='barh', title='MESAS CANTIDAD de VOTANTES')
####plt.show()
##
####---------------------------------------------------------------
##
####---------------------------------------------------------------
#### GRAFICA MODO BARRAS VERTICALES por eso es solo: BAR
####plot_barras = datos['ESCUELA'].value_counts().plot(kind='bar', title='MESAS CANTIDAD de VOTANTES')
####plt.show()
##
####---------------------------------------------------------------
##
#### GRAFICA MODO TORTA o PIE...
##plot_torta = datos['ESCUELA'].value_counts().plot(kind='pie', autopct='%.2f', figsize=(8, 8),
##                                            title='PORCENTAJE de VOTANTES por ESCUELAS')
##plt.show()
##
####---------------------------------------------------------------
#### SITIOS WEB DE AYUDA:
##
#### https://dfrieds.com/data-visualizations/bar-plot-python-pandas.html
##
#### https://mode.com/python-tutorial/counting-and-plotting-in-python/
##
####-------------------------------------------------------------------
