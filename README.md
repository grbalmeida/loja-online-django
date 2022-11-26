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

# Celery

### Disparando tarefas assíncronas com o Celery

Tudo que você pode executar em uma view afetará os tempos de resposta. Em muitas situações, talvez
você queira devolver uma resposta ao usuário o mais rápido possível e deixar que o servidor execute
algum processo de forma assíncrona. Isso será particularmente relevante para processos que consumam
tempo ou que estejam sujeitos a falhas e possam precisar de uma política de novas tentativas.

O Celery é uma fila de tarefas distribuída, capaz de processar grandes quantidades de mensagens.
Ao usar o Celery, podemos não só criar tarefas assíncronas facilmente e deixar que sejam executadas
por workers assim que for possível, como também podemos agendá-las para que sejam executadas em
horários específicos.

**IMPORTANTE:**

O parâmetro CELERY_ALWAYS_EAGER permite executar tarefas localmente, de modo síncrono, em vez de
enviá-las para a fila. Isso será conveniente para executar testes de unidade, ou para executar
a aplicação em nosso ambiente local sem executar o Celery.

### Adicionando tarefas assíncronas em nossa aplicação

**IMPORTANTE:**

Utilize tarefas assíncronas não só para processos que consomem tempo, mas também para outros processos
que não demorem tanto para serem executados, porém estão sujeitos a falhas de conexão ou exigem
uma política de novas tentativas.

### Comando para instalar RabbitMQ com Docker

```
docker run -d --hostname rabbit-host --name loja-online-django -p 15672:15672 -p 5672:5672 rabbitmq:management
```

### Comando para iniciar celery

```
celery -A myshop worker -l info
```

**IMPORTANTE:**

Executar comando dentro do diretório myshop

### Monitorando o Celery

Você pode monitorar as tarefas assíncronas que são executadas. O Flower é uma ferramenta
web para monitorar o Celery. É possível instalá-lo com este comando:

```
pip install flower==0.9.3
```

Assim que estiver instalado, você poderá iniciar o Flower executando o comando a seguir
no diretório de seu projeto:

```
celery -A myshop flower
```

Acesse [http://localhost:5555/dashboard](http://localhost:5555/dashboard) em seu navegador. Você verá os workers ativos
do Celery e as estatísticas sobre as tarefas assíncronas.

**IMPORTANTE:**

Se houver algum erro usando o sistema operacional Windows, verificar o link abaixo:
[https://stackoverflow.com/questions/62975722/error-executing-flower-with-celery-in-windows-10](https://stackoverflow.com/questions/62975722/error-executing-flower-with-celery-in-windows-10)


**IMPORTANTE:**

Rodar worker e flower em abas separadas do terminal. Verificar o link abaixo:
[https://stackoverflow.com/questions/34247062/celery-works-but-with-flower-doesnt-work](https://stackoverflow.com/questions/34247062/celery-works-but-with-flower-doesnt-work)

```
celery -A myshop worker -l info
```

```
celery -A myshop flower -l info
```

# Braintree

### Integrando o Braintree com Hosted Fields

A integração Hosted Fields permite criar nosso próprio formulário de pagamento
usando estilos e layouts personalizados. Um iframe será adicionado dinamicamente
na página por meio do uso do **SDK** (Software Development Kit, ou Kit de Desenvolvimento de Software)
Javascript do Braintree. O iframe inclui o formulário de pagamento Hosted Fields. Quando o cliente
submeter o formulário, o Hosted Fields obterá os detalhes do cartão de forma segura
e tentará gerar um token. Se esse processo for bem-sucedido, você poderá enviar o
token nonce gerado para a sua view a fim de criar uma transação utilizando o módulo
Python braintree.

Um token nonce é uma referência segura, utilizada uma única vez, para informações
de pagamento. Ele permite enviar informações confidenciais de pagamento ao
Braintree sem usar os dados brutos.