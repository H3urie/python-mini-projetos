# Validador de CPF (Python)

Projeto desenvolvido em Python com o objetivo de validar os dois últimos dígitos de um CPF, seguindo as regras oficiais do cálculo de validação.

O programa realiza o cálculo dos dígitos verificadores a partir dos 9 primeiros números do CPF e compara o resultado com o CPF informado, indicando se ele é válido ou inválido.

# Conceitos aplicados

- Manipulação de strings

- Listas e laços de repetição

- Conversão de tipos (int, str)

- Operações matemáticas

- Lógica de validação

- Algoritmo de cálculo de CPF

# Como funciona

- O CPF base (9 primeiros dígitos) é separado

- Cada dígito é multiplicado por um peso regressivo

- Os valores são somados e usados para calcular o resto

- O processo é repetido para o segundo dígito verificador

- O CPF calculado é comparado com o CPF original

# Objetivo do projeto

- Praticar lógica de programação em Python e implementar um algoritmo real utilizado em validações no dia a dia.
