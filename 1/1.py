# print([x for x in dir(__builtins__) if 'Error' in x])
import logging


def mutli(a, b) -> int:
    '''
    Raises: TypeError: W przypadku gdy parametry nie będą liczbami
    :param a:
    :param b:
    :return: int
    '''
    try:
        return a * b
    except TypeError:
        logging.warning('Niedozwolona operacja')
    except ValueError:
        logging.warning('Niedozwolona operacja2')


# print(mutli(2, 'a'))
# print(mutli(2, None))


def mutli2(a, b):
    try:
        return a * b
    except Exception as e:
        logging.warning(e)


# print(mutli2('2','3'))

valid_data = [{'name': 'Jan', 'age': '10'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_dict = [{}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_dict2 = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print('Niepoprawne dane: {}'.format(user))
        except ValueError:
            print('Niepoprawny wiek: {}'.format(user))
        else:
            count += 1 if user_age < age else 0
        finally:
            print("{},{}".format(i, user))
        return count


check_age(invalid_dict2, 18)

import ipdb;ipdb.set_trace()