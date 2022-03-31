- método *render()*

render() = Em particular, render retorna um elemento React, que é uma descrição simplificada do que renderizar. A maioria dos desenvolvedores do React usa uma sintaxe especial chamada “JSX”, que facilita a escrita desses elementos. A sintaxe <div /> é transformada em tempo de compilação para React.createElement ('div'). O exemplo acima é equivalente a:


return React.createElement('div', {className: 'shopping-list'},
  React.createElement('h1', /* ... filhos de h1 ... */),
  React.createElement('ul', /* ... filhos de ul ... */)
);
