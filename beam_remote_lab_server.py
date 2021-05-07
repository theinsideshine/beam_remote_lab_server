#https://www.youtube.com/watch?v=Esdj9wlBOaI min 18

from flask import Flask, jsonify, request
from serial_device import SerialDevice
import sys
import json  #pip install 
import time

ser = SerialDevice()
json_fields = {} 

if ser.open('COM3'): #Si no encuentra el COM LO BUSCA    
    print("Conectado.")
else:
   print("Error al abrir puerto.")
   sys.exit("Programa abortado.")
time.sleep(3)# arduino al iniciliarse el puerto serie ser resetea, este delay es para esperar que pase el reset 

app =  Flask(__name__)

from config import products

@app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})

@app.route('/parameters')
def getParameters():
    ser.send_cmd("{info:'all-params'}") 
    json_fields = ser.read_answer()   
   # return (json_fields)
    return jsonify(json_fields)


@app.route('/parameters/distance/<string:distance>', methods=['PUT'])
def putParmDistance(distance):    
    ser.send_cmd("{distance:'"+distance+"'}")    
    json_fields = ser.read_answer()   
    return jsonify(json_fields)


@app.route('/parameters/force/<string:force>', methods=['PUT'])
def putParmForce(force):
    ser.send_cmd("{force:'"+force+"'}")    
    json_fields = ser.read_answer()   
    return jsonify(json_fields)

@app.route('/comands/info/<string:information>', methods=['PUT'])
def putCmdInfo(information):
    ser.send_cmd("{info:'"+information+"'}")    
    json_fields = ser.read_answer()   
    return jsonify(json_fields)
    
    


#testgit
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=4000)
    
    