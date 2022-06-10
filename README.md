# Sessões

### Usando sessões Django

Quando os usuários fizerem login no site, sua sessão anônima será perdida e uma nova sessão
será criada para usuários autenticados. Se você armazenar itens em uma sessão anônima
e esses itens tiverem de ser preservados depois que o usuário fizer login, será necessário
copiar os dados da antiga para a nova sessão. Isso pode ser feito acessando os dados da
sessão antes de fazer o login do usuário com a função login() do sistema de autenticação
de Django e armazenando-os na sessão depois disso.

### Configuração de sessão

Há vários parâmetros que podem ser usados para configurar sessões em seu projeto. O mais
importante é SESSION_ENGINE. Esse parâmetro permite definir o local em que as sessões
serão armazenadas. Por padrão, Django armazena as sessões no banco de dados usando
o modelo Session da aplicação django.contrib.sessions.

Para que haja um melhor desempenho, utilize uma engine de sessão baseada em cache.
Django aceita prontamente o Memcached; além disso, é possível encontrar backends de cache
de terceiros para o Redis e para outros sistemas de cache.