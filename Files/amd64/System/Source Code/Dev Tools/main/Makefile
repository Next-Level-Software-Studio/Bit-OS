CC = gcc
# Inclusão da flag -march=native junto às outras regras estritas e verbosas
CFLAGS = -Wall -Wextra -O2 -march=native -fPIC -I. -v

LIB_NAME = libdevtools.so

# Destinos finais no Bit-OS
LIB_DEST = /usr/lib64/bit-os
INC_DEST = "/usr/include/Dev Tools"
OBJ_DIR = "/System/Temporary System Files/Dev Tools"

OBJS = $(OBJ_DIR)/disks.o \
       $(OBJ_DIR)/files.o \
       $(OBJ_DIR)/folders.o \
       $(OBJ_DIR)/symlinks.o \
       $(OBJ_DIR)/load.o \
       $(OBJ_DIR)/search.o \
       $(OBJ_DIR)/tab.o \
       $(OBJ_DIR)/value.o \
       $(OBJ_DIR)/management.o \
       $(OBJ_DIR)/t.o

all: $(LIB_NAME)

$(LIB_NAME): $(OBJS)
	$(CC) -v -shared -o $(LIB_NAME) $(OBJS)

# Compilação manual de cada objeto garantindo a criação do diretório
$(OBJ_DIR)/disks.o: filemanagement/disks.c filemanagement/disks.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c filemanagement/disks.c -o $(OBJ_DIR)/disks.o

$(OBJ_DIR)/files.o: filemanagement/files.c filemanagement/files.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c filemanagement/files.c -o $(OBJ_DIR)/files.o

$(OBJ_DIR)/folders.o: filemanagement/folders.c filemanagement/folders.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c filemanagement/folders.c -o $(OBJ_DIR)/folders.o

$(OBJ_DIR)/symlinks.o: filemanagement/symlinks.c filemanagement/symlinks.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c filemanagement/symlinks.c -o $(OBJ_DIR)/symlinks.o

$(OBJ_DIR)/load.o: registry/load.c registry/load.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c registry/load.c -o $(OBJ_DIR)/load.o

$(OBJ_DIR)/search.o: registry/search.c registry/search.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c registry/search.c -o $(OBJ_DIR)/search.o

$(OBJ_DIR)/tab.o: registry/tab.c registry/tab.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c registry/tab.c -o $(OBJ_DIR)/tab.o

$(OBJ_DIR)/value.o: registry/value.c registry/value.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c registry/value.c -o $(OBJ_DIR)/value.o

$(OBJ_DIR)/management.o: translations/management.c translations/management.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c translations/management.c -o $(OBJ_DIR)/management.o

$(OBJ_DIR)/t.o: translations/t.c translations/t.h
	sudo mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c translations/t.c -o $(OBJ_DIR)/t.o

install: all
	sudo mkdir -p $(LIB_DEST)
	sudo mkdir -p $(INC_DEST)/filemanagement
	sudo mkdir -p $(INC_DEST)/registry
	sudo mkdir -p $(INC_DEST)/translations
	sudo cp $(LIB_NAME) $(LIB_DEST)/
	sudo cp filemanagement/*.h $(INC_DEST)/filemanagement/
	sudo cp registry/*.h $(INC_DEST)/registry/
	sudo cp translations/*.h $(INC_DEST)/translations/
	sudo ldconfig -v

clean:
	rm -v -f $(OBJS) $(LIB_NAME)

.PHONY: all install clean