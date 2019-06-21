import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

def export_to_pdf(data):
    c = canvas.Canvas("Reporte_Alumnos.pdf", pagesize=letter)
    w, h = letter
    max_rows_per_page = 45
    # Margin
    x_offset = 50
    y_offset = 50
    # Space between rows
    padding = 15
    
    xlist = [x + x_offset for x in [0, 150, 200, 250, 300, 380, 480]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    
    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()
    
    c.save()
data = [("NOMBRE ALUMNO", "NOTA 1", "NOTA 2", "NOTA 3", "PROM", "ESTADO")]
for i in range(1, 35):
    exams = [randint(0, 10) for _ in range(3)]
    avg = round(mean(exams), 2)
    state = "Aprobado" if avg >= 4 else "Reprobado"
    data.append((f"Alumno {i}", *exams, avg, state))
export_to_pdf(data)