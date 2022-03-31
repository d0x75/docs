React possui alguns tipos diferentes de componentes. subclasses React.Component:



- Exemplo :

class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Lista de compras para {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}


Aqui ShoppingList, é um componente React do tipo classe. Um componente recebe parâmetros, chamados props (abreviação de
propriedades), e retorna uma hierarquia de elementos para exibir através do método render.


O componente ShoppingList acima apenas renderiza componentes internos do DOM como <div /> e <li />. Mas você também pode compor e renderizar componentes React personalizados. Por exemplo, agora podemos nos referir a toda a lista de compras escrevendo 
<ShoppingList />. Cada componente React é encapsulado e pode operar de forma independente; Isso permite que você construa interfaces complexas a partir de componentes simples.