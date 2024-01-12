from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.pratos import Pratos

restaurante_praca = Restaurante('praca', 'gourmet')
bebida_suco = Bebidas('Suco de Melancia', 5.0,'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Pratos('Paozinho',2.00,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
