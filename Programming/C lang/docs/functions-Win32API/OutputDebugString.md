OutputDebugString
------------------

- Utilizada para enviar uma string pro debugger exibir.
- Se a função for chamada e não houver debugger, retornará erro.
- Se a função for chamada sem retornar erro, é quando há debugger.
- Através do retorno do erro ou não .. descobrimos se há debugger ou não.