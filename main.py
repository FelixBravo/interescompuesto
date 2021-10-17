import argparse
import logging
from math import log10

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def _findForVariable(var_to_find):
    logging.info('Beginning, I will help you to find variable {}'.format(var_to_find))
    if (var_to_find == 'Valor Futuro'):
        VP = float(input('Please enter Valor Presente: '))
        I = float(input('Please enter Tasa Interes Compuesta en %: '))
        N = float(input('Please enter Periodo: '))
        VF = (VP * (1 + I/100)**N)
        print('Valor Futuro = ', VF)
    
    if (var_to_find == 'Valor Presente'):
        VF = float(input('Please enter Valor Futuro: '))
        I = float(input('Please enter Tasa Interes Compuesta en %: '))
        N = float(input('Please enter Periodo: '))
        VP = (VF / (1 + I/100)**N)
        print('Valor Presente = ', VP)

    if (var_to_find == 'Tasa de Interes'):
        VP = float(input('Please enter Valor Presente: '))
        VF = float(input('Please enter Valor Futuro: '))
        N = float(input('Please enter Periodo: '))
        I = ((VF / VP)**(1/N))-1
        print('Tasa de Interes en % = ', I*100)

    if (var_to_find == 'Periodo'):
        VP = float(input('Please enter Valor Presente: '))
        VF = float(input('Please enter Valor Futuro: '))
        I = float(input('Please enter Tasa Interes Compuesta en %: '))
        N = ( ( log10(VF) - log10(VP) ) / (log10(1 + (I/100))) )
        print('El Periodo es = ', N)   
        



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculadora Valor Futuro, Presente, Interes Compuesto y Periodo de una Inversion!!')

    variable_to_find = ['Valor Futuro', 'Valor Presente', 'Tasa de Interes', 'Periodo']

    parser.add_argument('newVar', 
                        help='The Variable that you want to find',
                        type=str,
                        choices=['Valor Futuro', 'Valor Presente', 'Tasa de Interes', 'Periodo'])

    args = parser.parse_args()
    _findForVariable(args.newVar)