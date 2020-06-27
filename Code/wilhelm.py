import turtle as t
import math


s = t.getscreen()

bg = t.bgcolor("#ffffff")
color = t.color("#000000")
fill = t.fillcolor("#000000")



colors = {
	"Rot": "#fc0303",
	"Grün": "#24fc03",
	"Blau": "#0331fc",
	"Türkis": "#03e7fc",
	"Gelb": "#f0fc03",
	"Lila": "#f803fc",
	"Orange": "#fca503",
	"Pink": "#fc03b5",
	"Rosa": "#fc03b5",
	"Schwarz": "#000000",
	"Weiß": "#ffffff"
}

#----------------------------------------------------------------------------------

def farbe (stift, hintergrund, fill):
	t.bgcolor(hintergrund)
	t.color(stift)
	t.fillcolor(fill)

def quad(size):
	t.penup()
	t.bk(size/2)
	t.rt(90)
	t.fd(size/2)
	t.lt(90)
	t.pendown()
	position = t.pos()
	t.begin_fill()
	for i in range(3):
		t.fd(size)
		t.lt(90)
	t.goto(position)
	t.end_fill()

#----------------------------------------------------------------------------------

def dreieck (seite1, seite2, winkel1):
	t.begin_fill()
	position = t.pos()
	t.fd(seite1)
	t.lt(180 - winkel1)
	t.fd(seite2)
	t.goto(position)
	t.end_fill()
#----------------------------------------------------------------------------------

def gleichseitigesdreieck(size):
	t.begin_fill()
	t.penup()
	t.bk(size/2)
	t.rt(90)
	t.fd(size/2)
	t.lt(90)
	t.pendown()
	for i in range(2):
		t.fd(size)
		t.lt(120)
	t.fd(size)
	t.end_fill()


#----------------------------------------------------------------------------------

def kreis(radius, abschnitt):
	t.begin_fill()
	t.penup()
	t.right(90)
	t.forward(radius)
	t.left(90)
	t.pendown()
	t.circle(radius, abschnitt)
	t.end_fill()
#----------------------------------------------------------------------------------
def rechteck(size1, size2):
  t.penup()
  t.bk(size1/2)
  t.rt(90)
  t.fd(size2/2)
  t.lt(90)
  t.pendown()
  t.begin_fill()
  t.fd(size1)
  t.lt(90)
  t.fd(size2)
  t.lt(90)
  t.fd(size1)
  position=t.pos()
  t.lt(90)
  t.fd(size2)
  t.end_fill()
  return position
#----------------------------------------------------------------------------------
def stern(size):
  t.rt(108)
  t.begin_fill()
  for i in range(5):
	  t.fd(size)
	  t.rt(36)
	  t.fd(size)
	  t.rt(252)
  t.end_fill()

 #---------------------------------------------------------------------------------- 
def pentagramm(size):
  t.lt(72)
  t.begin_fill()
  for i in range(5):
   t.fd(size)
   t.penup()
   #t.fd(size)
   t.pendown()
   t.fd(size)
   t.rt(180-36)
  t.end_fill()
  t.begin_fill()
  t.end_fill()
#----------------------------------------------------------------------------------
def zauberstab(size):
  t.begin_fill()
  t.lt(30)
  pos = rechteck(20,size)
  t.penup()
  t.goto(pos)
  t.fd(10)
  t.rt(180-54)
  t.fd(size/4)
  t.lt(180)
  t.pendown()
  pentagramm(size/4)
  t.end_fill()

#----------------------------------------------------------------------------------

def haus(size):
  quad(size)
  t.bk(size)
  t.lt(90)
  l=math.sqrt(size**2/2)
  dreieck(size,l,45)

#----------------------------------------------------------------------------------

f = input("Möchtest du die Farben wählen?: ")
if f == "Ja" or f == "ja":
	f = input("Möchtest du die Farben in Hexadezimal angeben?: ")
	if f == "Ja" or f == "ja":
		t.bgcolor(input("Wähle eine Stiftfarbe: "))
		t.color(input("Wähle eine Hintergrundfarbe: "))
		t.fillcolor(input("Wähle eine Füllfarbe: "))
	else:
		s = input ("Wähle eine Stiftfarbe: ")
		h = input ("Wähle eine Hintergrundfarbe: ")
		f = input ("Wähle eine Füllfarbe: ")
		farbe(colors.get(s), colors.get(h), colors.get(f))
print("Es gibt:\nKreis\nQuadrat\ngleichseitiges Dreieck\nDreieck\nStern\nPentagramm\nHaus\nRechteck\nZauberstab")
print(".\n.\n.")
x =  input("Wähle eine Form: ")
if x == "Kreis":
  r = float(input ("Wähle einen Radius: "))
  a = float(input ("Wähle einen Abschnitt: "))
  kreis (r, a)
elif x == "Quadrat":
  l = float(input ("Wähle eine Seitenlänge: "))
  quad(l)
elif x == "Rechteck":
	l = float(input("Wähle eine Seitenlänge: "))
	w = float(input("Wähle eine Seitenbreite: "))
	rechteck(l, w)
elif x == "Stern":
  l = float(input ("Wähle eine Seitenlänge: "))
  stern(l)
elif x == "Pentagramm":
  l = float(input ("Wähle eine Seitenlänge: "))
  pentagramm(l)
elif x == "Haus":
  l=float(input("Wähle eine Seitenlänge: "))
  haus(l)
elif x == "Zauberstab":
  l = float(input ("Wähle eine Stablänge: "))
  zauberstab(l)
elif x == "gleichseitiges Dreieck":
  l = float(input ("Wähle eine Seitenlänge: "))
  gleichseitigesdreieck (l)
elif x == "Dreieck":
	l1 = float(input("Wähle eine Seitenlänge für die erste Seite: "))
	l2 = float(input("Wähle eine Seitenlänge für die zweite Seite: "))
	w1 = float(input("Wähle einen ersten Winkel für das Dreieck: "))


	if (w1 >= 180):
		print("Error!\n Das Dreieck konnte wegen zu großen Winkeln nicht erstellt werden.")
		
	else:
		dreieck(l1, l2, w1)
	
else:
	print("Error! Bitte schreibe nur eine der möglichen Antworten")