"""Biblioteca de consola: diccionarios y conjuntos de la Unidad 2."""


def registrar_libro(catalogo, codigo, titulo, autor):
    # R1: pertenencia e inserción en dict: O(1) promedio.
    if codigo in catalogo:
        return False
    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    return True


def buscar_libro(catalogo, codigo):
    # R1: búsqueda por clave: O(1) promedio.
    return catalogo.get(codigo)


def catalogo_ordenado(catalogo):
    # R2: ordenar n códigos: O(n log n); construir resultado: O(n).
    return [(codigo, catalogo[codigo]) for codigo in sorted(catalogo)]


def registrar_socio(socios, identificador):
    # R3: pertenencia y alta en set: O(1) promedio; evita duplicados.
    if identificador in socios:
        return False
    socios.add(identificador)
    return True


def analizar_prestamos(novela, ciencia):
    # R4: intersección O(min(a,b)), diferencia O(a), unión O(a+b), promedio.
    ambos = novela & ciencia
    solo_novela = novela - ciencia
    todos = novela | ciencia
    return ambos, solo_novela, todos


def leer_dato(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El dato no puede estar vacío.")


def mostrar_libro(codigo, libro):
    print(f"{codigo}: {libro['titulo']} — {libro['autor']}")


def main():
    catalogo = {
        "L003": {"titulo": "Breve historia del tiempo", "autor": "Stephen Hawking"},
        "L001": {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
        "L002": {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    }
    socios = {"S001", "S002", "S003", "S004"}
    novela = {"S001", "S002"}
    ciencia = {"S002", "S003"}

    while True:
        print("\nBIBLIOTECA\n1. Registrar libro\n2. Buscar libro\n3. Catálogo ordenado"
              "\n4. Registrar socio\n5. Consultar socio\n6. Registrar préstamo por género"
              "\n7. Analizar préstamos\n0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("Hasta pronto.")
            break
        elif opcion == "1":
            codigo = leer_dato("Código: ")
            titulo = leer_dato("Título: ")
            autor = leer_dato("Autor: ")
            ok = registrar_libro(catalogo, codigo, titulo, autor)
            print("Libro registrado." if ok else "El código ya existe.")
        elif opcion == "2":
            codigo = leer_dato("Código: ")
            libro = buscar_libro(catalogo, codigo)
            if libro is None:
                print("Libro no encontrado.")
            else:
                mostrar_libro(codigo, libro)
        elif opcion == "3":
            for codigo, libro in catalogo_ordenado(catalogo):
                mostrar_libro(codigo, libro)
        elif opcion == "4":
            ok = registrar_socio(socios, leer_dato("Identificador: "))
            print("Socio registrado." if ok else "El socio ya está registrado.")
        elif opcion == "5":
            # R3: consulta de pertenencia: O(1) promedio.
            existe = leer_dato("Identificador: ") in socios
            print("Socio registrado." if existe else "Socio no registrado.")
        elif opcion == "6":
            socio = leer_dato("Identificador del socio: ")
            if socio not in socios:
                print("Primero debe registrar al socio.")
                continue
            genero = leer_dato("Género (novela/ciencia): ").lower()
            if genero not in {"novela", "ciencia"}:
                print("Género no válido.")
                continue
            grupo = novela if genero == "novela" else ciencia
            if socio in grupo:
                print("El socio ya tiene un préstamo registrado en ese género.")
            else:
                grupo.add(socio)  # O(1) promedio.
                print("Préstamo por género registrado.")
        elif opcion == "7":
            ambos, solo, todos = analizar_prestamos(novela, ciencia)
            # sorted solo presenta los resultados; añade O(k log k) por grupo.
            print("Ambos géneros:", ", ".join(sorted(ambos)) or "Ninguno")
            print("Solo novela:", ", ".join(sorted(solo)) or "Ninguno")
            print("Socios distintos:", ", ".join(sorted(todos)) or "Ninguno")
            print("Total de socios distintos:", len(todos))
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalizado.")
