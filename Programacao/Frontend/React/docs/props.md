*props*


Passar 'props' é a forma como os dados fluem em aplicações React, de pais para filhos.
Exemplo de passar um “prop” de um componente Pai Filho.


	class Filho extends React.Component{

		render(){
			return(<h1>teste filho {this.props.teste}</h1>)
		}
	}


	class Pai extends React.Component{

		render(){
			const a = 10;
			return(
				<div>
					<h1>teste pai</h1>)
					<Filho teste={a}/>
				</div>
		}
	}