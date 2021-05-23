import random
from deap import base, creator, tools

#определение функции оценки
def eval_func(individual):

    target_sum = 15
    return len(individual) - abs(sum(individual) - target_sum),

#набор инструментов с правильными параметрами
def create_toolbox(num_bits):

    creator.create("FitnessMax", base.Fitness, weights = (1.0,))
    creator.create("Individual", list, fitness = creator.FitnessMax)

    #инициализация панели инструментов
    toolbox = base.Toolbox()
    toolbox.register("attr_bool", random.randint, 0, 1)#атрибуты
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, num_bits)#инициализация структуры
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)#определяем популяцию как список людей
    toolbox.register("evaluate", eval_func)#оператор оценки
    toolbox.register("mate", tools.cxTwoPoint)#оператор скрещивания
    toolbox.register("mutate", tools.mutFlipBit, indpb = 0.05)#оператор мутации
    toolbox.register("select", tools.selTournament, tournsize = 3)#оператор для разведения

    return toolbox

if __name__ == "__main__":

    num_bits = 45
    toolbox = create_toolbox(num_bits)
    random.seed(7)#Генератор случайных чисел

    population = toolbox.population(n = 500)#Создание начальной популяции в 500 поколений
    probab_crossing, probab_mutating = 0.5, 0.2 #Определение вероятности скрещивания и мутации
    num_generations = 10 #Определение количества поколений
    print('\nEvolution process starts')

    #Оценка всего населения
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    print('\nEvaluated', len(population), 'individuals')

    #Создание и вывод печати
    for g in range(num_generations):
        print("\n --- Generation", g)
        offspring = toolbox.select(population, len(population))#Выбор следующего поколения
        offspring = list(map(toolbox.clone, offspring))#Клонирование

        #Применение скрещиваения и мутации на потомство
        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            #Скрещиваем два поколения
            if random.random() < probab_crossing:
                toolbox.mate(child1, child2)

                #Удаление значения фитнеса ребенка
                del child1.fitness.values
                del child2.fitness.values

        #Мутация
        for mutant in offspring:
            if random.random() < probab_mutating:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        #Оценка особи с недопустимым значением
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print('Evaluated', len(invalid_ind), 'individuals')

        #Замена неселения на следующее поколение
        population[:] = offspring

        #Печать статистики
        fits = [ind.fitness.values[0] for ind in population]

        length = len(population)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print('Min =', min(fits), ', Max =', max(fits))
        print('Average =', round(mean, 2), ', Standard deviation =', round(std, 2))

    print("\n --- Evolution ends")

    best_ind = tools.selBest(population, 1)[0]
    print('\nBest individual:\n', best_ind)
    print('\nNumber of ones:', sum(best_ind))
