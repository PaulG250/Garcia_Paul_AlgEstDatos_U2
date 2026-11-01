# Biblioteca — Unidad 2

Programa de consola de Python 3, sin bibliotecas externas.

## Ejecución

Descarga el repositorio, abre una terminal en su carpeta y ejecuta:

```console
python main.py
```

## Requerimientos

- R1: diccionario código -> título y autor. Registra y busca libros; rechaza códigos repetidos.
- R2: muestra los códigos ordenados con sorted(). Un TreeMap mantiene las claves ordenadas durante las actualizaciones; dict conserva el orden de inserción y no ordena por clave.
- R3: conjunto de identificadores de socios, con registro sin duplicados y consulta de pertenencia.
- R4: conjuntos de socios con préstamos de novela y ciencia. Calcula intersección, diferencia y unión, y cuenta los socios distintos.

La opción 6 registra la pertenencia de un socio a un género de préstamo. No modela ejemplares ni devoluciones. Los datos viven en memoria y se reinician al cerrar el programa.

## Ejemplo de prueba manual

1. Opción 3: aparecen L001, L002 y L003 en ese orden.
2. Opción 2, L001: muestra Don Quijote de la Mancha.
3. Opción 4, S001: informa que el socio ya está registrado.
4. Opción 7: ambos géneros S002; solo novela S001; unión S001, S002, S003; total 3.
5. Opción 6, S004, ciencia; opción 7: el total pasa a 4.
6. Opción 0: termina el programa.

## Eficiencia

n = libros, a = socios de novela, b = socios de ciencia.

| Operación | Tiempo promedio |
|---|---|
| Registrar/buscar libro | O(1) |
| Ordenar catálogo | O(n log n) |
| Registrar/consultar socio | O(1) |
| Intersección | O(min(a,b)) |
| Diferencia novela - ciencia | O(a) |
| Unión | O(a+b) |
| Contar unión ya construida | O(1) |

Las operaciones hash pueden degradarse por colisiones. Ordenar los resultados para mostrarlos añade O(k log k) por conjunto de k elementos. El orden del catálogo es lexicográfico: usa códigos con ceros, como L001.
