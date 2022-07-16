const mongoose = require("mongoose")

// Asignacion de URL que tendra conexion nuestra base de datos

const url = "mongodb://localhost:27017/Cine"

mongoose.connect(url,{})
    .then(() => console.log("Conexion a MongoDB exitosa"))
    .catch((error) => console.log("El error es:"+error))


// Crearemo un esquema para trabajar con la base de datos

const peliculasSchema = mongoose.Schema(
    {
        _id: Number,
        Pelicula: String
    }
)

const PeliculasModel = mongoose.model("Peliculas", peliculasSchema)

// Crearemos las funciones listar y agregar

const Listar = async()=>
{
    const Peliculas = await PeliculasModel.find()
    console.log(Peliculas)
}

const Agregar = async()=>
{
    const Peliculas = new PeliculasModel
    ({
        Pelicula: "ELVIS"
    })
    const resultado = await Peliculas.save()
    console.log(resultado)
}

Listar()
Agregar()