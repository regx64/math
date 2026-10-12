PDF = ../pdf

all: $(PDF)/learning-notes.pdf $(PDF)/problem-notes.pdf $(PDF)/problem-sets.pdf $(PDF)/erdos1063-prime-k.pdf

$(PDF)/learning-notes.pdf: learning-notes.tex preamble.tex $(wildcard gen/*.tex)
	mkdir -p $(PDF) build
	xelatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	xelatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	cp build/learning-notes.pdf $@

$(PDF)/problem-notes.pdf: problem-notes.tex preamble.tex $(wildcard gen/*.tex)
	mkdir -p $(PDF) build
	xelatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	xelatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	cp build/problem-notes.pdf $@

$(PDF)/problem-sets.pdf: problem-sets.tex preamble.tex $(wildcard gen/*.tex)
	mkdir -p $(PDF) build
	xelatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	xelatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	cp build/problem-sets.pdf $@

$(PDF)/erdos1063-prime-k.pdf: erdos1063-prime-k.tex
	mkdir -p $(PDF) build
	pdflatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	pdflatex -output-directory=build -interaction=nonstopmode $< >/dev/null
	cp build/erdos1063-prime-k.pdf $@

clean:
	rm -rf build
