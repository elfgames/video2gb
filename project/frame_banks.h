unsigned char use_frame_bank(unsigned long frame) {
    switch(frame)
    {
        case 114: return 3;
        case 273: return 4;
        case 387: return 5;
        case 516: return 6;
        case 596: return 7;
        case 687: return 8;
        case 796: return 9;
        case 897: return 10;
        case 995: return 11;
        case 1123: return 12;
        case 1212: return 13;
        case 1320: return 14;
        case 1436: return 15;
        case 1554: return 16;
        case 1646: return 17;
        case 1758: return 18;
        case 1890: return 19;
        case 2016: return 20;
        case 2114: return 21;
        default: return 1;
    }
}
