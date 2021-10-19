# Interes Compuesto, Valor Futuro, Valor Presente y Periodo
Programa que calcula cualquiera de las variables, teniendo las otras 3.
Es uno de los primeros desafíos del programa PlatziMaster, para evaluar las habilidades técnicas de los Masters (participantes del programa), del cual soy parte.

### El ejercicio consiste de lo siguiente: 

# Ejercicio_ValorFuturo
En este ejercicio tendrás que calcular el valor futuro de una inversión con base en el valor presente de la inversión, el interés y el periodo. 
## Descripción
El valor futuro de una inversión es justamente entender cuál va a ser el dinero en el futuro cuando acabe esta inversión o después de un cierto tiempo. Para esto lo puedes obtener si tienes el interés dado al periodo de esta inversión, el número de periodos a invertir y el valor presente, o cuánto vale el dinero al día de hoy. Esto se puede calcular con base en la siguiente fórmula:

<img src="https://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%20VF%3DVP%281&plus;i%29%5En " /> 

Donde:
- VF = Valor Futuro
- VP = Valor presente
- i = interés del periodo
- n = total de periodos

Como un ejemplo si una persona decide invertir 100 a una tasa del 1% por periodo por 10 periodos, entonces al final de los 10 periodos al final su inversión valdrá un total de 100*(1.01)^10=110.4

## Siguientes pasos
Usa algebra para despejar la fórmula y que igual puedas obtener calquiera de los valores (VP, i o n) dados los otros 3 valores. 

## Bonus
Investiga que es el interés convertido nominal y aplícalo en tu fórmula.

## Desarrollo del Problema

Se utilizaron las siguientes formulas del Interes Compuesto:

Valor Futuro $$VF = VP  (1+i)^n$$

Valor Presente $$VP = VF / (1+i)^n$$

Interes Compuesto $$i = ((VF/VP)^{(1/n)})-1$$

Periodo $$(logVF - logVP)/log(1+i) $$

Donde:
- VF = Valor Futuro
- VP = Valor presente
- i = interés compuesto del periodo
- n = total de periodos

###Uso de la Aplicación

La aplicación fue desarrollada con python 3, es una aplicación de consola y para poder ejecutarla se deben seguir los siguientes pasos en ambiente mac, para windows o linux, podría haber alguna modificación en los comandos.

1. Clonar el repositorio de github donde esta alojado el proyecto, en una carpeta vacia para tener mayor control, el comando es el siguiente:
`$ git clone git@github.com:FelixBravo/interescompuesto.git`

2. Después de clonar, entras al directorio "interescompuesto".
`$ cd interescompuesto`

3. Listas los archivos:
`$ ls`
		**README.md**: archivo que contiene la información del proyecto.
		**main.py**: archivo principal del proyecto que contiene la programación.

4. Ejecución del proyecto, siempre que quieras ejecutar el proyecto debes tipear lo siguiente:
`$ python3 main.py --help`

Con el comando help te mostrará una pequeña guia para poder ejecutar el programa.

5. Para buscar el Valor Futuro de una inversión se ejecuta lo siguiente:
`$ python3 main.py "Valor Futuro"`

Al ingresar este comando te pedirá ingresar las otras 3 variables (Valor Presente, Tasa de Interés compuesta o Efectiva, y el Periodo de tiempo en meses años, según corresponda con la tasa de interés).

Para la ejecución en busca de las otras variables:
Valor Presente = `$ python3 main.py "Valor Presente"`
Tasa de Interes = `$ python3 main.py "Tasa de Interes"`
Periodo = `$ python3 main.py "Periodo"`

Fin!, muchas gracias por leer, sientete libre si quieres mejorar el proyecto. Saludos.






