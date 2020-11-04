let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")

menu.addEventListener("click", function () {
	//60 + alto navegaciones
	if (header.style.height == "50px" || header.offsetHeight == 50) {
		header.style.height = 50 + nav.offsetHeight + "px"
	} else {
		header.style.height = "50px"
	}
})

window.addEventListener("resize", function () {
	//obtener el ancho
	let ancho = document.documentElement.clientWidth

	if (ancho > 480) {
		header.style = ""
	}
})