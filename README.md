# 📈 Modelado de Crecimiento Exponencial con EDOs: Caso Solana (SOL)

Este proyecto consiste en el análisis del comportamiento del precio de Solana (SOL) utilizando un modelo matemático basado en Ecuaciones Diferenciales Ordinarias (EDOs), específicamente para representar un crecimiento exponencial. Se modela el precio del activo como una función del tiempo y se ajusta a los datos históricos obtenidos mediante la API oficial de Binance.

# 📥 Obtención de datos

Los datos utilizados en este proyecto provienen de la API de Binance. Se recopila información diaria del par SOL/USDT en el rango comprendido entre el 23 de marzo de 2022 y el 1 de abril de 2022.

El archivo sol_plot_data.csv se genera automáticamente a partir de un script en Python que realiza la consulta y guarda los datos procesados.

# 📐 Modelado con EDO
 Se plantea una EDO del tipo:


dP/dt = kP
Donde:

P(t) es el precio de Solana en función del tiempo.

k es la tasa de crecimiento.

La solución general de esta EDO es:


P(t) = P₀ · e^(kt)

A partir de los datos extraídos, se linealiza el modelo aplicando logaritmo natural a los precios para obtener una relación lineal, de modo que se pueda estimar el parámetro k mediante regresión lineal simple.

# ⚙️ Proceso de ajuste

Se transforman los precios de cierre (Close) con logaritmo natural.

Se asocia cada precio con un valor de tiempo t a partir de la fecha.

Se aplica un modelo de regresión lineal para encontrar los valores de k y P₀.

Se utiliza la solución analítica de la EDO para generar la curva de predicción.

# 📊 Visualización de resultados

El gráfico resultante muestra:

Los precios reales de Solana en el rango de tiempo seleccionado.

La curva ajustada que representa el crecimiento exponencial estimado por el modelo.

Esto permite visualizar el grado de ajuste del modelo al comportamiento real del mercado en ese período específico.

📊 Dashboard en Google Sheets
Puedes ver el dashboard y los cálculos del análisis con los datos del proyecto en el siguiente enlace:

👉  ([Ver Dashboard en Google Sheets](https://docs.google.com/spreadsheets/d/1w5lPFt5nwxMDH9g1_u66DyS-534x_CnJDeKwwvUBNkE/edit?usp=sharing))

# 🧠 Conclusiones

Aunque el mercado de criptomonedas es altamente volátil y no siempre sigue una tendencia exponencial, este enfoque permite:

Explorar cómo ciertas tendencias a corto plazo pueden aproximarse con modelos matemáticos simples.

Tener una base conceptual para extender el análisis a modelos más complejos (por ejemplo, logísticos o estocásticos).

Integrar técnicas matemáticas con programación y análisis de datos en un caso real del ámbito financiero.
