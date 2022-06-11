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

# Processadores de contexto

Um processador de contexto é uma função Python que recebe o objeto request como argumento
e devolve um dicionário que será adicionado no contexto da requisição. Os processadores
de contexto são convenientes quando queremos disponibilizar algo de modo global a todos os templates.

- django.template.context_processors.debug: define a variável booleana debug e a variável sql_queries.
- django.template.context_processors.request: define a variável request no contexto.
- django.contrib.auth.context_processors.auth: define a variável user na requisição.
- django.contrib.messages.context_processors.messages: define a variável messages no contexto.

**IMPORTANTE:**

Os processadores de contexto são executados em todas as requisições que utilizem RequestContext.
Você poderia criar uma tag de template personalizada em vez de um processador de contexto caso a
sua funcionalidade não fosse necessária em todos os templates, sobretudo se ela envolvesse consultas no banco de dados.