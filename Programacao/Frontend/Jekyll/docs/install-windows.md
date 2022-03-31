## Procedimento padrão para Instalação do Jekyll no Windows.


1. download instalador ruby + devkit.

		https://rubyinstaller.org/downloads/

2. após finalizar a instalação e o 'ridk install' também, vamos abrir outro prompt de comandos e instalar a gem do Jekyll :

		gem install jekyll bundler

3. Em seguida verifique se Jekyll foi instalado corretamente : 

		jekyll -v



- Agora já podemos subir o template padrão em um webserver que o jekyll cria, para começarmos a trabalhar. Para isso fazer o seguinte:



		gem install jekyll bundler

		bundle add webrick ( Caso a versão do Ruby seja 3.0+ )

		jekyll new myblog

		cd myblog

		bundle exec jekyll serve




PS : Para atualização em tempo real nas alterações feitas no código do site, devemos passar a opção '--livereload' quando formos subir o server, EX:


		bundle exec jekyll serve --livereload