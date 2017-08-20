#include <gb/gb.h>
#include <gb/drawing.h>
#include <string.h>
#include <stdio.h>
//generical functions to simply display and move charas
#include "gbdk-lib-extension/rle_lib.h"


//definition of gameplay functions
#include "main.h"

unsigned char buffer[360];

void set_bkg_tiles_rle(unsigned char *d) {
	unsigned char * p = &buffer[0];	
	unsigned char * l1 = p+360;
	UBYTE j = 0, w = 0;
	for (; p != l1; ++d) {
		if (*(d) == 0xFFU)
		{
			if  (*(d+1) != 0xFFU)
			{
				++d;
				w = *(d+1);
				for (j = 0; j != w; ++j)
				{
					(*p) = *d;
					++p;
					if (p == l1)
						break;
				}
				++d;
			}
			else
			{
				++d;
				*p = *d;
				++p;
			}
		}
		else
		{
			*p = *d;
			++p;
		}
	}
}
extern unsigned char * frames[];
//extern unsigned char * getFrame2(UINT16 i) NONBANKED;
//extern unsigned char * frames2[];

//const unsigned char * banks = {106};

void main() {
	UINT16 i = 0, keys;
	UINT8 b = 2, syncronizer = 0, syncronizer2 = 0;
	unsigned char * actual_frame = 0;
	//reset all graphics
	DISPLAY_OFF;
	disable_interrupts();
	SPRITES_8x8;
	HIDE_SPRITES;
	HIDE_BKG;
	HIDE_WIN;
	printf("PRESS START TO PLAY!");
	SHOW_BKG;
	DISPLAY_ON;
	enable_interrupts();
	while(1)
	{
		wait_vbl_done();
		keys = joypad();
		if (keys & J_START)
			break;
	}

	DISPLAY_OFF;
	disable_interrupts();
	HIDE_BKG;
	init_graphics();
	//set up screen
	SHOW_BKG;
	DISPLAY_ON;
	enable_interrupts();
	//graphic loop start
	while(1) {
		if ((++syncronizer2 & 7) == 0)
			wait_vbl_done();
		if ((++syncronizer & 7) != 0)
			wait_vbl_done();
		//wait_vbl_done();
		keys = joypad();
		if (keys & J_DOWN)
			continue;

		if (i == 2189) {
			break;
		}

		++i;

		use_frame_bank(i, &b);

		SWITCH_ROM_MBC1(30);
		actual_frame = frames[i];
		SWITCH_ROM_MBC1(b);
		set_bkg_tiles_rle(actual_frame);
		wait_vbl_done();
		set_bkg_tiles(0, 0, 20, 18, &buffer[0]);
	}
	DISPLAY_OFF;
	disable_interrupts();
	HIDE_BKG;
	printf("Credits:\n Code: ProGM\n Music: Frash Pikass\n\nThanks for watching!");
	//set up screen
	SHOW_BKG;
	DISPLAY_ON;
	enable_interrupts();
	while(1) {
		wait_vbl_done();
	}
}
void init_graphics() NONBANKED {
	//background
	//swap to first bank memory
	SWITCH_ROM_MBC1(1);
	//start background loading
	set_bkg_data(0, 255, test_tiledata);
	//swap to second bank memory
	SWITCH_ROM_MBC1(2);
	set_bkg_tiles_rle(frame0);
	set_bkg_tiles(0, 0, 20, 18, &buffer[0]);
}
