//para hacer el .js como un servidor
var http = require('http');
//para conectar a mongoDB
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost/hacking_db";
//puerto donde vamos a escuchar
var PORT = 3000;

//variable donde se guarda un texto de error o actualizacion
var textoErr;
//agarramos express
const express = require('express');
const app = express();

//usamos ejs para meter nuestro contenido al html
app.set('view engine', 'ejs');

/*
//usamos esto para poder ejecutar el python, o el comando que actualice el collection 'graficas'
//el cual tiene los datos para poder graficar.
const execSync = require('child_process').execSync;
*/

MongoClient.connect(url, function(err, db) {
	  //si hay un error, mandar a página de error
	  if (err) {
		console.log('Error al conectar a la base de datos.')
		texto = "Error al conectar a la base de datos."
		res.render('error.ejs', {error: texto})
	  }
	  //Mostrar en consola
	  console.log('conectado a mongodb');
	  app.listen(PORT, function() {
		console.log('listening on 3000')
	  });
	  
	  //este es para el home
	  app.get('/', function(req, res) {
		var query = {};
		//de la coleccion volumen, encontrar todos los datos.
		db.collection("productos").find(query).toArray(function (err, result) {
			if (err) {
				console.log('Error al buscar graficas en la base de datos')
				textoErr = "Error al buscar graficas en la base de datos"
				res.render('error.ejs', {error: textoErr})
				}
			//si la consulta arroja resultados, en infoVolumen los guardamos, por orden.	
			if (result.length > 0 ) {				
				var A = result[0]["AB"]
				console.log(A)
				var B = result[0]["CD"]
				console.log(B)
				var C = result[0]["EF"]
				console.log(C)
			}
		res.render('index.ejs',{var1: A, var2:B, var3:C})
		});
		});
	  });
