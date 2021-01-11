from PriorityQueue import PriorityQueue

cp = PriorityQueue()

maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["Juan P", "Diego H"]}
niños = {"prioridad":2 , "descripcion":"Niños" , "personas":["Santi H", "Angel H"]}
mecanicos = {"prioridad":4 , "descripcion":"Mecanicos" , "personas":["Diana T", "Maria Z"]}
mujeres = {"prioridad":3 , "descripcion":"Mujeres" , "personas":["Valentina M", "Veronica L"]}
tercera_edad = {"prioridad":2 , "descripcion":"3ra edad" , "personas":["Teresa G", "Carmen B"]}
ninias = {"prioridad":1 , "descripcion":"Niñas" , "personas":["Victoria M", "Camila R"]}
hombres = {"prioridad":3 , "descripcion":"Hombres" , "personas":["Miguel M", "Miguel M"]}
vigia = {"prioridad":4 , "descripcion":"Vigia" , "personas":["Francisco O"]}
capitan = {"prioridad":5 , "descripcion":"Capitan" , "personas":["Jose M"]}
timonel = {"prioridad":4 , "descripcion":"timonel" , "personas":["Hugo R"]}

cp.enqueue(maestres['prioridad'] , maestres)
cp.enqueue(niños['prioridad'] , niños)
cp.enqueue(mecanicos['prioridad'] , mecanicos)
cp.enqueue(mujeres['prioridad'], mujeres)
cp.enqueue(tercera_edad['prioridad'], tercera_edad)
cp.enqueue(ninias['prioridad'], ninias)
cp.enqueue(hombres['prioridad'], hombres)
cp.enqueue(vigia['prioridad'], vigia)
cp.enqueue(capitan['prioridad'], capitan)
cp.enqueue(timonel['prioridad'], timonel)
cp.to_string()
