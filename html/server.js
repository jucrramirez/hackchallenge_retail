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
				var nombreProd = result[0]["Samsung Galaxy A50"][0][0]
				var tienda_elektra = result[0]["Samsung Galaxy A50"][0][1]
				var precio_elektra = result[0]["Samsung Galaxy A50"][0][3]
				var relacion_elektra = result[0]["Samsung Galaxy A50"][0][5]
				var entrega_elektra = result[0]["Samsung Galaxy A50"][0][7]
				var devolucion_elektra = result[0]["Samsung Galaxy A50"][0][8]
				var garantia_elektra = result[0]["Samsung Galaxy A50"][0][9]
				var tienda_coppel = result[0]["Samsung Galaxy A50"][1][1]
				var precio_coppel = result[0]["Samsung Galaxy A50"][1][3]
				var relacion_coppel = result[0]["Samsung Galaxy A50"][1][5]
				var entrega_coppel = result[0]["Samsung Galaxy A50"][1][7]
				var devolucion_coppel = result[0]["Samsung Galaxy A50"][1][8]
				var garantia_coppel = result[0]["Samsung Galaxy A50"][1][9]
			}
		res.render('index.ejs', {nomP: nombreProd, tien_E: tienda_elektra, pre_E: precio_elektra, rel_E: relacion_elektra, ent_E: entrega_elektra, dev_E: devolucion_elektra, gar_E: garantia_elektra, tien_C: tienda_coppel, pre_C: precio_coppel, rel_C: relacion_coppel, ent_C: entrega_coppel, dev_C: devolucion_coppel, gar_C: garantia_coppel})
		});
		});
	  });
