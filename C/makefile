BinTree: BinTreeMain.c BinTreeOps.o
	gcc -o BinTree ./BinTreeMain.c ./BinTreeOps.o
	./BinTree
	@echo executable generated
BinTreeOps.o: BinTreeOps.c
	gcc -c BinTreeOps.c
	@echo object code generated
clean:
	rm BinTreeOps.o
	@echo clean complete
