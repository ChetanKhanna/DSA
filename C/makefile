LinkedList: LinkedListMain.c LinkedListOps.o
	gcc -o LinkedList ./LinkedListMain.c ./LinkedListOps.o 
	@echo executable generated
LinkedListOps.o: LinkedListOps.c
	gcc -c LinkedListOps.c
	@echo object code generated
clean:
	rm LinkedList.o
	@echo clean complete
