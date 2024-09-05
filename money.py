import json#총액이 얼마인지를 저장하고 다시 가져오기 위해 가져옴
import atexit  #강제 종료를 위해서 가져옴
import datetime

date=datetime.date.today()

#mony.json 파일에서 데이터 가져오기
with open('money.json','r')as file:
    total_money_data=json.load(file)

if total_money_data["money"]=='':
    total_money=0
else:
    total_money=total_money_data['money']



#c언어의 구조체를 생각해서 파이썬에 무엇이 있나 생각을 하다가 class를 쓰는것
class income:
    repeat_cheak_income=0
    
    def __init__(self,message,money):
        income.repeat_cheak_income+=1
        self.message=message
        self.money=money
        self.instance_name=f"수입{income.repeat_cheak_income}"

    def __str__(self):
        return f"{self.instance_name}:{self.message},{self.money}"


class outcome:
    repeat_cheak_outcome=0

    def __init__(self,message,money):
        outcome.repeat_cheak_outcome+=1
        self.message=message
        self.money=money
        self.instance_name=f"지출{outcome.repeat_cheak_outcome}"

    def __str__(self):
        return f"{self.instance_name}:{self.message},{self.money}"
    


income_list=[]
outcome_list=[]


#input으로 내용과 가격을 입력 받는다
while True:
    user_input=input('수입 or 지출=')


    if user_input== "수입":
        user_result=input("수입 내용을 입력하시오=")

        user_money_income= int(input("얼마를 받았나요?="))
        total_money+=user_money_income

        income_instance = income(user_result, user_money_income)
        income_list.append(income_instance)
        income_list.append(date)
        

        print(income_instance)


    if user_input=="지출":
        user_result=input("지출 내용을 입력하시오")
        
        user_money_out=int(input("지출 내용을 입력하시오"))
        total_money-=user_money_out

        outcome_instance= outcome(user_result,user_money_out)
        outcome_list.append(outcome_instance)
        outcome_list.append(date)

       

    print(f"현재 잔액은{total_money}원 있습니다")
    if user_input=="":
        break


def save_income():
    f = open("income.txt", "a")

    for _ in income_list:
        f.write(str(_) + "\n")
    f.close()
atexit.register(save_income)

def save_outcome():
    d= open("outcome.txt","a")
    for __ in outcome_list:
        d.write(str(__)+"\n")
    d.close()
atexit.register(save_outcome)


data={"money":total_money}

with open("money.json","w") as file:
    json.dump(data ,file)



        
# 1.클래스로 데이터를 저장한다
# 2.다음은 그것을 list로 저장한다.
# 3.다음은 그것을 어떻게 저장을 한다
        



#매월 초기화되는것도 해야한다



