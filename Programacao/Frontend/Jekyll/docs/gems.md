## Notas sobre gems no Jekyll


- Gems : São códigos que podem ser incluídos em projetos escritos em Ruby. Gems podem ser compartilhadas em outros projetos ou
com outras pessoas.

- Gemfile : É uma lista de gems usadas pelo site. Essa lista fica em um arquivo GemFile na pasta principal do site. Para o um site simples , este arquivo Gemfile pode ser como o seguinte exemplo :

			source "https://rubygems.org"

			gem "jekyll"

			group :jekyll_plugins do
			  gem "jekyll-feed"
			  gem "jekyll-seo-tag"
			end
