all:
	latexmk -pdf main.tex
	pdf2svg architettura.pdf architettura.svg

continuous:
	latexmk -pdf -pvc main.tex

clean:
	latexmk -c
