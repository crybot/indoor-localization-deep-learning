OBJECTS=img/architettura.pdf
SOURCES=img/architettura.tex

default: all

all: $(OBJECTS)
	latexmk -pdf -shell-escape main.tex

$(OBJECTS): $(SOURCES)
	# -cd change to directory of source file when processing it 
	latexmk -bibtex -pdf -cd -shell-escape img/architettura.tex
	# convert pdf file to vectorized image
	pdf2svg img/architettura.pdf img/architettura.svg

continuous:
	latexmk -pdf -pvc -interaction=batchmode -shell-escape main.tex 

clean:
	# clean all aux files (including pdf, dvi, etc.)
	latexmk -C
	rm -f main.run.xml main.bbl main-figure*
	# enter ./img/ and execute the Makefile with the target 'clean'
	$(MAKE) -C img clean

