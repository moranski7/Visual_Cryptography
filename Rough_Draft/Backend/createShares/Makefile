ALL: 	getInfo \
		moveBlankFile \
		pswd \
		moveFile \
		convertImage \
		moveImage \
		makeVisualCrypt \
		moveCrypt \
		sendImage \
		moveImgToStorage \

getInfo:
	cd getUserInfo/ && \
	make

moveBlankFile:
	mv ./getUserInfo/*.txt ./createPswd/

pswd: 
	cd createPswd/ && \
	make && \
	./createPswd *.txt

moveFile:
	mv ./createPswd/*.txt ./convertToImage/usePython

convertImage:
	cd convertToImage/usePython && \
	python convertPython.py *.txt && \
	cat *.txt

moveImage:
	mv ./convertToImage/usePython/*.bmp ./visualCrypt/ 

makeVisualCrypt:
	cd visualCrypt && \
	./createVisualCrypt.py *.bmp && \
	rm -f *.bmp

moveCrypt:
	mv ./visualCrypt/*out1.png ./emailImage/ && \
	mv ./visualCrypt/*out2.png ./emailImage/

sendImage:
	cd emailImage && \
	./sendImage.py *out2.png jw666 && \
	rm -f *out2.png

moveImgToStorage:
	mv ./emailImage/*out1.png ./storeImage/

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
	rm -f ./visualCrypt/decryptedPswd.png ./storeImage/*out1.png ./emailImage/*out2.png
