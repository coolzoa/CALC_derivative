;Manual de usuario para calculo.py
;Ingresar la funcion y el intervalo donde la funcion es continua y derivable
;Seleciconar las casillas de las graficas que desea ver
;Seleccionar 'Graficar'
; La funcion rectas se encarga de determinar la recta tangente y secante
;	dependiendo de las casillas, va a ocultar algunos graficos y mostrar otros
; los valores de c encontrados por el valor intermedio se van a mostrar al lado derecho de la ventana
;Las ecuaciones de las rectas encontradas tambien seran mostradas en el lado derecho de la pantalla

Rectas:
La recta secante se muestra en verde
La funcion se muestra en color negro
La recta tangente semuestra en color azul


;NOTA: 
	1. Cuando ingrese la funcion, debe tenerla en terminos de 'x' de lo contrario no va a servir
	2. Si va a incluir un termino (ej 2x), debe poner el * para que el programa reconozca que es una 		multiplicacion

	3. Puede haber errores cuando se trata de graficar solo la recta tangente o solo la recta secante

	4. En caso de raices, solo se puede calcular cuando se usan raices cuadradas

	5. Si va a graficar una fraccion, use “/“ para señalar que es una fraccion

	6/ si va a meter una funcion trigonometrica al cuadrado, tiene que ponerlo como producto.