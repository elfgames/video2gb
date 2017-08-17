..\gbdk\bin\lcc -Wa-l -Wf-ba0 -c -o saveslot1.o saves/saveslot1.c
..\gbdk\bin\lcc -Wa-l -Wf-bo1 -c -o bg.o background/bg.s
..\gbdk\bin\lcc -Wa-l -Wf-bo2 -c -o frames1.o background/frames1.s
..\gbdk\bin\lcc -Wa-l -Wf-bo3 -c -o frames2.o background/frames2.s
..\gbdk\bin\lcc -Wa-l -Wf-bo4 -c -o frames3.o background/frames3.s
..\gbdk\bin\lcc -Wa-l -Wf-bo5 -c -o frames4.o background/frames4.s
..\gbdk\bin\lcc -Wa-l -Wf-bo6 -c -o frames5.o background/frames5.s
..\gbdk\bin\lcc -Wa-l -Wf-bo7 -c -o frames6.o background/frames6.s
..\gbdk\bin\lcc -Wa-l -Wf-bo8 -c -o frames7.o background/frames7.s
..\gbdk\bin\lcc -Wa-l -Wf-bo9 -c -o frames8.o background/frames8.s
..\gbdk\bin\lcc -Wa-l -Wf-bo10 -c -o frames9.o background/frames9.s
..\gbdk\bin\lcc -Wa-l -Wf-bo11 -c -o frames10.o background/frames10.s
..\gbdk\bin\lcc -Wa-l -Wf-bo12 -c -o frames11.o background/frames11.s
..\gbdk\bin\lcc -Wa-l -Wf-bo13 -c -o frames12.o background/frames12.s
..\gbdk\bin\lcc -Wa-l -Wf-bo14 -c -o frames13.o background/frames13.s
..\gbdk\bin\lcc -Wa-l -Wf-bo30 -c -o indexes.o background/indexes.s
..\gbdk\bin\lcc -Wa-l -c -o rle_lib.o gbdk-lib-extension/rle_lib.c
..\gbdk\bin\lcc -Wa-l -c -o main.o main.c

..\gbdk\bin\lcc -Wl-yt3 -Wl-yo32 -Wl-ya4 -o video.gb indexes.o main.o saveslot1.o rle_lib.o bg.o frames1.o frames2.o frames3.o frames4.o frames5.o frames6.o frames7.o frames8.o frames9.o frames10.o frames11.o frames12.o frames13.o

del *.o
del *.lst

