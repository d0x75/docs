Os componentes React podem ter estado (state) configurando *this.state* em seus construtores. *this.state* deve ser considerado como privado para o componente React que o definiu. Exemplo do constructor que deve ter no componente  para trabalhar como 'state'. :


	  constructor(props){
	    super(props);
	    this.state = {
	      value: null
	    };
	  }


Em classes JavaScript, você sempre precisa chamar super ao definir o construtor de uma subclasse. Todas os componentes de classe React que possuem um método constructor devem iniciá-lo com uma chamada super (props).



Exemplo completo referente a *state* :


		class Square extends React.Component {
		  constructor(props) {
		    super(props);
		    this.state = {
		      value: null,
		    };
		  }

		  render() {
		    return (
		      <button
		        className="square"
		        onClick={() => this.setState({value: 'X'})}
		      >
		        {this.state.value}
		      </button>
		    );
		  }
		}


Ao chamar this.setState a partir de um manipulador onClick no método render do componente Square, nós dizemos ao React para renderizar novamente aquele Square sempre que seu <button> for clicado

Após a atualização, o this.state.value do Square será 'X', então vamos ver o X no tabuleiro do jogo. Se você clicar em qualquer quadrado, um X deve aparecer.

Quando você chama setState em um componente, o React atualiza automaticamente os componentes filhos dentro dele também.