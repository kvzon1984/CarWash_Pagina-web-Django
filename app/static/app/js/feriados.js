let url = "https://api.control-z.cl/api/feriados"

$.get(
	url,
	function (item) {
		let nombreFestivo = ""
		let fechaFestiva = ""
		let fecha = ""
		let fechaHoy = new Date(new Date().setHours(0, 0, 0, 0))
		let diaFestivo = []
		let contador = 0

		item.forEach(function (respuesta) {
			nombreFestivo = respuesta.nombre
			fecha = respuesta.fecha

			fechaFestiva = new Date(fecha.split("-").join("/"))

			if (fechaFestiva > fechaHoy) {
				contador += 1

				if (contador == 1) {
					diaFestivo = nombreFestivo + " " + fecha.split("-").reverse().join("/")
					
				}
			}
		})

		$("#feriado").text(diaFestivo)
	},
	"json"
)