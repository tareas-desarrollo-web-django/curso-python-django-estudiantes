from django.shortcuts import render
from django.views import View


def vista_funcion(request):
    r""" Vista basada en funciones """
    if request.method == 'GET':
        return render(request, 'bases/index.html', {'tarjetas':range(8)})
    elif request.method == 'POST':
        return render(request, 'bases/index.html', {'tarjetas':range(8), 'datos':request.POST})


class VistaClase(View):
    def get(self, request):
        r""" Para obtener información """
        return render(request, 'bases/index.html', {'tarjetas':range(12)})
    
    def post(self, request):
        r""" Para crear información """
        return render(request, 'bases/index.html', {'tarjetas':range(12), 'datos':request.POST})

    def put(self, request):
        r""" Para crear información, similar a POST, pero el cliente decide el ID """
        ...

    def patch(self, request):
        r""" Para actualizar información """
        ...
    
    def delete(self, request):
        r""" Para eliminar información """
        ...
    
    def options(self, request):
        r""" Para obtener información de las opciones disponibles """
        ...


class VistaPlantilla(View):
    plantilla = None
    contexto_extra = {}

    def get(self, request):
        if not hasattr(self.__class__, 'plantilla') or self.plantilla is None:
            raise AttributeError("No se ha definido una plantilla")

        return render(request, self.plantilla, self.contexto_extra)

    def post(self, request):
        if not hasattr(self.__class__, 'plantilla') or self.plantilla is None:
            raise AttributeError("No se ha definido una plantilla")

        contexto = {'datos':request.POST}

        contexto.update(self.contexto_extra)
        return render(request, self.plantilla, contexto)


class MiPlantilla(VistaPlantilla):
    plantilla = 'bases/index_2.html'
    contexto_extra = {'mensaje':'Envía el formulario!'}




