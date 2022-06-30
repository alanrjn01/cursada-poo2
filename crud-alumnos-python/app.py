from flask import Flask, jsonify, make_response,request
from alumnos import alumnos

app = Flask(__name__)
contador = 10

#peticion GET: retorna el JSON de los alumnos
@app.route('/alumnos',methods=['GET'])
def listar_alumnos():
    return jsonify(alumnos)

#peticion GET: retorna el JSON de un alumno a partir de una ID.
@app.route('/alumnos/<int:id>',methods=['GET'])
def listar_alumno(id):
    for alumno in alumnos:
        if alumno['id']==id:
            return jsonify(alumno)  
    return alumno_no_encontrado("El alumno no fue encontrado")    
            
#peticion POST: se crea un alumno y retorna el JSON.
@app.route('/alumnos', methods=['POST'])
def crear_alumno():
    global contador
    contador+=1
    try: 
        if request.json['nombre']!="" and request.json['apellido']!="" and request.json['dni']!="" :
            nuevo_alumno= {
                "id": contador,
                "nombre": request.json['nombre'],
                "notas": request.json['notas'],
                "dni": request.json['dni'],
                "apellido": request.json['apellido']
            }
            alumnos.append(nuevo_alumno)
            return request.json
        else:
            return error_al_crear_alumno("Faltan datos")
    except:
        return error_al_crear_alumno("Faltan atributos")

#peticion GET: mediante una ID se obtiene el promedio del alumno, retorna el JSON.
@app.route('/alumnos/promedio/<int:id>',methods=['GET'])
def obtener_promedio_alumno(id):
    notas = []
    promedio = 0
    for alumno in alumnos:
        if alumno['id']==id:
            notas = alumno['notas']
    if notas == []:
        return alumno_no_encontrado("El alumno a realizar promedio no fue encontrado o no tiene notas")        
    for nota in notas:
        promedio+=nota
    promedio = promedio/len(notas)
    return jsonify({"promedio":promedio})

#peticion GET: se obtiene el promedio de cada alumno, retorna el JSON.
@app.route('/alumnos/promedios',methods=['GET'])
def obtener_promedios():
    alumnos_promedio=[]
    for alumno in alumnos:
        promedio = 0
        if alumno["notas"]!=[]:
            for nota in alumno['notas']:
                promedio+= nota
            informe_alumno={
                "nombre":alumno["nombre"],
                "apellido":alumno["apellido"],
                "dni":alumno["dni"], 
                "promedio":promedio/len(alumno['notas'])
            }
            alumnos_promedio.append(informe_alumno)
    return jsonify({"Promedio de alumnos":sorted(alumnos_promedio,key=lambda x: x['promedio'])})   

#peticion DELETE: se elimina el alumno especificado con la ID, retorna el JSON.
@app.route('/alumnos/<int:id>',methods=['DELETE'])
def quitar_alumno(id):
    for alumno in alumnos:
        if alumno['id']==id:
            alumnos.remove(alumno)
            return jsonify(alumno)   
    return alumno_no_encontrado("El alumno no fue encontrado")    

#peticion PUT: se edita la nota del alumno especificado con la ID, retorna el JSON. 
@app.route('/alumnos/<int:id>',methods=['PUT'])
def editar_nota(id): 
    alumno = [alumno for alumno in alumnos if alumno['id'] == id]
    alumno[0]['notas'] = request.json['notas']
    return jsonify(alumno[0])

#peticion GET: retorna el JSON de alumnos ordenados de manera ascendente segun apellido.
@app.route('/alumnos/asc',methods=['GET'])
def obtener_alumnos_apellido_ascendente():
    ordenados = sorted(alumnos,key=lambda x: x['apellido'])
    return jsonify(ordenados)

@app.errorhandler(404)
def alumno_no_encontrado(error="error"):
    mensaje = {"mensaje":error}
    return make_response(jsonify(mensaje),404)

@app.errorhandler(400)
def error_al_crear_alumno(error="error"):
    mensaje = {"mensaje":error}
    return make_response(jsonify(mensaje),400)

if __name__ == '__main__':
    app.run(debug=True)