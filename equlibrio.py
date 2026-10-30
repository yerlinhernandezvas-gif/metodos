import numpy as np
import pandas as pd

# Parámetros iniciales definidos en el modelo
precio_venta = 10      # Precio de venta por unidad (s)
costo_fijo = 1000      # Costos fijos totales (f)
costo_variable = 5     # Costo variable por unidad (v)

# Cálculo analítico del punto de equilibrio en unidades
# Fórmula: Costos Fijos / (Precio de Venta - Costo Variable Unitario)
punto_equilibrio = costo_fijo / (precio_venta - costo_variable)

print(f"Punto de equilibrio: {punto_equilibrio} unidades")

# Simulación de diferentes volúmenes de venta (de 0 a 400 unidades)
unidades = np.arange(0, 401, 20)
ingresos = unidades * precio_venta
costos_totales = costo_fijo + (costo_variable * unidades)
ganancias = ingresos - costos_totales

# Creación de un DataFrame para organizar los resultados
df_resultados = pd.DataFrame({
    'Unidades': unidades,
    'Ingresos': ingresos,
    'Costos Totales': costos_totales,
    'Ganancia': ganancias
})

print(df_resultados.to_string(index=False))
