slide 7 dict 사전코드 작성

sensors = {
    'dht11': {
        'temperature': 23,
        'humidity': 47,
        'unit': 'celsius'
    },
    'bh1750': {
        'illuminance': 450,
        'unit': 'lux'
    }
}
slide 33 - 2, 3, 4 코드 작성 thonny

2.
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

if month == 8 and day == 15:
    print("광복절")
elif (month % 2 == 1 and day == 15) or (month % 2 == 0 and day == 16):
    print("그날")
else:
    print("평일")
    
    
    
    <img width="526" height="125" alt="image" src="https://github.com/user-attachments/assets/6886a827-1ae8-4ae0-b3b5-84887cc5d04f" />
    <img width="382" height="145" alt="image" src="https://github.com/user-attachments/assets/57fde37c-b0ac-40bc-b477-e3940cc7fe55" />
    <img width="433" height="103" alt="image" src="https://github.com/user-attachments/assets/0f72a4e0-11be-4582-b66a-7a97550aaccc" />


3.
total = 0

for i in range(1, 51):
    if i % 2 == 0 and i % 3 != 0:
        total += i

print(total)



<img width="313" height="62" alt="image" src="https://github.com/user-attachments/assets/f84ad395-9213-48c5-a6c5-dde9a8dcbeba" />

4.
total = 0
i = 1

while i <= 50:
    if i % 2 == 0 and i % 3 != 0:
        total += i
    i += 1

print(total)




<img width="704" height="524" alt="image" src="https://github.com/user-attachments/assets/c9d6fb13-ac0b-4b85-b0ff-13eb8e97669c" />
