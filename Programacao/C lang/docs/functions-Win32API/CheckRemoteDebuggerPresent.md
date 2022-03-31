CheckRemoteDebuggerPresent
----------------------------


- Quase identifica ao IsDebuggerPresent
- Também faz a verificação do campo IsDebugged da PEB
- Pode fazer por si própria(no próprio processo), ou pode fazer isso para outro processo desde que seja passado o handle do processo pra ela.
