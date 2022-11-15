"""Компьютер угадыает число"""

import numpy as np
def random_predict(number:int=1) -> int: #компьютер рандомно угадывает число
    """Угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток"""

    count=0
    max_number=100
    min_number=1

    while True:
        count+=1
        predict_number=int (np.random.randint(1,101)) #компьютер предполагает число
        predict_number=(max_number+min_number)//2
        if predict_number>number:
            max_number=predict_number-1
        elif predict_number<number:
            min_number=predict_number+1
        elif number==predict_number:
            break #компьютер угадал число, конец игры
            
    return count
print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) ->int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгорит
    
    Args:
        random_predict([type]): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """

    count_ls=[]
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array=np.random.randint(1,101,size=(1000)) #загадываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score=int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за:{score} попыток')
    return score

print(f"Среднее количество попыток: {random_predict()}")
