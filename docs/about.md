## graphene-java-standalone-stack
Crie aplicações ou modulos Java de forma rápida e padronizada, escolha entre as versões (11 e 17), (Gradle, Maven ou Java puro), experimentos, validações de conceitos, testes e algoritmos.

#### Veja abaixo os cenários de exemplos em que a utilização da stack é aplicável:
- Poc
- Experimentos Java
- Testes
- Algoritmos
- Modulo de domain de arquitetura limpa;
- Modulo de infraestrutura;
- Modulo de DTO.

#### Para utilizar o template standalone é necessário realizar os seguintes passos:
- ##### 1 Importar a stack
 ```
    stk import stack https://github.com/stack-spot/graphene-java-standalone-stack
 ```

- ##### 2 Executar o comando
 ```
    stk create app <nome da aplicação> --template graphene-java-standalone-stack/starter-java
 ```

#### Após a execução da sequência de comandos acima, o stackspot deve apresentar as seguintes opções para geração do projeto:
- Versão do projeto
- Nome do pacote: Ex (br.com.orgname)
- Versão do Java: (11 ou 17)
- Ferramenta de compilação: (Maven, Gradle ou Java puro)

### Requerimentos:
- É necessário ter o java instalado no ambiente local de acordo com a versão selecionada.
- Caso não esteja com o Gradle ou Maven previamente instalado, basta executar o wrapper de acordo o selecionado, sendo eles:
    - ./gradlew build (Linux/ mac)
    - gradlew build (windows)
    - ./mavenw install (Linux/ mac)
    - mavenw install (windows)