# OBJECTS=img/architettura-sp.pdf
# SOURCES=img/architettura.tex img/architettura-sp.tex

default: all

all:
	latexmk -pdf -shell-escape main.tex
	# -cd change to directory of source file when processing it 
	latexmk -pdf -cd -shell-escape img/architettura-sp.tex
	# convert pdf file to vectorized image
	pdf2svg img/architettura-sp.pdf img/architettura-sp.svg

# $(OBJECTS): $(SOURCES)

continuous:
	latexmk -pdf -pvc -interaction=batchmode -shell-escape main.tex 

clean:
	# clean all aux files (including pdf, dvi, etc.)
	latexmk -C
	rm -f main.run.xml main.bbl main-figure*
	# enter ./img/ and execute the Makefile with the target 'clean'
	$(MAKE) -C img clean

