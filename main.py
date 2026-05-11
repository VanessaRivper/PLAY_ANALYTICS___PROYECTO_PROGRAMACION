from archivos import *
from analisis import *

datos = cargar_datos()

while True:
    print("+----------------------------------+")
    print("|            MENÚ                  |")
    print("+----------------------------------+")
    print("|        1. Buscar                 |")
    print("|        2. Estadísticas           |") 
    print("|        3. Filtrar                |")
    print("|        4. Historial              |")
    print("|        5. Comparar plataformas   |")
    print("|        6. Salir                  |")
    print("+----------------------------------+")
    
    opcion = input("\n Seleccione una opción: ")
    
    if opcion == "1":
        entrada = input("Ingrese búsqueda: ")
        resultados = buscar(datos, entrada)
        guardar_hist(entrada, len(resultados))
        guardar = input("¿Desea guardar los resultados? (s/n): ")

        if guardar.lower() == "s":
            guardar_csv("Busqueda.csv", resultados)
        
    elif opcion == "2":
        estadisticas(datos)
        guardar_hist("Estadísticas", 1)
        
    elif opcion == "3":
        resultados = filtrar(datos)
        if resultados:
        guardar_hist(f"Filtro", len(resultados))

    elif opcion == "4":
        ver_historial()

    elif opcion == "5":
        comparar(datos)
                
    elif opcion == "6":
        print("\n¡Adiós! El programa ha finalizado")  
        break
    else:
        print("Opción inválida")

    input("\nPresione Enter para continuar ")
