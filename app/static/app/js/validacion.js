/* Validacion Registro*/

$("#login_formulario").validate({

    rules:{
        rut:{
            required: true,
            rut: true
        },
        nombre:{
            required: true,
            minlength: 3,
            maxlength: 80
        },
        apellido:{
            required: true,
            minlength: 3,
            maxlength: 80
        },
        email:{
            required: true,
            email: true,
        },
        fecha_nacimiento:{
            required: true
        },
        nombre_usuario:{
            required: true,
            minlength: 5
        },
        password:{
            required: true,
            minlength: 8
        }
    }

})


/* Validacion login */
$("#login").validate({

    rules:{
        rut:{
            required: true,
            minlength: 7,
            maxlength: 10,
            rut: true
        },
        password:{
            required: true,
            minlength: 8
        }
    }

})

/* Validacion Contacto*/

$("#formulario_contacto").validate({
    rules:{
        tipo_solicitud:{
            required: true
        },
        nombre:{
            required: true,
            minlength: 3,
            maxlength: 80
        },
        apellidos:{
            required: true,
            minlength: 3,
            maxlength: 80
        },
        email:{
            required: true,
            email: true,
        },
        descripcion:{
            required: true,
            minlength: 3,
            maxlength: 200
        }
    }
})

/** Validacion Insumos */

$("#formulario_insumos").validate({
    rules:{
        nombre_producto:{
            required: true,
            minlength: 3,
            maxlength: 120
        },
        cantidad: {
            required: true,
            number: true
        },
        precio: {
            required: true,
            number: true
        },
        descripcion: {
            required: true,
            minlength:3,
            maxlength: 200
        }
    }
})