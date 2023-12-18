# Função para verificar se é seguro colocar uma rainha em uma determinada posição no tabuleiro
def verifica_pos(matriz, linha, coluna):
    # Verificar a linha à esquerda
    for i in range(coluna):
        if matriz[linha][i] == 1:
            return False

    # Verifica a diagonal superior à esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if matriz[i][j] == 1:
            return False

    # Verifica a diagonal inferior à esquerda
    for i, j in zip(range(linha, 8, 1), range(coluna, -1, -1)):
        if matriz[i][j] == 1:
            return False

    return True

# Função recursiva para resolver o problema das oito rainhas usando backtracking
def backTracking_rainhas(matriz, coluna, posicoes):
    # Se todas as rainhas estiverem colocadas, retorne verdadeiro
    if coluna >= 8:
        return True

    # Para cada linha, chama a func para verificar as posições e ver se é "safe" de colocar a rainha ali
    for i in range(8):
        if verifica_pos(matriz, i, coluna):
            # Se for seguro, coloque uma rainha naquela posição
            matriz[i][coluna] = 1
            posicoes.append((i, coluna))

            # Recursivamente tente colocar as rainhas nas colunas restantes
            if backTracking_rainhas(matriz, coluna + 1, posicoes) == True:
                return True

            # Se colocar a rainha na posição atual não levar a uma solução, remova a rainha daquela posição (backtracking)
            matriz[i][coluna] = 0
            posicoes.remove((i, coluna))

    # Se a rainha não puder ser colocada em nenhuma linha nesta coluna, retorne falso
    return False

# Função para resolver o problema de fato 
def solve():
    # Inicializar o tabuleiro e a lista de posições
    matriz = [[0 for _ in range(8)] for _ in range(8)]
    posicoes = []

    # Tentar resolver o problema das oito rainhas
    if backTracking_rainhas(matriz, 0, posicoes) == False:
        print("Não foi possível encontrar uma solução.")
        return False

    # Printa a solução encontrada em forma de matriz de 0 e 1
    print("\nSolução encontrada:")
    for i in range(8):
        for j in range(8):
            print(matriz[i][j], end = " ")
        print()

    # Imprimir as posições colocadas em forma de par de vértices (X, Y).
    print("\nPosições das rainhas:")
    for pos in posicoes:
        print(pos)

    return True

# função solve para resolver o problema
solve()