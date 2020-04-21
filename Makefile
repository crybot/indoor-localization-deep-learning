all:
	latexmk -pdf main.tex

continuous:
	latexmk -pdf -pvc main.tex

clean:
	latexmk -c
