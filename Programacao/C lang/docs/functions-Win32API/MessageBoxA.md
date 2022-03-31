MessageBoxA
-------------

Função que exibe uma caixa de diálogo com uma mensagem e um título na janela.


**Protótipo** :

	int WINAPI MessageBox(
	    _In_opt_ HWND    hWnd,
	    _In_opt_ LPCTSTR lpText,
	    _In_opt_ LPCTSTR lpCaption,
	    _In_     UINT    uType
	);


- Parâmetros da função MessageBoxA:

#### hWnd [entrada, opcional]

Um handle que identifica qual janela é dona da caixa de mensagem. Isso serve para atrelar uma mensagem a uma certa janela (e impedi-la de ser fechada antes da caixa de mensagem, por exemplo). Como é opcional, este parâmetro pode ser NULL, o que faz com que a caixa de mensagem não possua uma janela dona.

#### lpText [entrada, opcional]

Um ponteiro para um texto (uma string) que será exibido na caixa de mensagem. Se for NULL, a mensagem não terá um conteúdo, mas ainda assim aparecerá.

#### lpCaption [entrada, opcional]

Um ponteiro para o texto que será o título da caixa de mensagem. Se for NULL a caixa de mensagem não terá um título, mas ainda aparecerá.

#### uType [entrada]

Parâmetro que seta o tipo da caixa de diálogo, cada tipo tem seu padrão e designer próprio. Exemplos:


	MB_OKCANCEL (0x01)

	MB_ICONEXCLAMATION (0x30)

	MB_OKCANCEL | MB_ICONEXCLAMATION



- Observação: Dizer que um parâmetro é opcional não quer dizer que você não precise passá-lo ao chamar a função, mas sim que ele pode ser NULL, ou zero, dependendo do que a documentação da função diz.

---

- Exemplo em C :

		int main(void)

		{

			MessageBoxA(
				NULL,
				"Eduardo",
				"d0x75",
				MB_OK | MB_ICONEXCLAMATION
			);
		return 0;

		}


---
