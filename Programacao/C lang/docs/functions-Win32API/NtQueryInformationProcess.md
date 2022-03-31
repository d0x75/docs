NtQueryInformationProcess
---------------------------

- função da native API (ntdll.dll)
- recupera informações sobre um processo.
- primeiro parâmetro pra função é o handle do processo.
- segundo parâmetro = tipo de informação a ser recuperada.
- se o segundo parâmetro == 7 , é pra descobrir se está sendo debuggado ou não.
- Se o retorno == 0 ( não há debugger )
- Se o retorno != 0 ( há debugger )

