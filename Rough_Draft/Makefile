ALL: 	pswd \
		moveFile \
		convertImage \
		moveImage

pswd: 
	cd createPswd/ && \
	make && \
	./createPswd

moveFile:
	mv ./createPswd/p5wd.txt ./convertToImage/usePython

convertImage:
	cd convertToImage/usePython && \
	python convertPython.py p5wd.txt && \
	cat "p5wd.txt"

moveImage:
	mv ./convertToImage/usePython/test.bmp ./visualCrypt/

clean: cleanOne \
	   cleanTwo

cleanOne:
	cd createPswd/ && \
	make clean

cleanTwo:
	cd convertToImage/ && \
	make clean && \
	rm -f p5wd.txt
