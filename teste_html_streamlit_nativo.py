import streamlit as st

# Dados da tabela em formato que possa ser diretamente convertido em Markdown
dados_tabela = [
    "Linha | numeros | chave | valor | resultado | valor % 2 | Ação",
    "--- | --- | --- | --- | --- | --- | ---",
    "1 | {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} | - | - | - | - | Inicializa `numeros`",
    "2 | {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} | - | - | {} | - | Inicializa `resultado` como dicionário vazio",
    "3-7 | {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} | a | 1 | {'a': 'ímpar'} | 1 | Loop começa, `valor=1` é ímpar",
    "3-7 | {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} | b | 2 | {'a': 'ímpar', 'b': 'par'} | 0 | `valor=2` é par, adiciona 'par' ao resultado",
    # Adicione as linhas restantes conforme necessário...
    "8 | {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} | - | - | {'a': 'ímpar', 'b': 'par', 'c': 'ímpar', 'd': 'par', 'e': 'ímpar'} | - | Imprime o dicionário `resultado`"
]


st.markdown ('''
```python
1. numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
2. resultado = {}
3. for chave, valor in numeros.items():
4.    if valor % 2 == 0:
5.        resultado[chave] = 'par'
6.    else:
7.        resultado[chave] = 'ímpar'
8. print(resultado)
```

''',  unsafe_allow_html = True
)

# Inicializando o índice da linha atual
if 'indice_atual' not in st.session_state:
    st.session_state.indice_atual = 0

# Função para adicionar a próxima linha e mostrar a tabela acumulada
def adicionar_e_mostrar_linhas():
    # Verificar se ainda há linhas a serem adicionadas
    if st.session_state.indice_atual < len(dados_tabela):
        # Exibir as linhas acumuladas até o momento
        tabela_markdown = "\n".join(dados_tabela[:st.session_state.indice_atual + 1])
        st.markdown(tabela_markdown, unsafe_allow_html = True)
        st.session_state.indice_atual += 1
    else:
        st.markdown("Todas as linhas foram exibidas.")

# Botão para mostrar a próxima linha e atualizar a exibição
st.button("Mostrar próxima linha", on_click=adicionar_e_mostrar_linhas)







