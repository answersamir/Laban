CFLAGS = -g
CC = gcc
#CXX = i686-w64-mingw32-g++
CXX = g++
executables = led lintel compln prfrm viewc frad3c split3e shadoq raselr nudes 

all: ${executables}

led: led.cpp
	$(CXX) -I /usr/include/GL led.cpp -o led -lm -lglut -lGL

lintel: lintel.cpp
	$(CXX) -g lintel.cpp -o lintel

compln: compln.c
	$(CC) compln.c -o compln -lm

prfrm:  prfrm.c
	$(CC) prfrm.c -o prfrm -lm

viewc:  viewc.c
	$(CC) viewc.c -o viewc -lm

frad3c:  frad3c.c
	$(CC) frad3c.c -o frad3c

split3e: split3e.c
	$(CC) split3e.c -o split3e

shadoq:  shadoq.c
	$(CC) shadoq.c -o shadoq -lm

raselr:  raselr.c
	$(CC) raselr.c -o raselr -lm

nudes:  nudes.c
	$(CC) $(CFLAGS) nudes.c -o nudes
clean:
	rm -rf $(executables) *.tmp 
