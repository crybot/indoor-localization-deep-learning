OBJECTS=img/architettura.pdf
SOURCES=img/architettura.tex

default: all

all: $(OBJECTS)
	latexmk -pdf main.tex

$(OBJECTS): $(SOURCES)
	# -cd change to directory of source file when processing it 
	latexmk -pdf -cd img/architettura.tex
	# convert pdf file to vectorized image
	pdf2svg img/architettura.pdf img/architettura.svg

continuous:
	latexmk -pdf -pvc main.tex

clean:
	# clean all aux files (including pdf, dvi, etc.)
	latexmk -C
	# enter ./img/ and execute the Makefile with the target 'clean'
	$(MAKE) -C img clean

