from pyplasm import *

def facciate():
	#north
	base_facciata_scarna = MKPOL([[[-1.5,1],[1.5,1],[1.5,0],[-1.5,0]],[[1,2,3,4]],None])
	facciata_superiore_scarna = MKPOL([[[-1.5,1],[1.5,1],[1.5,4],[-1.5,4]],[[1,2,3,4]],None])
	tetto = MKPOL([[[-1.5,4],[1.5,4],[0,5]],[[1,2,3]],None])

	 
	def semicerchio(r):
		def semicerchio1(p):
			return [r*COS(p[0]),r*SIN(p[0])]
		def intervallo(dens=16):
			return INTERVALS(PI)(dens) 
		return MAP(semicerchio1)(intervallo()) 
	#porte
	superiore_porta = COLOR(RED)(T([1,2])([1.1,1.5])(JOIN(semicerchio(0.2))))
	inferiore_porta = COLOR(RED)(MKPOL([[[0.9,1.5],[1.3,1.5],[1.3,1],[0.9,1]],[[1,2,3,4]],None]))
	porta_dx = STRUCT([superiore_porta,inferiore_porta])
	porta_sx = T([1])(-2.2)(porta_dx)
	#finestre
	finestra_dx = T([1,2])([-0.6,0.1])(inferiore_porta)
	finestra_sx = T([1,2])([-1,0])(finestra_dx)
	buchi_finestra = T([1,2])([-0.22, 1.1])(PROD([QUOTE([0.1,-0.01]*4), QUOTE([0.1,-0.01]*6)]))
	finestra_centrale = T([1,2])([0.65,-0.3])(SCALE([1,2])([1.3,1.3])(finestra_sx))
	rincavo_alto = COLOR(GREEN)(T([1,2])([-1.1,1])(porta_dx))
	finestra_alto = COLOR(BLUE)(T(2)(1.7)(DIFFERENCE([finestra_centrale,buchi_finestra])))

	facciata_superiore = STRUCT([facciata_superiore_scarna,finestra_alto,rincavo_alto,porta_dx,porta_sx,finestra_centrale, finestra_dx,finestra_sx])
	#tetto
	curva_esterno = JOIN(semicerchio(0.4))
	curva_interno = JOIN(semicerchio(0.2))
	curva = T(2)(4)(COLOR(GREEN)(DIFFERENCE([curva_esterno,curva_interno])))

	tetto_nord = STRUCT([tetto,curva])
	#facciata inferiore
	porta_basso_sx = T([1,2])([-0.5,-1])(porta_dx)
	porta_basso_centro = T(1)(-0.6)(porta_basso_sx)
	porta_basso_dx = T(1)(-0.6)(porta_basso_centro)

	base = STRUCT([base_facciata_scarna,porta_basso_sx,porta_basso_centro,porta_basso_dx])

	facciata_principale = STRUCT([tetto_nord,facciata_superiore,base])

	#east
	rettangolo1 = MKPOL([[[0,0],[1.5,0],[1.5,4],[0,4]],[[1,2,3,4]],None])
	rettangolo2 = COLOR(RED)(MKPOL([[[0,0],[3.5,0],[3.5,4],[0,4]],[[1,2,3,4]],None]))
	rettangolo2 = T(1)(1.5)(rettangolo2)

	freccia = STRUCT([tetto,base_facciata_scarna,facciata_superiore_scarna]) 
	freccia = COLOR(GREEN)(S([1,2])([0.4,0.8])(freccia))
	freccia = T(1)(2.7)(freccia)
	tetto_lat = COLOR(BLUE)(MKPOL([[[0,0],[3.2,0],[3.2,1],[0,1]],[[1,2,3,4]],None]))
	tetto_lat = T([1,2])([1.7,4])(tetto_lat)
	#VIEW(STRUCT([rettangolo2,rettangolo1,freccia, tetto_lat]))
	facciata_sinistra = T(1)(1.5)(R([1,3])(PI/2)(STRUCT([freccia,rettangolo1,rettangolo2,tetto_lat])))
	#west
	facciata_destra = T(1)(-1.5)(R([1,3])(PI/2)(STRUCT([freccia,rettangolo1,rettangolo2,tetto_lat])))
	#unione facciate 
	facciata_retro = T(3)(5)(STRUCT([base_facciata_scarna,facciata_superiore_scarna,tetto]))

	return STRUCT([facciata_principale,facciata_retro,facciata_sinistra,facciata_destra])

