# Exercícios em Python

## Sobre o projeto

Esse projeto foi feito para praticar programação em Python durante a disciplina. A ideia foi começar com exercícios básicos e depois fazer alguns programas que mostram informações do próprio computador, como uso de memória, CPU, disco e rede.



## O que foi utilizado

* Visual Studio Code
* Python
* Biblioteca psutil



## Como rodar os códigos

Primeiro é necessário ter o Python instalado. Depois disso, no terminal do VS Code, foi usado o seguinte comando para instalar a biblioteca:

```
python -m pip install psutil
```

Depois disso, é só abrir os arquivos `.py` e executar normalmente.

---

## Organização das pastas

Os arquivos foram separados em duas pastas:

```
python/
  ├── basico/
  ├── sistema/
```

* **basico**: exercícios mais simples para treinar lógica
* **sistema**: programas que pegam informações do computador

---

## Parte 1 – Exercícios básicos

Na pasta `basico` tem exercícios mais simples, como:

* leitura de dados com input
* uso de print
* if e else
* laços de repetição
* listas

Alguns exemplos:

* pedir nome e mostrar uma mensagem
* soma de números
* cálculo de média
* verificar se número é par ou ímpar
* tabuada
* contador de vogais
* jogo de adivinhação
* calculadora simples
* sistema de tarefas com arquivo .txt

---

## Parte 2 – Monitoramento do sistema

Na pasta `sistema` foram feitos programas usando a biblioteca psutil.

Com isso foi possível pegar informações como:

* uso de memória RAM
* uso da CPU
* espaço em disco
* tráfego de rede

---

## Painel

Também foi feito um programa que junta várias informações em uma tela só, funcionando como um painel simples no terminal.

Ele mostra:

* uso de RAM
* uso de CPU
* espaço do disco
* velocidade da internet

E atualiza automaticamente.

---

## Conclusão

Com esses exercícios deu pra entender melhor como funciona a lógica de programação em Python e também como usar bibliotecas para acessar informações do sistema.

Também ajudou a organizar melhor os arquivos em pastas, o que facilita na hora de trabalhar com projetos maiores.
