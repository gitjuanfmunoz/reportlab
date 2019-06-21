from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("Figurasytxt.pdf",pagesize=letter)
c.setLineWidth(.8) #ancho de linea
c.setFont('Helvetica',18) #Fuente y Tamaño
c.drawString(275, 705, "Linea") #pos x, y en puntos
c.drawString(275, 500, "Circulo") #pos x, y en puntos
c.drawString(260, 250, "Rectangulo") #pos x, y en puntos
c.rect(150, 150, 300, 200) #Rectangulo (x, y, width, height)
c.circle(300, 510, 100, 1, 0)
c.line(200,698,400,698)

c.save()


      