import funcion_hotel as fn

while True:
    fn.ver_menu()
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.grabar()
    elif opcion == 2:
        fn.buscar()
    elif opcion == 3:
        fn.retirarse()
    else:
        fn.salir()
        break
    
    