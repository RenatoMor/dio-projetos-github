<p align="center"> 
  <img src="https://raw.githubusercontent.com/RenatoMor/repo_img/main/img/220.png" alt="HAR Logo" width="980px" height="120px">
</p>

<h1 align="center">Formação GitHub Certification</h1>

<h2 align="center">Projeto: Utilizando as Ferramentas do Github para Solucionar Algoritmos em Python</h2>

<p align="center"> 
  <img src="https://raw.githubusercontent.com/RenatoMor/repo_img/main/img/Signal.gif" alt="Sample signal" width="70%" height="70%">
</p>

<h5> I ❤️ Back-End Development!</h5>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h3 >Encontre-me :handshake: </h3>

<p align="center">
    <a href="https://www.linkedin.com/in/renatomoreira-rm/" target="_blank">
        <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=plastic&logo=linkedin&logoColor=white">
    </a>
    <a href="https://github.com/RenatoMor" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=plastic&logo=github&logoColor=white">
    </a>
    <a href="https://discord.com/channels/@me/1123380010779152444/" target="_blank">
        <img alt="Discord" src="https://img.shields.io/badge/Discord-5865F2?style=plastic&logo=discord&logoColor=white">
    </a>
</a>
    <a href="https://kovihq.slack.com/" target="_blank">
        <img alt="Slack" src="https://img.shields.io/badge/Slack-4A154B?style=plastic&logo=slack&logoColor=white">
    </a>
    <a href="https://www.instagram.com/renatomorspider/" target="_blank">
        <img alt="Instagram" src="https://img.shields.io/badge/Instagram-E4405F?style=plastic&logo=instagram&logoColor=white">
    </a>
    <a href="mailto:piano.tato@gmail.com" target="_blank">
        <img alt="Gmail" src="https://img.shields.io/badge/Gmail-EA4335?style=plastic&logo=gmail&logoColor=white">
    </a>
</p>
</p>
<br>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Menu

- [Descrição](#descrição)
- [Projetos](#projetos)
- [P1 - Concatenar Strings](#p1---concatenar-strings)
- [P2 - Operações Matemáticas Simples](#p2---operações-matemáticas-simples)
- [P3 - Repetindo Textos](#p3---repetindo-textos)
- [P4 - Catetos e Hipotenusa](#p4---catetos-e-hipotenusa)
- [P5 - Conversor de Medidas](#p5---conversor-de-medidas)
- [Utilização do GitHub Copilot](#utilização-do-github-copilot)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)
- [Agradecimentos](#agradecimentos-tada)


## Descrição

Este repositório contém projetos desenvolvidos durante a formação em GitHub da DIO (Digital Innovation One).

Neste repositório, você encontrará uma coleção de projetos práticos que foram desenvolvidos durante a formação em GitHub. Cada projeto está em sua própria pasta e contém um README separado com instruções detalhadas sobre como executar e utilizar o projeto.

## Projetos

- [Projeto 1](p1%20-%20info_concat.py): Concatenação de Strings
- [Projeto 2](p2%20-%20op_matemat_simples.py): Operações Matemáticas Simples
- [Projeto 3](p3%20-%20repetindo_textos.py): Repetindo Textos
- [Projeto 4](p4%20-%20catetos_e_hipotenusa.py): Catetos e Hipotenusa
- [Projeto 3](p5%20-%20conversor_de_medidas.py): Conversor de Medidas

## P1 - Concatenar Strings

Neste projeto, o objetivo é realizar a concatenação de duas strings informadas pelo usuário.

### GitHub Copilot

Utilizei o Git Copilot para gerar o código de exemplo abaixo, que utiliza a biblioteca `colored` para adicionar cores ao texto.

### Exemplo de uso

```python
print("A concatenação dos valores informados:", colored(
    info_concatenadas, 'yellow', attrs=['bold', 'underline']))
```

## P2 - Operações Matemáticas Simples

Neste projeto, o objetivo é realizar operações matemáticas simples com dois números informados pelo usuário.

Utilizei o Git Copilot para trazer uma abordagem com importação da biblioteca `operator` para realizar as operações matemáticas, resultando em um código mais limpo e organizado.

### Biblioteca `operator`

```python
import operator
```

```python
operacoes = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
```

## P3 - Repetindo Textos

Neste projeto, o objetivo é repetir um texto informado pelo usuário um número de vezes também informado pelo usuário.

**Repetindo textos v1:** Nesta abordagem sem a utilização do `GitHub Copilot`, o texto é repetido sem implementar nenhuma formatação adicional na saída

```python	
Output:

print(resultado)
```

### GitHub Copilot

**Repetindo textos v2:** Nesta abordagem com a utilização do `GitHub Copilot`, o texto é repetido com um caractere separador entre cada repetição e a saída é formatada em uma tabela.

```python	
Output:

print(f"{'\n\rTexto':<10} {'Repetições':<15} {'Resultado':<10}")
print(f"{texto:<10} {repetir:<15} {resultado:<10}")
```

## P4 - Catetos e Hipotenusa

Neste projeto, o objetivo é calcular a hipotenusa de um triângulo retângulo com base nos catetos informados pelo usuário.

O programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcula e mostra o comprimento da hipotenusa.

### GitHub Copilot

O Git Copilot foi utilizado para sugerir uma fórmula matemática com o uso de biblioteca `math` para calcular a hipotenusa de um triângulo retângulo.

```python
from math import hypot
```

## P5 - Conversor de Medidas

Neste projeto, o objetivo é converter uma medida informada pelo usuário de metros para centímetros e milímetros.

O programa que lê uma medida em metros e mostra o valor convertido em centímetros e milímetros.

### GitHub Copilot

O Git Copilot foi utilizado para sugerir a fórmula matemática para realizar a conversão de metros para centímetros e milímetros.

```python
Versão 1: com a utilização do GitHub Copilot

import math

m = float(input("Uma distância em metros: "))
cm = math.floor(m * 100)
mm = math.floor(m * 1000)

print("{}m corresponde a {}cm e {}mm".format(m, cm, mm))
```

```python
Versão 2: sem a utilização do GitHub Copilot
m = float(input("Uma distância em metros: "))
cm = m * 100
mm = m * 1000

print("{}m corresponde a {}cm e {}mm".format(m, cm, mm))
```

## Utilização do GitHub Copilot

O Git Copilot é uma ferramenta de assistência de programação baseada em inteligência artificial que pode ajudar a gerar código automaticamente. Ele pode sugerir trechos de código, completar linhas de código e fornecer exemplos de implementação.

    Para utilizar o GitHub Copilot, siga as etapas abaixo:

1. Certifique-se de ter o Git Copilot instalado em seu ambiente de desenvolvimento.
2. Abra o arquivo em que deseja utilizar o Git Copilot.
3. Digite o código que você deseja completar ou gerar.
4. O Git Copilot irá analisar o contexto e fornecer sugestões de código.
5. Selecione a sugestão desejada e o Git Copilot irá inserir o código no seu arquivo.

Lembre-se de revisar e ajustar o código gerado pelo Git Copilot para atender às suas necessidades específicas.

## Como Contribuir

Se você deseja contribuir para este repositório, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch com o nome da sua feature: `git checkout -b minha-feature`.
3. Faça as alterações desejadas e adicione os arquivos modificados: `git add .`.
4. Faça o commit das suas alterações: `git commit -m 'Adicionando minha feature'`.
5. Faça o push para a branch criada: `git push origin minha-feature`.
6. Abra um pull request neste repositório.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Agradecimentos :tada:

**Digital Innovation One:** Agradeço à Digital Innovation One por proporcionar recursos educacionais valiosos que contribuíram para o desenvolvimento dos meus projetos.

<a href="https://digitalinnovation.one/" target="_blank">
  <img src="https://digitalinnovationone.github.io/roadmaps/assets/logo-dio.svg" width="100" alt="Digital Innovation One">
</a>


**Python:**
Agradeço profundamente à comunidade Python e à equipe de desenvolvimento por criar uma linguagem poderosa, versátil e amigável. O Python tem sido uma ferramenta incrível que tornou possível transformar minhas ideias em realidade de maneira eficiente e elegante.

<a href="https://www.python.org/" target="_blank">
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="100" alt="Python">
</a>


**VS Code:** Agradeço à equipe do Visual Studio Code pelo incrível editor que facilita o desenvolvimento deste projeto.

[<img src="https://code.visualstudio.com/assets/favicon.ico" width="30">](https://code.visualstudio.com/)


**GitHub:** Agradeço à equipe do GitHub por fornecer uma plataforma de desenvolvimento colaborativo que facilita o compartilhamento de projetos.

**GitHub:** Agradeço à equipe do GitHub por fornecer uma plataforma de desenvolvimento colaborativo que facilita o compartilhamento de projetos.

[![GitHub](https://github.githubassets.com/favicons/favicon.png)](https://github.com/RenatoMor)

Copyright © 2024 / RenatoMor