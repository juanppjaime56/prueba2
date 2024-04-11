from django.shortcuts import render

def pagina1(request):

    doc = "<html><head><title></title></head><body><h1>hola</h1></body></html>"

    return render(request,"pagina.html",{})
