
CFLAGS = -std=c++11 -Wall -pedantic

.PHONY: fclean

bin/main: bin/main.o bin/game.o bin/ObjectField.o
	g++ -g -o main bin/main.o bin/game.o bin/ObjectField.o $(CFLAGS) -lncurses

bin/main.o: src/main.cpp
	mkdir -p bin
	g++ -g -c -o bin/main.o src/main.cpp $(CFLAGS)

bin/ObjectField.o: src/ObjectField.cpp src/ObjectField.h
	mkdir -p bin
	g++ -g -c -o bin/ObjectField.o src/ObjectField.cpp $(CFLAGS)

bin/game.o: src/game.cpp src/game.h
	mkdir -p bin
	g++ -g -c -o bin/game.o src/game.cpp $(CFLAGS)

fclean:
	rm -rf bin
	rm main






