from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader



def probandoTemplate(self):
    ##miHtml = open("C:/Users/carlosdecabo/Desktop/17bis/17bis/Proyecto1/Proyecto1/plantillas/template1.html")
    ##plantilla = Template(miHtml.read())
    plantilla = loader.get_template('MVT_Carlos.html')
    ##miHtml.close()
    ##miContexto = Context() 
    ##documento = plantilla.render(miContexto)
    documento = plantilla.render()
    return HttpResponse(documento)


def home(request):
    return HttpResponse("<h1>Hola Este es el MVT de Carlos De cabo selecciona: http://127.0.0.1:8000/MVT para acceder al ejercicio </h1>")

