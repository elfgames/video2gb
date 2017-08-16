..\bin\lcc -Wa-l -Wf-ba0 -c -o saveslot1.o saves/saveslot1.c
..\bin\lcc -Wa-l -Wf-bo1 -c -o bg.o background/bg.s
..\bin\lcc -Wa-l -Wf-bo2 -c -o frames1.o background/frames1.s
..\bin\lcc -Wa-l -Wf-bo3 -c -o frames2.o background/frames2.s
..\bin\lcc -Wa-l -Wf-bo4 -c -o frames3.o background/frames3.s
..\bin\lcc -Wa-l -Wf-bo5 -c -o frames4.o background/frames4.s
..\bin\lcc -Wa-l -Wf-bo6 -c -o frames5.o background/frames5.s
..\bin\lcc -Wa-l -Wf-bo7 -c -o frames6.o background/frames6.s
..\bin\lcc -Wa-l -Wf-bo8 -c -o frames7.o background/frames7.s
..\bin\lcc -Wa-l -Wf-bo9 -c -o frames8.o background/frames8.s
..\bin\lcc -Wa-l -Wf-bo10 -c -o frames9.o background/frames9.s
..\bin\lcc -Wa-l -Wf-bo11 -c -o frames10.o background/frames10.s
..\bin\lcc -Wa-l -Wf-bo12 -c -o frames11.o background/frames11.s
..\bin\lcc -Wa-l -Wf-bo13 -c -o frames12.o background/frames12.s
..\bin\lcc -Wa-l -Wf-bo14 -c -o frames13.o background/frames13.s
..\bin\lcc -Wa-l -Wf-bo15 -c -o frames14.o background/frames14.s
..\bin\lcc -Wa-l -Wf-bo16 -c -o frames15.o background/frames15.s
..\bin\lcc -Wa-l -Wf-bo17 -c -o frames16.o background/frames16.s
..\bin\lcc -Wa-l -Wf-bo18 -c -o frames17.o background/frames17.s
..\bin\lcc -Wa-l -Wf-bo19 -c -o frames18.o background/frames18.s
..\bin\lcc -Wa-l -Wf-bo20 -c -o frames19.o background/frames19.s
..\bin\lcc -Wa-l -Wf-bo21 -c -o frames20.o background/frames20.s

..\bin\lcc -Wa-l -Wf-bo30 -c -o indexes.o background/indexes.s

..\bin\lcc -Wa-l -c -o rle_lib.o gbdk-lib-extension/rle_lib.c
..\bin\lcc -Wa-l -c -o main.o main.c
..\bin\lcc -Wl-yt3 -Wl-yo32 -Wl-ya4 -o video.gb indexes.o main.o saveslot1.o rle_lib.o bg.o frames1.o frames2.o frames3.o frames4.o frames5.o frames6.o frames7.o frames8.o frames9.o frames10.o frames11.o frames12.o frames13.o frames14.o frames15.o frames16.o frames17.o frames18.o frames19.o frames20.o

del *.o
del *.lst

