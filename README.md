# OrdenacaoPython
Uma implementação de algoritmos de ordenação em Python como trabalho de Análise de Algoritmos do curso de SI - UFPA (ERE 2020.4)

Todos foram construidos com Python3 utilizando a IDE VSCode
Nesse projeto foram implementados os seguintes algoritmos: `Quicksort`, `Heapsort`, `Radixsort`, `Countingsort` e `Bucketsort`

### `criarvetor.py`
É um código reutilizado pelos algoritmos para criação dos vetores de 3 tamanhos diferentes (1.000, 5.000, 10.000), além do armazenamento do criado num arquivo de texto (.txt). Quando o vetor já possui elementos e deseja utilizá-lo novamente, o algoritmo dá a opção para reutilização.
Nele são utilizadas as bibliotecas:
- `os`: para verificação da existência do arquivo e se não está vazio
- `random`: para geração de números aleatórios que alimentam o vetor

Foram utilizados em algumas execuções elementos variando de 1 a 100 e em outras de 1 a 1000

##### `criarvetor_gna.py`
É utilizado uma variação do código para obedecer a questão de geração de sequências uniformemente distribuídas.
Além das bibliotecas anteriores é utilizado neste código a `datetime` e `random.seed()` para gerar os elementos dado o horário atual de execução (linhas 19 - 31)

##### `vetor.txt`
Ele recebe os elementos que foram criados a partir do algortimo `criarvetor.py`.

###### `zipcodes.py` e `zipcodes.txt`
Contém um algoritmo que recebe todos os CEPs ordenados do arquivo `zipcodes.txt` e cria um `vetor.txt` com elementos randomicamente de tamanho informado para utilização na questão de radixsort.

### Bucketsort
O algoritmo recebe um vetor inicial deseordenado e implementa um `Insertionsort` para ordenação. Dependendo da escolha ele chama `criarvetor_gna.py` ou `criarvetor.py` para decisão de usar o vetor no arquivo de texto ou criar um novo.
Primeiro é calculado o tamanho do vetor inicial e então instanciado lista de "baldes" vazias nas quais serão inseridos elementos baseados no seu valor e no tamanho de cada balde. O `insertionsort_b` então é chamado para ordenação da lista de baldes. E no fim é retornado um novo vetor com a saída.

### Countingsort
O algoritmo recebe um vetor desordenado e cria um vetor contador que recebe o contador da ocorrência de cada elemento e inicializa o vetor contador com 0. Em um loop cada elemento é analisado e é contado a ocorrencia de cada. Seguindo num próximo loop, o vetor de contadores deverá conter a posição do elemento no vetor. Seguindo no próximo loop, é construído o vetor de saída e então copiado o vetor de saída para o vetor original, que agora está ordenado e então é retornado.

### Heapsort
O algoritmo recebe um vetor inicial desordenado, ordenado (crescente) ou ordenado (descrescente) no momento da execução. Então o método `heapify` recebe o vetor, o tamanho do heap e a raiz da subárvore. É inicializado com essa raiz da subárvore e váriaves que estabelecem as operações para o lado esquerdo e direito da árvore. Então é verificado se o filho a esquerda da raiz existe e é maior do que a raiz, se for a variável `maior` recebe o índice do filho da esquerda. A mesma coisa é verificado com o filho da direita, se for a variável `maior` recebe o índice do filho da direita. A função `heapsort` recebe o vetor inicial para ordenamento, constrói um heap máximo e extrai elementos um por um e faz a troca entre eles caso necessário. O vetor inicial estará ordenado no fim.

### Quicksort (iterativo e recursivo)
O algoritmo recebe um vetor inicial desordenado, ordenado (crescente) ou ordenado (descrescente) no momento da execução. A função `particao` faz o particionamento e incrementado o índice do menor elemento, escolhendo o pivô e efetuando a troca. A função `quicksort` recebe o vetor inicial, o índice inicial e o índice final. Ele cria uma pilha auxiliar e a inicializa no topo. Então os elementos que estão nos índices inicial e final são postos no vetor auxiliar e continua a retirar elementos da pilha enquanto não está vazio, em um loop, retirando elementos nos índices inicial e final. Logo após isso o pivô é acertado na posição correta com a função `particao`, se existem os elementos no lado esquerdo do pivô então são colocados no lado esquerdo da pilha. Se acontecer o mesmo na direita, são colocados ao lado direito da pilha. No fim, é recebido o vetor ordenado.

### Radixsort
O algoritmo recebe um vetor inicial deseordenado e implementa um `Countingsort` para ordenação. O `countingsort_r` irá criar um vetor de saída que tem espaços do tamanho do vetor inicial e cria um vetor contador iniciado em 0 (aqui com 10 índices pois a questão que o pede trata de CEPs de 8 digitos), então é feita a contagem das ocorrências no vetor contador. Então o contador com um índice de um loop irá receber o índice real daquele digito para o vetor de saída e constrói o vetor de saída. O vetor de saída então é copiado para o vetor inicial contendos os digitos em si ordenados. A função `radixsort` encontrará o maior número para conhecimento do número de dígitos e fará a chamada do `countingsort_r`para cada dígito. No final se obtém o vetor ordenado.
