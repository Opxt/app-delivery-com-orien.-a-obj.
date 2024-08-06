from modelos.restaurante import Restaurante

restaurante_larissa = Restaurante('Restaurante Larissa', 'Caseira')
restaurante_dio = Restaurante('Mama Dio', 'Hamburgueria')
restaurante_sushi = Restaurante('Tanka', 'Japonesa')
restaurante_larissa.receber_avaliacao('Dio', 4)
restaurante_larissa.receber_avaliacao('Lari', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()