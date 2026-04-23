from persona import persona

juan = persona("juan", "castellanos", 15)
juan.mostrarpersona()

leidy = persona("leidy", "alvarez", 18)
leidy.mostrarpersona()

leidy.apellidos = "perez"
leidy.mostrarpersona()

juan = leidy
juan.mostrarpersona()