<h1 align="center">Projeto Triangle com Pytest</h1>

<p align="center">
  Um projeto Python para análise e manipulação de testes utilizando pytest.
</p>

<p align="center">
  <a href="[Link para o repositório GitHub do projeto]">
    <img src="https://img.shields.io/github/stars/[username]/[nome-do-repositorio]?style=social" alt="GitHub Stars">
  </a>
  <a href="[Link para a licença do projeto]">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
</p>

## Sobre o Projeto

Este projeto fornece uma classe `Triangle` para representar e analisar triângulos. Inclui métodos para calcular a área, perímetro, verificar a validade do triângulo, e determinar o tipo (equilátero, isósceles, escaleno). Os testes unitários são implementados utilizando `pytest` para garantir a correção e robustez da biblioteca.

### Principais Características

- **Classe `Triangle`:** Representação de triângulos com atributos para os lados.
- **Cálculo de Área:** Método para calcular a área do triângulo utilizando a fórmula de Heron.
- **Cálculo de Perímetro:** Método para calcular o perímetro do triângulo.
- **Validação de Triângulos:** Função para verificar se os lados fornecidos formam um triângulo válido.
- **Determinação de Tipo:** Método para determinar se o triângulo é equilátero, isósceles ou escaleno.
- **Testes Unitários:** Testes abrangentes utilizando `pytest` para garantir a qualidade do código.

### Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **pytest:** Framework para testes unitários.

## Como Começar

1.  Clone o repositório:
    ```bash
    git clone [Link para o repositório GitHub do projeto]
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd [nome-do-repositorio]
    ```

3.  Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate.bat # No Windows
    ```

4.  Instale as dependências:
    ```bash
    pip install pytest
    ```

5.  Execute os testes:
    ```bash
    pytest
    ```
