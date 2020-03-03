trainings = {'Course1': {'Tariner': 'Adam Frust', 'Level': 'Beginner', 'Subject': 'Programming in Java'},
             'Course2': {'Tariner': 'George Rodney', 'Level': 'Intermediate', 'Subject': 'Programming in Python'},
             'Course3': {'Trainer': 'Mark Sweet', 'Level': 'Expert', 'Subject': 'Programming in C#'}
             }
trainings2 = trainings.copy()
trainings['Course3']['Trainer'] = 'Mark Roug'  #zmiana wartości w kopi mimo że edytujemy oryginał
trainings['Course2'] = {'Trainer': 'Ada Linz', 'Level': 'Novice', 'Subject': 'Programming in C++'}  #nie zmienia się wartość kopii, jedynie oryginału
print(trainings2['Course3'])
print(trainings2['Course2'])