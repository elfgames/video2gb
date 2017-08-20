#include "frame_banks.h"

void use_frame_bank(UINT16 frame, unsigned char * b) NONBANKED {
    switch(frame)
    {
        case 114: *b = 3; break;
        case 273: *b = 4; break;
        case 387: *b = 5; break;
        case 516: *b = 6; break;
        case 596: *b = 7; break;
        case 687: *b = 8; break;
        case 796: *b = 9; break;
        case 897: *b = 10; break;
        case 995: *b = 11; break;
        case 1123: *b = 12; break;
        case 1212: *b = 13; break;
        case 1320: *b = 14; break;
        case 1436: *b = 15; break;
        case 1554: *b = 16; break;
        case 1646: *b = 17; break;
        case 1758: *b = 18; break;
        case 1890: *b = 19; break;
        case 2016: *b = 20; break;
        case 2114: *b = 21; break;
        default: break;
    }
}
