import random


random_variable = random.random()
random_int_variable = random.randint(7 , 90)
random_range_variable  = random.randrange(100 ,1000 , 5)
random_uniform_variable = random.uniform(3 , 5)



sample_list = [1,2,3,45,6]
choice_variable = random.choice(sample_list)
random.shuffle(sample_list)
print(sample_list)