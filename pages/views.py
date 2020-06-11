from django.shortcuts import render
import random
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비','탕수육','초밥','스파게티돈까스']
    pick = random.choice(menu)
    return render(request, 'hello.html',{'pick':pick})

def name(request):
    my_name = '이준성'
    return render(request, 'name.html', {'my_name':my_name})

def introduce(request):
    # my_info = ['이준성', '100']
    name = '이준성'
    age = 100
    major = 'Electrical Engineering'
    interest_field = 'IoT'
    github_url = 'https://github.com/junes7/'

    context = {
        'name' : name,
        'age' : age,
        'major' : major,
        'interest_field' : interest_field,
        'giturl' : github_url
    }
    # return render(request, 'introduce.html', {'my_name':my_info[0], 'my_age':my_info[1]})
    return render(request, 'introduce.html', context)

# 1. 리스트에 반 학생 5명 작성
# 2. 해당 리스트에서 무작위 한 명 선택
# 3. 그 학생 이름 출력하는 페이지 작성
def classroom(request):
    student = ['이준성','황제윤','김현정','백승재','심재민','이정윤']
    pick = random.choice(student)
    context = {
        'pick' : pick
    }
    return render(request, 'classroom.html', context)

def yourname(request, name):
    # name = name
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', context)

# Q1. 이름과 나이 받아보기
# 1. url 경로에 이름과 나이(반드시 int)입력
# 1-1. urls.py에 경로 설정 시
# <> 꺽쇠 형태로 구분하여 표현
# 2. 입력 받은 내용을 페이지에 출력
def yourinfo(request, name, age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'yourinfo.html', context)

# Q2. 숫자 곱한 값 보여주기
# 1. url 경로에 숫자 2개를 입력 받아서
# 2. 두 값을 곱한 값을 페이지에 출력
# 출력 형태
# {{num1}} 곱하기 {{num2}} 는 {{결과값}} 출력

def multiply(request, num1, num2):
    num3 = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'num3' : num3,
    }
    return render(request, 'multiply.html', context)

# Q3. 구구단 리스트 만들기
# 1. 숫자 2개를 입력받아서
# 2. 첫번째 숫자 만큼 반복하는데 range(1, num1)
# 2-1. for data in range(1, num1)
# 3. num2
# 4. list.append(data*num2)
def pigeon(request, big, small):
    result = []
    if big < small :
        big, small = small, big
    for data in range(1, small+1):
        result.append(big*data)
    context = {
        'big' : big,
        'small' : small,
        'result' : result
    }
    return render(request, 'pigeon.html', context)

def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = "Life is short, You need Python"
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today
    }
    return render(request, 'dtl.html', context)

def forif(request):
    my_list = [100, 50, 30, 20, 10]
    my_string = '간단한 문자열임'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b
    }
    return render(request, 'forif.html', context)

# 1. 간단한 반복문으로 리스트 각 요소들 출력
# 2. if, else 활용해서 문자열 비교
# 2-1. 내가 넘긴 문자열과 특정한 문자열 비교
# 3. if, elif, else 사용해보기
# {{my_string|length}}
# 3-1. 문자열의 길이가 5 이하면 short,
# 3-2. 문자열의 길이가 10 이상이면 long
# 3-3. 모두 아니면 적당 출력

# 모두 작성하셨다면,
## 1. 반복문으로 리스트 각 요소들을 출력해서
## 2. 해당 요소가 90 이상이면 A
## 3. 해당 요소가 50 이상이면 B
## 4. 그 외면 C 출력

def presentation(request):
    students = ['강인선','곽혜란']
    random.shuffle(students)
    context = {
        'students' : students
    }
    return render(request, 'presentation.html')