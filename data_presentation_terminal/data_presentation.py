from tabulate import tabulate

format = ['plain', 'simple', 'github', 'grid', 'fancy_grid',
          'pipe', 'jinja', 'ham', 'react', 'redux', 'nodejs', 'html',
          'css', 'pug', 'helmet', 'hanna', 'aloha', 'sunshine']


def deco_example(deco):
    data = [['Header 1', 'Header 2', 'Header 3'],
            ['Element 1', 'value_1', 'value_2'],
            ['Element 2', 'value_1', 'value_2'],
            ['Element 3', 'value_1', 'value_2']]

    return tabulate(data, headers='firstrow', tablefmt=deco)


print(deco_example('grid'))
