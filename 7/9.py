import pickle
import math
import dill
import bz2

# class example_class:
#     a_number = 35
#     a_string = "hej"
#     a_list = [1, 2, 3]
#     a_dict = {"first": "a", "second": "b", "third": [1, 2, 3]}
#     a_tuple = (22, 23)
#
# my_object = example_class()
#
# my_pickled_object = pickle.dumps(my_object)
# print(f"To są obiekty spiklowane\n{my_pickled_object}")
#
# my_object.a_dict = None
# #
# my_unpickled_object = pickle.loads(my_pickled_object)
# print(f"To są obiekty odpiklowane\n{my_unpickled_object.a_dict}")

# square = lambda x: x * x
# a = square(35)
# b = math.sqrt(484)
# dill.dump_session('testowo.pkl')
# exit()
#
# dill.load_session('testowo.pkl')
# print(globals().items())

# class foobar:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         del attributes['c']
#         return attributes
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
# my = foobar()
# new_pickle = pickle.dumps(my)
# my_new = pickle.loads(new_pickle)
# print(my_new.__dict__)

my_string = """65-letnia mieszkanka Suwałk zainteresowała się reklamą internetową, oferującą możliwość — jak przekonywano — szybkiego zysku bez ryzyka.
 Otworzyła link, by się z tą ofertą zapoznać; okazało się, że musi podać swój numer telefonu. Wtedy skontaktowali się z nią rzekomi doradcy inwestycyjni, 
 oferując pomoc przy dokonywaniu inwestycji.
"""

pickled = pickle.dumps(my_string)
compressed = bz2.compress(pickled)
print(len(my_string))
print(len(compressed))