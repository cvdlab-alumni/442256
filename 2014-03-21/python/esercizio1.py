from pyplasm import *

def floors():
	#costruzione muro_abside
	pianta_quadrato_esterno = MKPOL([[[-2,2],[2,2],[2,-2],[-2,-2]],[[1,2,3,4]],None])
	pianta_quadrato_interno = MKPOL([[[-1.5,1.5],[1.5,1.5],[1.5,-1.5],[-1.5,-1.5]],[[1,2,3,4]], None])
	#VIEW(pianta_quadrato_interno)
	#VIEW(pianta_quadrato_esterno)
	#VIEW(pianta_quadrato)
	pianta_rettangolo_verticale_esterno = MKPOL([[[-1,2.5],[1,2.5],[1,-2.5],[-1,-2.5]],[[1,2,3,4]],None])
	pianta_rettangolo_verticale_interno = MKPOL([[[-0.8,2.5],[0.8,2.5],[0.8,-2.5],[-0.8,-2.5]],[[1,2,3,4]],None])
	#VIEW(pianta_rettangolo_verticale)
	pianta_rettangolo_orizzontale_esterno = R([1,2])(PI/2)(pianta_rettangolo_verticale_esterno)
	pianta_rettangolo_orizzontale_interno = R([1,2])(PI/2)(pianta_rettangolo_verticale_interno)
	#VIEW(pianta_rettangolo_verticale_interno)
	#VIEW(STRUCT([pianta_quadrato,pianta_rettangolo_verticale,pianta_rettangolo_orizzontale]))
	pianta_interno = STRUCT([pianta_quadrato_interno,pianta_rettangolo_verticale_interno,pianta_rettangolo_orizzontale_interno])
	#VIEW(pianta_interno)
	pianta_esterno = STRUCT([pianta_quadrato_esterno,pianta_rettangolo_verticale_esterno,pianta_rettangolo_orizzontale_esterno])
	pianta_interno2 = SCALE([1,2])([-0.9,-0.9])(pianta_esterno)
	#VIEW(pianta_esterno)
	muri = DIFFERENCE([pianta_esterno, pianta_interno])
	muri = T([1,2])([0.3,0])(muri)
	#VIEW(muri)

	#costruzione absidi
	def semicerchio(r):
		def semicerchio1(p):
			return [r*COS(p[0]),r*SIN(p[0])]
		def intervallo(dens=16):
			return INTERVALS(PI)(dens) 
		return MAP(semicerchio1)(intervallo()) 

	abside_esterno = JOIN(semicerchio(0.4))
	abside_interno = JOIN(semicerchio(0.2))
	muro_abside = DIFFERENCE([abside_esterno,abside_interno])
	abside_alto = T([1,2])([0.3, 2.5])(muro_abside)
	abside_destra = T([1,2])([0.3,0.3])(R([1,2])(-PI/2)(abside_alto))
	abside_sud = T([1,2])([0.3,0.3])(R([1,2])(-PI/2)(abside_destra))
	absidi = STRUCT([abside_alto,abside_destra,abside_sud])


	#costruzione colonne
	def costruttoreColonne() :
		numeroColonne = 6
		fattoreTraslazioneX = -1.6
		fattoreTraslazioneY = 0.3
		colonne = []
		for i in range(0,3):
			x_colonne= QUOTE([0.3,-0.4]*numeroColonne)
			y_colonne = QUOTE([0.3,-0.4]*1)
			riga_colonne = PROD([x_colonne, y_colonne])
			riga_colonne = T([1,2])([fattoreTraslazioneX, fattoreTraslazioneY])(riga_colonne)
			colonne.append(riga_colonne)
			numeroColonne-=2
			fattoreTraslazioneX+= 0.7
			fattoreTraslazioneY+= 0.7
		return colonne

	colonne_meta_superiore = STRUCT(costruttoreColonne())
	colonne_meta_inferiore = T(1)(0.6)(R([1,2])(PI)(colonne_meta_superiore))
	colonne = STRUCT([colonne_meta_inferiore, colonne_meta_superiore])
	#VIEW(colonne)

	#ingresso
	ingresso_esterno = MKPOL([[[-3.5,1.5],[-2.3,1.5],[-3.5,-1.5],[-2.3,-1.5]],[[1,2,3,4]],None])
	ingresso_interno_verticale = MKPOL([[[-3,1.5],[-2.7,1.5],[-3,-1.5],[-2.7,-1.5]],[[1,2,3,4]],None])
	ingresso_interno_orizzontale1 = MKPOL([[[-3.5,0.7],[-2.3,0.7],[-3.5,0.5],[-2.3,0.5]],[[1,2,3,4]],None])
	ingresso_interno_orizzontale2 = T(2)(-1.2)(ingresso_interno_orizzontale1)
	ingresso_interno_centrale = T([2])(-0.6)(ingresso_interno_orizzontale1)
	ingresso_interno_orizzontale = STRUCT([ingresso_interno_orizzontale1,ingresso_interno_orizzontale2,ingresso_interno_centrale])
	ingresso = DIFFERENCE([ingresso_esterno, ingresso_interno_orizzontale,ingresso_interno_verticale])
	#VIEW(ingresso)


	#primo piano
	first_floor = STRUCT([colonne,muri,absidi,ingresso])
	#VIEW(first_floor)

	#secondo piano
	second_floor = STRUCT([muri,absidi,ingresso])
	second_floor = T(3)(1)(second_floor)
	#VIEW(second_floor)

	return [second_floor,first_floor]

