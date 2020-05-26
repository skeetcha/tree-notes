CC=g++
CFLAGS=-Wall -std=c++11
HEADERS=
OBJECTS=main.obj
INCLUDEDIRS=-Iimgui -ID:/Documents/graphics/sdl/include
LIBDIRS=-LD:/Documents/graphics/sdl/lib -LD:/Documents/graphics/glew
LIBS=-lSDL2 -lSDL2main -lglew32 -lopengl32
EXECUTABLE=build/treenotes.exe
#-----------------------------------
all: $(EXECUTABLE)
	$(CC) $(OBJECTS) $(INCLUDEDIRS) $(LIBDIRS) $(LIBS) -o $(EXECUTABLE)

%.obj: %.cpp $(HEADERS)
	$(CC) $(CFLAGS) $(INCLUDEDIRS) -o $@ $<

clean:
	rm -rf *.obj $(EXECUTABLE)