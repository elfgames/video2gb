#include "frame_banks.h"

void use_frame_bank(UINT16 frame, unsigned char * b) NONBANKED {
	switch(frame)
	{
		case 0: *b = 2; break;
		case 147: *b = 3; break;
		case 250: *b = 4; break;
		case 337: *b = 5; break;
		case 435: *b = 6; break;
		case 572: *b = 7; break;
		case 708: *b = 8; break;
		case 810: *b = 9; break;
		case 922: *b = 10; break;
		case 1103: *b = 11; break;
		case 1228: *b = 12; break;
		case 1327: *b = 13; break;
		case 1421: *b = 14; break;
		default: break;
	}
}
