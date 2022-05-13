ALL: 	pswd \
		moveFile \
		convertImage \
		moveImage \
		makeVisualCrypt

pswd:
	cd createPswd/ && \
	make && \
	./createPswd p5wd.txt 8

moveFile:
	mv ./createPswd/*.txt ./convertToImage/usePython

convertImage:
	cd convertToImage/usePython && \
	cat *.txt && \
	python3 convertPython.py *.txt

moveImage:
	mv ./convertToImage/usePython/*.bmp ./visualCrypt/

makeVisualCrypt:
	cd visualCrypt && \
	./createVisualCrypt.py *.bmp && \
	rm -f *.bmp

clean: cleanOne \
	   cleanTwo \
	   cleanThree

cleanOne:
	cd createPswd/ && \
	make clean

cleanTwo:
	cd convertToImage/ && \
	make clean && \
	rm -f *.txt

cleanThree:
	rm -f ./visualCrypt/*.png
