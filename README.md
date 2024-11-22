# Grafos
código desenvolvido na aatéria Teoria de grafos


Relatório do Projeto 
Parte 2

Nome do Integrante	RA
Francesco Z Coppola	10403340
	
	

Relatório


Importante: A aplicação se utiliza de algumas bibliotecas para manipulação de vídeo e de interface gráfica então e necessário rodar os seguintes comandos em seu terminal: 
pip install pillow 
pip install tk 
pip install opencv-python
 pip install matplotlib

O código deve ser executado pelo arquivo Menu















1)Definição Do Problema:


Estou desenvolvendo uma aplicação como parte do nosso TCC que utiliza tecnologia de detecção de objetos baseada em inteligência artificial para analisar vídeos enviados pelos usuários. A ferramenta será capaz de identificar objetos relevantes, isolar clipes de vídeo que apresentam esses objetos e descartar clipes estáticos.

Essa atividade tem como foco em otimizar o acesso a esses clipes processados de maneira eficiente. Para isso, foi aplicado conhecimentos adquiridos na disciplina de grafos, criando um grafo que representa as relações entre os objetos relevantes em cada clipe. Essa abordagem nos permitirá navegar e consultar os dados de forma mais ágil e estruturada. 


Para a modelagem do problema, utilizei  um grafo do tipo 1, pois as relações entre os clipes são bilaterais. No entanto, quando tivermos acesso a filmagens reais, poderemos adicionar pesos às arestas com base na diferença de tempo entre os clipes, o que aprimorará ainda mais a experiência  de busca. Essa funcionalidade já foi implementada, mas no momento os clipes disponíveis são apenas exemplos e não apresentam uma linearidade temporal entre si.











1.2)Representação no Graph online



Grafo Real :
![image](https://github.com/user-attachments/assets/392bc6e4-2b46-4b8f-a03f-3349dad8be62)


 

















Devido ao elevado número de arestas no grafo, decidi criar uma versão simplificada com 9 vértices, cada um representando um clipe. Os rótulos das arestas indicam os objetos presentes em cada clipe, e utilizamos diferentes cores para cada tipo de relação, facilitando assim a visualização e compreensão das conexões entre os clipes.


Grafo Simplificado :
![image](https://github.com/user-attachments/assets/111bfb31-8ede-46c3-88e1-705eba63670b)


    





































1.3) Código Desenvolvido: 
Nesta segunda fase do projeto, houve um grande esforço para aprimorar a qualidade do código, aplicando conceitos fundamentais aprendidos ao longo do curso, como: classes, modularidade, microsserviços, herança e os princípios SOLID. O objetivo foi criar uma base sólida para o desenvolvimento do futuro trabalho de conclusão de curso (TCC).

O código monolítico e orientado a gambiarra do primeiro projeto foi completamente reestruturado, dando lugar a um sistema modular baseado em classes. A utilização de herança permitiu a construção de uma solução mais eficiente, flexível e preparada para se adaptar a novos requisitos de maneira escalável e de fácil manutenção. Além disso, a aplicação do princípio de responsabilidade única do SOLID aprimorou significativamente o processo de depuração, tornando a identificação e correção de bugs mais eficaz e assertiva.


Arquivo GRAFO:
Este módulo fornece a base para todas as subclasses relacionadas a grafos. Ele foi projetado seguindo o princípio de cascata, onde funções de alto nível delegam tarefas a funções de baixo nível, sem interferir diretamente em suas implementações, enquanto funções de baixo nível não chamam ou dependem de funções de nível superior.
Estrutura do Arquivo:
Contém 3 classes principais:

Grafo: 
•  Classe central de controle, atuando como interface principal para acesso às informações das classes de menor nível (Vértice e Aresta).
•	Somente esta classe é exposta para interação com programas externos.
•	Realiza chamadas às funções de classes subordinadas sem se preocupar com os detalhes de implementação.
•	Armazena informações gerais do grafo, como:
	Nome;
	Número de arestas;
	Número de vértices;
	Lista de vértices;
	Indicação se o grafo é direcionado ou não.


Vértice : 
•	Classe responsável por gerenciar informações e operações relacionadas aos vértices.
•	Armazena dados como:
	Nome do vértice;
	Listas de adjacências .
•	Pode chamar funções de nível inferior da classe Aresta

Aresta:
•	Classe responsável exclusivamente por informações e operações envolvendo arestas.
•	Armazena dados como:
	Peso;
	Vértice inicial;
	Vértice final;
	Indicação se a aresta é direcionada.












Arquivo TGRAFO:
Este módulo é uma especialização do módulo GRAFO, projetado para permitir o uso de tags nos elementos do grafo. Ele foi utilizado para realização do projeto.
Contém 3 classes:

TGrafo: 
•	Classe criança de Grafo com as mesmas funções porem considerando o tratamento de  tags. 

TaggedVertice: 
•	Classe criança de vértice com as mesmas funções porem considerando o tratamento de  tags. 
•	Armazena o caminho dos clips e suas tags.

TaggedAresta:
•	Classe criança de Aresta com as mesmas funções porem considerando o tratamento de  tags. 


Arquivos de Funções(Coloracao , Euliriano, Hamiltoniato e etc...)

Diferentemente do primeiro projeto, no qual as funções eram frequentemente duplicadas ou reescritas para diferentes tipos de grafos, nesta nova abordagem, cada funcionalidade foi encapsulada em arquivos separados. Isso eliminou a necessidade de portar ou reimplementar as mesmas funções para cada tipo de grafo, promovendo uma solução única e reutilizável que atende a múltiplos cenários.

Essa desacoplação do código trouxe melhorias significativas em modularidade e organização. Cada arquivo de função agora possui responsabilidades bem definidas, permitindo que novas funcionalidades sejam implementadas e integradas de maneira mais eficiente, sem causar impacto no restante do sistema.
  Arquivo menu: 
	Arquivo responsável pela interação gráfica com o usuário e arquivo por onde o projeto deve ser executado.  



2) Modelagem do problema no arquivo grafo.txt; 
Neste projeto, a modelagem do problema é baseada nas relações entre os clipes de vídeo. Dessa forma, o problema foi modelado usando uma pasta de vídeos(Clips segurança). Entretanto podemos obter sua modelagem em um arquivo txt utilizando a função gravar após carregar os vídeos, isso resultara em um arquivo GRAFO.txt que contêm a modelagem(esse já estará incluso no envio para teste)
 




3) O desenvolvimento de uma aplicação contendo um menu de opções:
 Como este trabalho se trata de um pré-TCC voltado para uma aplicação destinada a usuários não programadores, optamos por utilizar a biblioteca de interface gráfica Tkinter para construir o menu. Isso nos permitiu desenvolver um menu gráfico interativo, facilitando a interação do usuário com a aplicação de forma intuitiva e acessível. Menu gerado pela Aplicação:






4) objetivos da ODS:
 ![image](https://github.com/user-attachments/assets/3112f69c-4d1a-44a0-a3b3-9f2487a331a3)

O projeto se alinha principalmente com o Objetivo  9 - Indústria, Inovação e Infraestrutura, por promover o uso de tecnologias avançadas de Inteligência Artificial para aprimorar sistemas de segurança e infraestrutura digital de forma inovadora


5) Investigar uma solução para o problema baseado no conteúdo da disciplina:
Um dos grandes desafios identificados em nosso grafo é a navegação eficiente entre clipes, baseada nas conexões estabelecidas pelas arestas. Para resolver esse problema, recorremos a um conceito fundamental aprendido neste semestre: o Caminho Hamiltoniano.

A teoria dos Caminhos Hamiltoniano nos permite determinar se existe uma rota no grafo que percorra todas os vértices uma vez, sem repetições. Essa abordagem é particularmente relevante para nosso projeto, pois, ao identificar a existência de um Caminho Hamiltoniano , podemos definir um trajeto ótimo para navegar por todos os clipes conectados, evitando redundâncias.

Com base nisso, aplicamos a teoria ao nosso grafo e realmente existe caminhos Hamiltonianos em nosso grafo!

Resultado: 

Caminho Hamiltoniano encontrado:
clip1 -> clip2 -> clip3 -> clip4 -> clip6 -> clip5 -> clip7 -> clip9 -> clip8 -> clip10 -> clip12 -> clip13 -> clip14 -> clip15 -> clip16 -> clip18 -> clip11 -> clip17 -> clip20 -> clip19 -> clip21 -> clip22 -> clip23 -> clip24 -> clip27 -> clip25 -> clip26 -> clip28 -> clip29 -> clip31 -> clip34 -> clip30 -> clip32 -> clip33 -> clip35 -> clip36 -> clip37 -> clip39 -> clip40 -> clip41 -> clip42 -> clip38 -> clip43 -> clip45 -> clip48 -> clip44 -> clip46 -> clip49 -> clip50 -> clip47
5) Utilizar técnicas estudadas na disciplina ou não com a finalidade de descobrir pelo menos três características interessantes do problema modelado.



Coloração: 


![image](https://github.com/user-attachments/assets/30e5261f-d9c8-4b2d-8749-2c93899e38a8)


  

Nosso grafo pode ser representado em 32 cores 





Caminho euleriano: 

![image](https://github.com/user-attachments/assets/a52ddabc-19d8-4582-83d5-33e0c8cff46a)

 
 
O grafo não tem nenhum caminho que passe pelas 1674 arestas sem repetir nenhuma 







Emparelhamento:

 ![image](https://github.com/user-attachments/assets/c36421f8-ba2e-4ffc-a778-dab5bd1e73c6)



Existe um emparelhamento perfeito no Grafo!! 
