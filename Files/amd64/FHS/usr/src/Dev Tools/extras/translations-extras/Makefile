CC = gcc
# Inclusão da flag -march=native para a compilação do módulo extra
CFLAGS = -Wall -Wextra -O2 -march=native -fPIC -I. -v

LIB_NAME = libdevtools-translations-extras.so

# Destinos finais no Bit-OS
LIB_DEST = /usr/lib64/bit-os
INC_DEST = "/usr/include/Dev Tools"
OBJ_DIR = "/System/Temporary System Files/Dev Tools"

OBJS = $(OBJ_DIR)/google.o

all: $(LIB_NAME)

$(LIB_NAME): $(OBJS)
	$(CC) -v -shared -o $(LIB_NAME) $(OBJS)

$(OBJ_DIR)/google.o: google.c google.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c google.c -o $(OBJ_DIR)/google.o

install: all
	sudo mkdir -p $(LIB_DEST)
	sudo mkdir -p $(INC_DEST)
	sudo cp $(LIB_NAME) $(LIB_DEST)/
	sudo cp google.h $(INC_DEST)/
	sudo ldconfig -v

clean:
	rm -v -f $(OBJS) $(LIB_NAME)

.PHONY: all install clean