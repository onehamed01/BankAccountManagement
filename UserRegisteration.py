import json

class RegisterAccount:
    def __init__(self, fullname: str, age: int,  contact: int, postcode: str, init_amount = 0):
        self.fullname = fullname
        self.age = age
        self.contact = contact
        self.postcode = postcode
        self.init_amount = init_amount

    def save_data(self):
        db = []
        try:
            with open("db.json", 'r', encoding='utf-8') as f:
                db = json.load(f)
        except Exception as e:
            print(f"Error: {e}. File has Created")

        db.append({
            "Fullname":self.fullname,
            "Age":self.age,
            "Contact":self.fullname,
            "Postcode":self.postcode,
            "Amount":self.init_amount,
        })
        
        with open("db.json", 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=4)

    
hami = RegisterAccount("Hamed Mohammad vand", 23, 7733009227, "NE4 8QH", 120)
sophia = RegisterAccount("Sophia Marlin", 27, 7733009389, "NE6 1BH", 80)
hami.save_data()
sophia.save_data()
