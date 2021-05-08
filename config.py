# Lee por el puerto serie parametros de configuracion en formato json.
# Comandos
# {info:'all-params'}   Envia todos los parametros en formato json.
# {info:'version'}      Envia  la version del firmware.
# {info:'status'}       Envia  es estatus del ensayo.
# {info:'reaction_one'} Devuelve la reaccion 1 del ensayo.
# {info:'reaction_two'} Devuelve la reaccion 2 del ensayo.
# {info:'flexion'}      Devuelve la flexion  del ensayo.
# {cmd:'start'}   Comienza el ensayo


#parametros del ensayo

# {distance:'500'}       distance:0 a 254       Distancia en cm donde se aplica la fuerza.
# {force:'11'}          force:0 a 254          Fuerza a aplicar en Kg.
# {reaction_one:'1'}    reaction_one :0 a 254  Fuerza de reaccion uno, en Kg.
# {reaction_two:'2'}    reaction_two :0 a 254  Fuerza de reaccion dos, en Kg.
# {flexion:'3'}         flexion :0 a 254       Flexion del ensayo, en mm.
# {st_test:'1'}         st_test : 0 ensayo desactivado. 
#                       st_test : 1 ensayo activado.
# {log_level:'0'}       log_level:0=desactivado,
#                                 1=mensajes.
#                                 2=info control estandar.
#                                 3=info control arduino plotter.

products = [
        {"distance":55},
        {"force":1},
        {"reaction_one":0},
        {"reaction_two":0},
        {"flexion":3},
        {"st_test":0},
        {"log_level":0}
    ]