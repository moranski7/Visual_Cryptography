D = gdc
DFLAGS = -Wall -pedantic -Werror -g
DEBUG = 
OFLAG = -o
.SUFFIXES: .d .o
.d.o:
	$(D) $(DFLAGS) -c $<

createPswd: createPswd.o
	$(D) $(DFLAGS) $^ $(OFLAG) $@

createPswd.o: createPswd.d

clean:
	rm -f *.o createPswd p5wd.txt
