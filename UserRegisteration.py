import json
import random

class RegisterAccount:
    def __init__(self, fullname: str, age: int,  contact: int, postcode: str, init_amount = 0):
        self.fullname = fullname
        self.age = age
        self.contact = contact
        self.postcode = postcode
        self.init_amount = init_amount

    def __cardnumber_generator(self, defualt = "4971"):
        random_cardnumber = "".join(str(random.randint(1, 9)) for _ in range(10))
        return defualt+random_cardnumber

    def save_data(self):
        db = []
        try:
            with open("db.json", 'r', encoding='utf-8') as f:
                db = json.load(f)
        except Exception as e:
            print(f"Error: {e}. File has Created")

        cardnumber = int(self.__cardnumber_generator())
        db.append({
            "Fullname":self.fullname,
            "Age":self.age,
            "Contact":self.fullname,
            "Postcode":self.postcode,
            "Amount":self.init_amount,
            "Cardnumber":cardnumber
        })
        print(f"Ms/Mr. {self.fullname}\nyour card number is {cardnumber}")        
        with open("db.json", 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=4)

  

    def search_fullname(self, fullname = None):
        with open("db.json", 'r', encoding='utf-8') as f:
            db = json.load(f)
            
        for x in db:
            if x['Fullname'] == fullname:
                for x,y in x.items():
                    print(f"{x}: {y}")
            else:
                print("We don't find any information")
            break

acc1 = RegisterAccount("Hami MDV", 23, 7700112233, "NE4 8QH", 5000)
acc2 = RegisterAccount("Mastaneh Noroozi", 24, 7711223344, "NE4 5QH", 300)
acc3 = RegisterAccount("Ali Rahimi", 30, 7722334455, "NE3 6PL", 1500)
acc4 = RegisterAccount("Sara Karimi", 28, 7733445566, "NE2 4LG", 800)


acc1.search_fullname(fullname="Hami MDV")