Win32 API
===========


- Uma API (Application Programming Interface) é uma interface para programar uma aplicação. No caso do Windows, consiste num conjunto de funções expostas para serem usadas por aplicativos, inclusive em user mode.

- Os aplicativos do Windows rodam em uma camada do Sistema Operacional conhecida como Ring 3 ou Userland. Porém esses programas precisam ser capazes de interagir com funções que ficam no Kernel do SO, em outra camada do Sistema Operacional que é conhecida como Ring 0 ou KernelLand. Existem funções da API do windows que permitem os aplicativos da Userland(Ring 3), solicitem uma operação específica ao Kernel.

- O código das APIs, geralmente ficam nas DLLs do windows ( Ex: A função Y da x.dll ).


- Interface de programação para aplicativos Windows.
- Nas linguagens de alto nível geralmente não são acessadas diretamente, funções próprias da linguagem fazem a chamada.
- Não é tão amigável para o programador.
- Possui 4 dlls principais:

1. kernel32.dll - file system,dispositivos,processo e memória
2. advapi32.dll - componentes do windows, registros e usuário
3. user32.dll   - janelas,elementos gráficos, botões etc..
4. gdi32.dll    - serviços gráficos de baixo nível (aonde inicia o acesso ao win32k.sys)


- Algumas funções dessas dlls são implementadas em user mode.
- Muitas funções requerem serviços de kernel mode(transição de privilegio)

No mundo Windows, a maioria das funções tem duas formas: a forma ANSI e a forma Unicode. O formulário ANSI termina com A e espera parâmetros ANSI. A forma Unicode termina com W e espera parâmetros Unicode. 

---