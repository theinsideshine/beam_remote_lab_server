
#parametros del ensayo

# Lee por el puerto serie parametros de configuracion en formato json.
# {info:'all-params'}        Envia todos los parametros en formato json.
# {info:'all-calibration'}   Envia todos los parametros en formato json de calibracion de la flexion y el nivel de logeo.
# {info:'version'}           Envia  la version del firmware.
# {info:'status'}            Devuelve el estatus del ensayo.
# {info:'reaction_one'}      Devuelve la reaction1 del ensayo.
# {info:'reaction_two'}      Devuelve la reaction2 del ensayo.
# {info:'flexion'}           Devuelve la flexion del ensayo.
# {info:'st_mode'}           Devuelve el modo del ensayo.
# {info:'step_cal'}          Devuelve la cantidad de pasos contados para la calibracion de step_k.
# {info:'step_k'}            Constante de calibracion de flexion.
# {info:'log_level'}         Nivel de logeo por puerto serie.


# {log_level:'0'}       log_level:0=desactivado,
# {log_level:'1'}                 1=mensajes.
# {log_level:'2'}                 2=info control estandar.
# {log_level:'3'}                 3=info control arduino plotter.

# {cmd:'start'}       Comienza el ensayo.

# {m1_fwd:'50'}           Mueve 50 mm el motor 1 hacia adelante.
# {m1_rwd:'4'}            Mueve 4 mm el motor 1 hacia atras.
# {step_m1_fwd:'200'}     Mueve 200 pasos el motor 1 hacia adelante.
# {step_m1_rwd:'200'}     Mueve 200 pasos el motor 1 hacia atras.


# {m2_up:'5'}              Mueve 5 mm el motor 1 hacia arriba.
# {m2_down:'4'}            Mueve 4 mm el motor 1 hacia abajo.
# {step_m2_up:'200'}       Mueve 200 pasos el motor 2 hacia arriba.
# {step_m2_down:'200'}     Mueve 200 pasos el motor 2 hacia abajo.

 #   {cdd:'start',data:{distance:'20',force:'306'}} 


# {distance:'290'}      distance      Distancia en mm donde se aplica la fuerza.
# {force:'2000'}        force         Fuerza a aplicar en g.
# {reaction_one:'1'}    reaction_one  Fuerza de reaccion uno, en g.
# {reaction_two:'2'}    reaction_two  Fuerza de reaccion dos, en g.
# {flexion:'0.12630'}   flexion       Flexion del ensayo, en cm.
# {st_test:'1'}         st_test       0 ensayo desactivado. 
#                       st_test       1 ensayo activado. 
# {st_mode:'0'}         st_mode       ST_MODE_TEST                    0  ensayo activado.
#                                     ST_MODE_HOME_M2                 1 Va al home del motor 2.
#                                     ST_MODE_CELL                    2 Lee las celdas de carga.
#  {step_cal:'2000'}    step_cal      Devuelve la cantidad de pasos contados para la calibracion de step_k.
#  {step_k:'0.123456'}  step_k        Constante de calibracion de flexion.

products = [
        {"distance":55},
        {"force":1},
        {"reaction_one":0},
        {"reaction_two":0},
        {"flexion":3},
        {"st_test":0},
        {"log_level":0},
        {"step_k":0},
        {"step_cal":0}
    ]