## Notas sobre Bundler no Jekyll


- Bundler : É uma gem que instala todas as gems no arquivo Gemfile. Embora não seja obrigatório utilizar-lo, é altamente recomendado, pois garante que você esteja usando o jekyll e seus plugins em ambientes diferentes.

Instalação do Bundler :
	
			gem install bundler
			
Você só precisa instalá-lo uma vez, não quando criar um projeto Jekyll.

Para instalar gems em seu Gemfile usando Bundler, execute o seguinte no diretório que contém o Gemfile: 

			bundle install
			bundle exec jekyll serve
