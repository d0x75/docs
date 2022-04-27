c lang
------


memset
Ex: (push 0x08, push 0x0, push EAX)
return = 




I/O
----


ReadFile() = retorna 1 quando consegue ler o arquivo e 0 quando não conseguir.



Criptografia
-------------

CryptDecrypt

Caixas de diálogo
-----------------

MessageBoxA
MessageBoxW
MessageBoxExA
MessageBoxExW
DialogBoxParamA
GetWindowTextA
GetDlgItemInt
GetDlgItemTextA
Janelas
EnableWindow
EnableMenuItem
EnableWindow


---


Entrada e saída (I/O)
----------------------

CreateFileA
CreateFileW
OpenFile
OpenFileMappingA
OpenFileMappingW
OpenMutexA
OpenMutexW
LoadLibraryA
LoadLibraryExA
LoadLibraryW
LoadLibraryExW
CreateFileMappingA
CopyFileA
CopyFileW
CopyFileExA
CopyFileExW
MoveFileA
MoveFileW
MoveFileExA
MoveFileExW
DeleteFileA
DeleteFileW
LoadCursorFromFileA
GetPrivateProfileStringA
GetPrivateProfileIntA


---


Registro
----------

RegOpenKeyA
RegOpenKeyExA
RegCloseKey
RegQueryValueA
RegEnumKeyExA
RegSetValueA
RegSetValueW
RegSetValueExA
RegSetValueExW


---


Data e hora
------------

SetSystemTime
GetLocalTime
SetLocalTime


---


Processos e threads
--------------------

CreateToolhelp32Snapshot
Process32First
Process32Next
Process32FirstW
Module32First
Module32Next
Module32FirstW
Module32NextW
Toolhelp32ReadProcessMemory
Heap32ListFirst
Heap32ListNext
Heap32First
Heap32Next
OpenProcess
TerminateProcess
ExitProcess
ExitThread
OpenProcessToken
ADVAPI32.DLL
OpenThreadToken (ADVAPI32.DLL)
ZwQueryInformationProcess (NTDLL.DLL)
ZwSetInformationThread (NTDLL.DLL)
WriteProcessMemory
CreateThread
CreateRemoteThread
CreateProcessA


---


Anti-debugging
---------------

IsDebuggerPresent
CheckRemoteDebuggerPresent
NtSetInformationThread (NTDLL.DLL)


---


Strings
--------

lstrcatA
lstrcmpA
lstrcpyA
lstrlenA


---


Disco
------

GetDiskFreeSpaceA
GetDriveTypeA


Undocumented
-------------

NtQueryInformationProcess
OutputDebugString