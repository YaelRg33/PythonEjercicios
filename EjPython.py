from tkinter import *
from tkinter import ttk


def ventanaEjercicio1():
    listaTrabajadoresEj1 = []
    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 1: Aumento de Sueldos")
    nuevaVentana.geometry("450x550")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Sistema de Registro de Sueldos", font=("Arial", 12, "bold")).pack(pady=10)

    nombreVar = StringVar()
    sueldoVar = StringVar()

    Label(nuevaVentana, text="Nombre del trabajador:").pack()
    Entry(nuevaVentana, textvariable=nombreVar, width=30).pack(pady=5)

    Label(nuevaVentana, text="Sueldo basico:").pack()
    Entry(nuevaVentana, textvariable=sueldoVar, width=30).pack(pady=5)

    etiquetaAlertasEj1 = Label(nuevaVentana, text="", fg="red")
    etiquetaAlertasEj1.pack(pady=5)

    def calcular():
        nombre = nombreVar.get()
        sueldoTexto = sueldoVar.get()

        if nombre == "" or sueldoTexto == "":
            etiquetaAlertasEj1.config(text="Completa todos los campos.", fg="red")
            return

        try:
            sueldo = float(sueldoTexto)
            if sueldo < 0:
                etiquetaAlertasEj1.config(text="El sueldo no puede ser negativo.", fg="red")
                return
        except ValueError:
            etiquetaAlertasEj1.config(text="Ingresa un valor numérico válido para el sueldo.", fg="red")
            return

        if sueldo < 4000:
            aumento = sueldo * 0.15
        elif sueldo <= 7000:
            aumento = sueldo * 0.10
        else:
            aumento = sueldo * 0.08

        nuevoSueldo = sueldo + aumento

        listaTrabajadoresEj1.append(f"Nombre: {nombre} | Nuevo Sueldo: ${nuevoSueldo:.2f}")

        cajaHistorial.delete(1.0, END)
        for registro in listaTrabajadoresEj1:
            cajaHistorial.insert(END, registro + "\n")

        nombreVar.set("")
        sueldoVar.set("")

        etiquetaAlertasEj1.config(text=f"Aumento aplicado: ${aumento:.2f}", fg="green")

    Button(nuevaVentana, text="Calcular", command=calcular).pack(pady=10)

    Label(nuevaVentana, text="Historial de Trabajadores:").pack(pady=5)
    cajaHistorial = Text(nuevaVentana, height=10, width=50)
    cajaHistorial.pack()

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


totalRecaudadoEj2 = 0.0
def ventanaEjercicio2():
    global totalRecaudadoEj2

    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 2: Parque de Diversiones")
    nuevaVentana.geometry("400x600")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Bienvenido al Parque de Diversiones", font=("Arial", 12, "bold")).pack(pady=10)

    nombreVar = StringVar()
    edadVar = StringVar()
    juegosVar = StringVar()
    listaClientesEj2 = []

    Label(nuevaVentana, text="Nombre del visitante:").pack()
    Entry(nuevaVentana, textvariable=nombreVar, width=30).pack(pady=5)

    Label(nuevaVentana, text="Edad:").pack()
    Entry(nuevaVentana, textvariable=edadVar, width=30).pack(pady=5)

    Label(nuevaVentana, text="Cantidad de juegos utilizados:").pack()
    Entry(nuevaVentana, textvariable=juegosVar, width=30).pack(pady=5)

    etiquetaAlertasEj2 = Label(nuevaVentana, text="", fg="red")
    etiquetaAlertasEj2.pack(pady=5)

    def calcular():
        global totalRecaudadoEj2

        nombre = nombreVar.get()
        edadTexto = edadVar.get()
        juegosTexto = juegosVar.get()
        precio = 50

        if nombre == "" or edadTexto == "" or juegosTexto == "":
            etiquetaAlertasEj2.config(text="Completa de manera correcta todos los campos", fg="red")
            return

        try:
            edad = int(edadTexto)
            juegos = int(juegosTexto)
            if edad < 0 or juegos < 0:
                etiquetaAlertasEj2.config(text="La edad y los juegos no pueden ser negativos", fg="red")
                return
        except ValueError:
            etiquetaAlertasEj2.config(text="Ingresa valores numericos para edad y juegos", fg="red")
            return

        subtotal = precio * juegos

        if edad < 10:
            descuento = subtotal * 0.25
        elif edad <= 17:
            descuento = subtotal * 0.10
        else:
            descuento = 0

        precioFinal = subtotal - descuento
        totalRecaudadoEj2 += precioFinal

        listaClientesEj2.append(f"{nombre} | Pagó: ${precioFinal:.2f} | Ahorro: ${descuento:.2f}")

        cajaDescuentos.delete(1.0, END)
        for registro in listaClientesEj2:
            cajaDescuentos.insert(END, registro + "\n")

        etiquetaTotal.config(text=f"Total recaudado por el parque: ${totalRecaudadoEj2:.2f}")

        nombreVar.set("")
        edadVar.set("")
        juegosVar.set("")

        etiquetaAlertasEj2.config(
            text=f"Total a pagar: ${precioFinal:.2f} | Descuento aplicado: ${descuento:.2f}", fg="green")

    Button(nuevaVentana, text="Calcular y Guardar", command=calcular).pack(pady=10)

    Label(nuevaVentana, text="Historial de visitantes:").pack(pady=5)
    cajaDescuentos = Text(nuevaVentana, height=8, width=45)
    cajaDescuentos.pack()

    etiquetaTotal = Label(nuevaVentana, text="Total recaudado por el parque: $0.00", font=("Arial", 10, "bold"))
    etiquetaTotal.pack(pady=10)

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


totalVendidoEj3 = 0.0
def ventanaEjercicio3():
    global totalVendidoEj3

    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 3: Descuentos de tienda")
    nuevaVentana.geometry("400x550")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    alertasEj3 = Label(nuevaVentana, text="", fg="red")
    alertasEj3.pack(pady=5)
    Label(nuevaVentana, text="Sistema de Descuentos por Mes", font=("Arial", 12, "bold")).pack(pady=10)

    nombreVar = StringVar()
    importeVar = StringVar()
    mesVar = StringVar()

    listaComprasEj3 = []

    Label(nuevaVentana, text="Nombre del cliente:").pack()
    Entry(nuevaVentana, textvariable=nombreVar, width=30).pack(pady=5)

    Label(nuevaVentana, text="Mes de la compra:").pack()
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]
    comboMes = ttk.Combobox(nuevaVentana, textvariable=mesVar, values=meses, state="readonly", width=27)
    comboMes.pack(pady=5)

    Label(nuevaVentana, text="Importe de la compra:").pack()
    Entry(nuevaVentana, textvariable=importeVar, width=30).pack(pady=5)

    def calcularDescuento():
        global totalVendidoEj3

        nombre = nombreVar.get()
        mes = mesVar.get()
        importeTexto = importeVar.get()

        if nombre == "" or mes == "" or importeTexto == "":
            alertasEj3.config(text="Completa todos los campos y selecciona un mes", fg="red")
            return

        try:
            importe = float(importeTexto)
            if importe <= 0:
                alertasEj3.config(text="El importe debe ser mayor a 0", fg="red")
                return
        except ValueError:
            alertasEj3.config(text="Ingresa un numero valido para el importe", fg="red")
            return

        if mes == "Octubre":
            descuento = importe * 0.15
        elif mes == "Diciembre":
            descuento = importe * 0.20
        elif mes == "Julio":
            descuento = importe * 0.10
        else:
            descuento = 0

        totalFinal = importe - descuento
        totalVendidoEj3 += totalFinal

        listaComprasEj3.append(f"{nombre} ({mes}) | Pago: ${totalFinal:.2f}")

        cajaCompras.delete(1.0, END)
        for registro in listaComprasEj3:
            cajaCompras.insert(END, registro + "\n")

        etiquetaTotal.config(text=f"Total vendido en el dia: ${totalVendidoEj3:.2f}")

        nombreVar.set("")
        importeVar.set("")
        comboMes.set("")
        alertasEj3.config(text=f"Compra registrada.\nTotal a pagar: ${totalFinal:.2f}\nDescuento: ${descuento:.2f}",
                          fg="green")

    Button(nuevaVentana, text="Guardar", command=calcularDescuento).pack(pady=10)

    Label(nuevaVentana, text="Historial de compras:").pack(pady=5)
    cajaCompras = Text(nuevaVentana, height=8, width=45)
    cajaCompras.pack()

    etiquetaTotal = Label(nuevaVentana, text="Total vendido en el día: $0.00", font=("Arial", 10, "bold"))
    etiquetaTotal.pack(pady=10)

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


intentosEj4 = 0
def ventanaEjercicio4():
    global intentosEj4
    intentosEj4 = 0

    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 4: Validación de Numeros <10")
    nuevaVentana.geometry("400x400")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Validacion de Numero Menor a 10", font=("Arial", 12, "bold")).pack(pady=10)

    numeroVar = StringVar()

    Label(nuevaVentana, text="Ingresa un numero entero menor que 10:").pack()
    Entry(nuevaVentana, textvariable=numeroVar, width=30).pack(pady=5)

    alertasEj4 = Label(nuevaVentana, text="", fg="red")
    alertasEj4.pack(pady=5)

    resultadosEj4 = Label(nuevaVentana, text="", font=("Arial", 11, "bold"))
    resultadosEj4.pack(pady=10)

    def validar():
        global intentosEj4

        intentosEj4 += 1

        numeroTexto = numeroVar.get()

        if numeroTexto == "":
            alertasEj4.config(text=f"Intento {intentosEj4}: El campo está vacio.", fg="red")
            return

        try:
            numero = int(numeroTexto)
        except ValueError:
            alertasEj4.config(text=f"Intento {intentosEj4}: Ingresa solo numeros enteros.", fg="red")
            return

        if numero >= 10:
            alertasEj4.config(text=f"Intento {intentosEj4}: El numero {numero} NO es menor a 10.", fg="red")
            resultadosEj4.config(text="")
        else:
            alertasEj4.config(text="Validación exitosa", fg="green")
            resultadosEj4.config(
                text=f"Numero correcto ingresado: {numero}\nCantidad de intentos: {intentosEj4}")

            intentosEj4 = 0
            numeroVar.set("")

    Button(nuevaVentana, text="Validar Numero", command=validar).pack(pady=10)
    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


intentosEj5 = 0
def ventanaEjercicio5():
    global intentosEj5
    intentosEj5 = 0

    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 5: Validación de numeros <20")
    nuevaVentana.geometry("400x350")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Validacion de Numero (0 a 20)", font=("Arial", 12, "bold")).pack(pady=10)

    numeroVar = StringVar()
    Label(nuevaVentana, text="Ingresa un numero entre 0 y 20:").pack()
    Entry(nuevaVentana, textvariable=numeroVar, width=30).pack(pady=5)

    alertasEj5 = Label(nuevaVentana, text="", fg="red")
    alertasEj5.pack(pady=5)

    def validarRango(num):
        return 0 <= num <= 20

    def validar():
        global intentosEj5
        intentosEj5 += 1
        try:
            numero = int(numeroVar.get())
            if not validarRango(numero):
                alertasEj5.config(text=f"{numero} está fuera del rango. (Intento {intentosEj5})", fg="red")
            else:
                alertasEj5.config(text=f"Numero valido: {numero}. Tomo {intentosEj5} intentos.", fg="green")
                intentosEj5 = 0
                numeroVar.set("")
        except ValueError:
            alertasEj5.config(text=f"Ingresa un numero entero, Intento {intentosEj5}", fg="red")

    Button(nuevaVentana, text="Validar Numero", command=validar).pack(pady=10)
    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


intentosIncorrectosEj6 = 0
listaIntentosEj6 = []
def ventanaEjercicio6():
    global listaIntentosEj6, intentosIncorrectosEj6
    listaIntentosEj6.clear()
    intentosIncorrectosEj6 = 0

    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 6: Intentos de validacion")
    nuevaVentana.geometry("400x500")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Registro de Intentos (0 a 20)", font=("Arial", 12, "bold")).pack(pady=10)

    numeroVar = StringVar()
    Label(nuevaVentana, text="Ingresa un numero:").pack()
    Entry(nuevaVentana, textvariable=numeroVar).pack(pady=5)

    etiquetaAlertasEj6 = Label(nuevaVentana, text="", fg="red")
    etiquetaAlertasEj6.pack(pady=5)

    def validar():
        global listaIntentosEj6, intentosIncorrectosEj6

        try:
            numero = int(numeroVar.get())
            listaIntentosEj6.append(numero)

            if 0 <= numero <= 20:
                etiquetaAlertasEj6.config(
                    text=f"Numero {numero} correcto.\nErrores cometidos: {intentosIncorrectosEj6}", fg="green")
                listaIntentosEj6.clear()
                intentosIncorrectosEj6 = 0
            else:
                intentosIncorrectosEj6 += 1
                etiquetaAlertasEj6.config(text=f"Fuera de rango Van {intentosIncorrectosEj6} errores.", fg="red")

            cajaHistorial.delete(1.0, END)
            cajaHistorial.insert(END, f"Historial ingresado: {listaIntentosEj6}")
            numeroVar.set("")

        except ValueError:
            etiquetaAlertasEj6.config(text="Ingresa un numero entero", fg="red")

    Button(nuevaVentana, text="Ingresar numero", command=validar).pack(pady=10)

    cajaHistorial = Text(nuevaVentana, height=5, width=40)
    cajaHistorial.pack(pady=10)

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


def ventanaEjercicio7():
    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 7: Suma de Enteros")
    nuevaVentana.geometry("400x400")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Suma de los primeros n numeros", font=("Arial", 12, "bold")).pack(pady=10)

    nVar = StringVar()
    Label(nuevaVentana, text="Ingresa un numero entero positivo (n):").pack()
    Entry(nuevaVentana, textvariable=nVar).pack(pady=5)

    etiquetaAlertasEj7 = Label(nuevaVentana, text="", fg="red")
    etiquetaAlertasEj7.pack(pady=5)

    def calcularSuma():
        try:
            n = int(nVar.get())
            if n <= 0:
                etiquetaAlertasEj7.config(text="n debe ser positivo.", fg="red")
                return

            suma = sum(range(1, n + 1))
            secuencia = " + ".join(str(i) for i in range(1, n + 1))

            cajaResultados.delete(1.0, END)
            cajaResultados.insert(END, f"Secuencia: {secuencia}\n\nResultado Final: {suma}")
            etiquetaAlertasEj7.config(text="Calculo finalizado", fg="green")

        except ValueError:
            etiquetaAlertasEj7.config(text="Ingresa un numero valido", fg="red")

    Button(nuevaVentana, text="Calcular", command=calcularSuma).pack(pady=10)
    cajaResultados = Text(nuevaVentana, height=8, width=40)
    cajaResultados.pack()

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


listaNumsEj8 = []
sumaAcumuladaEj8 = 0
def ventanaEjercicio8():
    global listaNumsEj8, sumaAcumuladaEj8
    listaNumsEj8.clear()
    sumaAcumuladaEj8 = 0

    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 8: Suma acumulativa")
    nuevaVentana.geometry("400x450")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Suma hasta ingresar 0", font=("Arial", 12, "bold")).pack(pady=10)

    numeroVar = StringVar()
    Label(nuevaVentana, text="Ingresa un numero (0 para detener):").pack()
    Entry(nuevaVentana, textvariable=numeroVar).pack(pady=5)

    etiquetaAlertasEj8 = Label(nuevaVentana, text="Suma actual: 0", font=("Arial", 10, "bold"))
    etiquetaAlertasEj8.pack(pady=5)

    def agregarNumero():
        global listaNumsEj8, sumaAcumuladaEj8
        try:
            num = int(numeroVar.get())

            if num == 0:
                cajaResultados.delete(1.0, END)
                cajaResultados.insert(END,
                                      f"Lista: {listaNumsEj8}\nCantidad: {len(listaNumsEj8)}\nSuma Total: {sumaAcumuladaEj8}")
                etiquetaAlertasEj8.config(text="Proceso finalizado", fg="green")
                listaNumsEj8.clear()
                sumaAcumuladaEj8 = 0
            else:
                listaNumsEj8.append(num)
                sumaAcumuladaEj8 += num
                etiquetaAlertasEj8.config(text=f"Suma actual: {sumaAcumuladaEj8}")

            numeroVar.set("")
        except ValueError:
            etiquetaAlertasEj8.config(text="Ingresa un entero valido", fg="red")

    Button(nuevaVentana, text="Agregar numero", command=agregarNumero).pack(pady=10)
    cajaResultados = Text(nuevaVentana, height=8, width=40)
    cajaResultados.pack()

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


listaNumsEj9 = []
sumaAcumuladaEj9 = 0
def ventanaEjercicio9():
    global listaNumsEj9, sumaAcumuladaEj9
    listaNumsEj9.clear()
    sumaAcumuladaEj9 = 0

    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 9: Suma con limite")
    nuevaVentana.geometry("400x450")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Suma hasta superar 100", font=("Arial", 12, "bold")).pack(pady=10)

    numeroVar = StringVar()
    Label(nuevaVentana, text="Ingresa un numero:").pack()
    Entry(nuevaVentana, textvariable=numeroVar).pack(pady=5)

    etiquetaAlertasEj9 = Label(nuevaVentana, text="Suma parcial: 0", font=("Arial", 10, "bold"))
    etiquetaAlertasEj9.pack(pady=5)

    def agregarNumero():
        global listaNumsEj9, sumaAcumuladaEj9
        try:
            num = int(numeroVar.get())
            listaNumsEj9.append(num)
            sumaAcumuladaEj9 += num

            if sumaAcumuladaEj9 > 100:
                cajaResultados.delete(1.0, END)
                cajaResultados.insert(END,
                                      f"Limite alcanzado\nCantidad de números: {len(listaNumsEj9)}\nLista: {listaNumsEj9}\nSuma Final: {sumaAcumuladaEj9}")
                etiquetaAlertasEj9.config(text="Proceso finalizado", fg="green")
                listaNumsEj9.clear()
                sumaAcumuladaEj9 = 0
            else:
                etiquetaAlertasEj9.config(text=f"Suma parcial: {sumaAcumuladaEj9}", fg="blue")

            numeroVar.set("")
        except ValueError:
            etiquetaAlertasEj9.config(text="Ingresa un entero valido.", fg="red")

    Button(nuevaVentana, text="Agregar numero", command=agregarNumero).pack(pady=10)
    cajaResultados = Text(nuevaVentana, height=8, width=40)
    cajaResultados.pack()

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)


def ventanaEjercicio10():
    global listaTrabajadores
    listaTrabajadores = []
    nuevaVentana = Toplevel(window)
    window.withdraw()

    nuevaVentana.title("Ejercicio 10: Pagos de trabajadores")
    nuevaVentana.geometry("450x700")

    def regresarMenu():
        nuevaVentana.destroy()
        window.deiconify()

    nuevaVentana.protocol("WM_DELETE_WINDOW", regresarMenu)

    Label(nuevaVentana, text="Sistema de Pago de Nomina", font=("Arial", 12, "bold")).pack(pady=10)

    nombreVar = StringVar()
    horasNormVar = StringVar()
    pagoHoraVar = StringVar()
    horasExtVar = StringVar()
    hijosVar = StringVar()

    Label(nuevaVentana, text="Nombre del trabajador:").pack()
    Entry(nuevaVentana, textvariable=nombreVar).pack()

    Label(nuevaVentana, text="Horas normales trabajadas:").pack()
    Entry(nuevaVentana, textvariable=horasNormVar).pack()

    Label(nuevaVentana, text="Pago por hora normal:").pack()
    Entry(nuevaVentana, textvariable=pagoHoraVar).pack()

    Label(nuevaVentana, text="Horas extras trabajadas:").pack()
    Entry(nuevaVentana, textvariable=horasExtVar).pack()

    Label(nuevaVentana, text="Número de hijos:").pack()
    Entry(nuevaVentana, textvariable=hijosVar).pack()

    etiquetaAlertasEj10 = Label(nuevaVentana, text="", fg="red")
    etiquetaAlertasEj10.pack(pady=5)

    def calcularNomina():
        nombre = nombreVar.get()
        if nombre == "" or horasNormVar.get() == "" or pagoHoraVar.get() == "" or horasExtVar.get() == "" or hijosVar.get() == "":
            etiquetaAlertasEj10.config(text="Completa todos los campos", fg="red")
            return

        try:
            horasNorm = float(horasNormVar.get())
            pagoHora = float(pagoHoraVar.get())
            horasExt = float(horasExtVar.get())
            hijos = int(hijosVar.get())

            pagoNormal = horasNorm * pagoHora
            pagoExtra = horasExt * (pagoHora * 1.5)
            bono = hijos * 0.5
            pagoTotal = pagoNormal + pagoExtra + bono

            resumen = f"{nombre} | Normal: ${pagoNormal:.2f} | Extra: ${pagoExtra:.2f} | Bono: ${bono:.2f} | Total: ${pagoTotal:.2f}"
            listaTrabajadores.append(resumen)

            cajaReporte.delete(1.0, END)
            for reg in listaTrabajadores:
                cajaReporte.insert(END, reg + "\n")

            etiquetaAlertasEj10.config(text=f"Nomina de {nombre} calculada correctamente", fg="green")

            nombreVar.set("")
            horasNormVar.set("")
            pagoHoraVar.set("")
            horasExtVar.set("")
            hijosVar.set("")

        except ValueError:
            etiquetaAlertasEj10.config(text="Verifica que los valores numericos sean correctos", fg="red")

    Button(nuevaVentana, text="Calcular Pago", command=calcularNomina).pack(pady=10)

    Label(nuevaVentana, text="Reporte de Pagos:").pack()
    cajaReporte = Text(nuevaVentana, height=10, width=50)
    cajaReporte.pack()

    Button(nuevaVentana, text="Regresar al Menú Principal", command=regresarMenu).pack(pady=10)

window = Tk()
window.title("Aplicación")
window.geometry('600x800')
window.config(bg='beige')

frame = Frame(window)
frame.pack(pady=10)
frame.config(width="450", height="750")
frame.config(bg='red')
frame.config(bd=10)
frame.config(relief='groove')
frame.config(cursor='pirate')

label = Label(frame, text="MENÚ DE EJERCICIOS", fg="blue", font=("Comic Sans MS", 14, "bold"))
label.place(x=100, y=20)

boton1 = Button(frame, text="1. Sistema de Sueldos", width=25, command=ventanaEjercicio1)
boton1.place(x=100, y=80)

boton2 = Button(frame, text="2. Parque de Diversiones", width=25, command=ventanaEjercicio2)
boton2.place(x=100, y=130)

boton3 = Button(frame, text="3. Descuentos de tienda", width=25, command=ventanaEjercicio3)
boton3.place(x=100, y=180)

boton4 = Button(frame, text="4. Validación de Números <10", width=25, command=ventanaEjercicio4)
boton4.place(x=100, y=230)

boton5 = Button(frame, text="5. Validación de Números <20", width=25, command=ventanaEjercicio5)
boton5.place(x=100, y=280)

boton6 = Button(frame, text="6. Intentos de validación", width=25, command=ventanaEjercicio6)
boton6.place(x=100, y=330)

boton7 = Button(frame, text="7. Suma de Enteros", width=25, command=ventanaEjercicio7)
boton7.place(x=100, y=380)

boton8 = Button(frame, text="8. Suma acumulativa", width=25, command=ventanaEjercicio8)
boton8.place(x=100, y=430)

boton9 = Button(frame, text="9. Suma con limite", width=25, command=ventanaEjercicio9)
boton9.place(x=100, y=480)

boton10 = Button(frame, text="10. Pagos de trabajadores", width=25, command=ventanaEjercicio10)
boton10.place(x=100, y=530)

try:
    miImagen = PhotoImage(file="gato.png")
    labelImg = Label(frame, image=miImagen)
    labelImg.place(x=120, y=600)
except:
    pass

window.mainloop()