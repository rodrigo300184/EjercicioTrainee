# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:16:16 2021

@author: rodri
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import MySQLdb

app =  Flask(__name__)

# MySQL Connection
db=MySQLdb.connect(
    host='rodrigo300184.mysql.pythonanywhere-services.com',
    user='rodrigo300184',
    passwd='Ropo6188',
    db='rodrigo300184$EjercicioTrainee')

# MySQL Connection2
#db=MySQLdb.connect(
 #   host='bpohkzf3droicpjkcs01-mysql.services.clever-cloud.com',
  #  user='uqfcymioymnc1aft',
   # passwd='eVCT0SXVQZTjcmBjyxsg',
    #db='bpohkzf3droicpjkcs01')

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = db.cursor()
    cur.execute('SELECT * FROM listado')
    datos = cur.fetchall()
    return render_template('index.html', base = datos)

@app.route('/agregar_vehiculo', methods=['POST'])
def agregar_vehiculo():
    if request.method =='POST':
        try:
            verificador_lleno = False
            verificador_patente = False
            marca = request.form['marca']
            modelo = request.form['modelo']
            color = request.form['color']
            patente = request.form['patente']
            if marca and modelo and color and patente:
                verificador_lleno = True
            if len(patente)==6:
                if patente[0:3].isalpha():
                    if patente[3:6].isdigit():
                        patente = patente.upper()
                        verificador_patente = True
                    else:
                        flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
                else:
                        flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
            elif len(patente)==7:
                if patente[0:2].isalpha():
                    if patente[3:5].isdigit():
                        if patente[6:7].isalpha():
                            patente = patente.upper()
                            verificador_patente = True
                        else:
                            flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
                    else:
                        flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
                else:
                    flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
            else:
                flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
            if verificador_lleno == True and verificador_patente == True:
                cur = db.cursor()
                cur.execute('INSERT INTO listado (Marca,Modelo,Color,Patente) VALUES (%s,%s,%s,%s)',(marca,modelo,color,patente))
                db.commit()
                flash('Vehículo Agregado Correctamente')
            else:
                flash('No puede haber campos vacíos')
        except Exception:
            flash('La patente ya pertenece a un vehículo')
    return redirect (url_for('index'))

@app.route('/editar_vehiculo/<string:id>')
def editar_vehiculo(id):
    cur = db.cursor()
    cur.execute('SELECT * FROM listado WHERE id = {}'.format(id))
    data = cur.fetchall()
    return render_template('editar_vehiculo.html', vehiculo = data[0])

@app.route('/actualizar_vehiculo/<string:id>', methods = ['POST'])
def actualizar_vehiculo(id):
    if request.method == 'POST':
        try:
            verificador_lleno = False
            verificador_patente = False
            marca = request.form['marca']
            modelo = request.form['modelo']
            color = request.form['color']
            patente = request.form['patente']
            if marca and modelo and color and patente:
                verificador_lleno = True
            if len(patente)==6:
                if patente[0:3].isalpha():
                    if patente[3:6].isdigit():
                        patente = patente.upper()
                        verificador_patente = True
                    else:
                        flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
                else:
                        flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
            elif len(patente)==7:
                if patente[0:2].isalpha():
                    if patente[3:5].isdigit():
                        if patente[6:7].isalpha():
                            patente = patente.upper()
                            verificador_patente = True
                        else:
                            flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
                    else:
                        flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
                else:
                        flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
            else:
                flash('La patente no posee un formato correcto del tipo AAA000 ó AA000BB')
            if verificador_lleno == True and verificador_patente==True:
                cur = db.cursor()
                cur.execute("""
                UPDATE listado
                SET Marca = %s,
                    Modelo = %s,
                    Color = %s,
                    Patente = %s
                WHERE
                id = %s
                """,(marca,modelo,color,patente,id))
                #db.connection.commit()
                flash('Vehículo Editado Correctamente')
            else:
                flash('No puede haber campos vacíos')
        except Exception:
            flash('La patente ya pertenece a un vehículo')
    return redirect(url_for('index'))


@app.route('/eliminar_vehiculo/<string:id>')
def eliminar_vehiculo(id):
    cur = db.cursor()
    cur.execute('DELETE FROM listado WHERE id = {}'.format(id))
    #db.connection.commit()
    flash('Vehículo Eliminado Correctamente')
    return redirect(url_for('index'))

if __name__=='__main__':
        app.run()
