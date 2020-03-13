ALL: 	pswd \
		moveFile \
		convertImage \
		moveImage \
		makeVisualCrypt \
		moveCrypt \
		sendImage

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

makeVisualCrypt:
	cd visualCrypt && \
	./createVisualCrypt.py test.bmp && \
	rm -f test.bmp

moveCrypt:
	mv ./visualCrypt/out1.png ./emailImage/ && \
	mv ./visualCrypt/out2.png ./emailImage/

sendImage:
	cd emailImage

clean: cleanOne \
	   cleanTwo \
	   cleanThree

cleanOne:
	cd createPswd/ && \
	make clean

cleanTwo:
	cd convertToImage/ && \
	make clean && \
	rm -f p5wd.txt

cleanThree:
	rm -f ./visualCrypt/decryptedPswd.png ./emailImage/out1.png /emailImage/out2.png
