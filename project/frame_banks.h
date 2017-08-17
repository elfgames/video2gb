unsigned char use_frame_bank(unsigned long frame) {
	switch(frame)
	{
		case 0: return 2;
		case 147: return 3;
		case 250: return 4;
		case 337: return 5;
		case 435: return 6;
		case 572: return 7;
		case 708: return 8;
		case 810: return 9;
		case 922: return 10;
		case 1103: return 11;
		case 1228: return 12;
		case 1327: return 13;
		case 1421: return 14;
		default: return 1;
	}
}
