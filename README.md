Lista de tareas
da fare (sujeto a cambios)

Eissan Charris
Edward Sanchez

Requisitos
Modificar, descompletar (?), eliminar

Crear                                                       [☑️]
1. Generar una ID                                           [☑️]
2. Recibir y poner el titulo de la tarea                    [☑️]
3. Recibir y poner la descripcion                           [☑️]
4. Recibir y poner la fecha limite                          [☑️]
5. Poner la fecha de creacion                               [☑️]

Completar                                                   []
1. Si ya paso la fecha limite y E="Pendiente" o             [☑️]
E="Atrasado" entonces DP=Date.today-FL              
2. Si checkbox esta marcada entonces E="Completo"           [☑️]
y FCOMP=date.today
4. Si checkbox no esta marcada y ya paso la fecha limite    [☑️]
entoces E="Atrasado"            
5. Si checkbox esta marcada y FL-FCOMP>0 entonces           [☑️]
E="Completo con retraso"
6. Si E="pendiente" color de fuente normal                  []
7. Si E="atrasado"  color de fuente rojo                    []
8. Si E="Completado" color de fuente normal, fondo          []
ligeramente oscuro                  
9. Si E="Completado con retraso" color de fuente rojo,      []
fondo ligeramente oscuro                  