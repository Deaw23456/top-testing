import unicodedata

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = str(age)
        self.group_neighbors = []
        self.random_neighbors = []

    def add_group_friend(self, other_person):
        if other_person not in self.group_neighbors:
            self.group_neighbors.append(other_person)
            other_person.group_neighbors.append(self)

    def add_random_friend(self, p):
        if p not in self.random_neighbors:
            self.random_neighbors.append(p)
            p.random_neighbors.append(self)



class SocialSystem:
    def __init__(self):
        self.all_nodes = {}
        self.group_list = []
        self.random_list = []

    def get_visual_width(self, text):
        count = 0
        for char in text:
            if unicodedata.category(char) != 'Mn':
                count += 1
        return count

    def pad_thai(self, text, width):
        visual_w = self.get_visual_width(text)
        return text + (" " * (width - visual_w))

    def display_table(self, target_list, title):
        if not target_list:
            print(f"\n--- {title} IS EMPTY ---")
            return

    
        rows = []
        for p in target_list:
            all_friends = [f.name for f in p.group_neighbors + p.random_neighbors]
            friend_str = ", ".join(all_friends) if all_friends else "None"
            rows.append([p.name, p.age, friend_str])

    
        headers = ["NAME", "AGE", "FRIENDS (CONNECTED)"]
        col_widths = [self.get_visual_width(h) for h in headers]

        for row in rows:
            for i in range(3):
                col_widths[i] = max(col_widths[i], self.get_visual_width(row[i]))

    
        print(f"\n--- {title} ---")
        border = "+" + "+" .join(["-" * (w + 2) for w in col_widths]) + "+"
        header_row = "| " + " | ".join([self.pad_thai(h, col_widths[i]) for i, h in enumerate(headers)]) + " |"

        print(border)
        print(header_row)
        print(border)

        for row in rows:
            content_row = "| " + " | ".join([self.pad_thai(row[i], col_widths[i]) for i in range(3)]) + " |"
            print(content_row)

        print(border)

    def add_group_member(self):
        name = input("ADD MEMBER NAME: ")
        age = input("AGE: ")
        new_person = Person(name, age)
        self.all_nodes[name.lower()] = new_person
        for existing in self.group_list:
            new_person.add_group_friend(existing)
        self.group_list.append(new_person)
        print(f"✨ ADD {name} SUCCESSFULLY!!!")

    def add_random_connection(self):
        friend_name = input("ADD FRIEND NAME: ")
        age = input("AGE: ")
        voucher_name = input(f"ADD BY (Voucher Name): ").lower()
        if voucher_name in self.all_nodes:
            member = self.all_nodes[voucher_name]
            random_p = Person(friend_name, age)
            member.add_random_friend(random_p)
            self.all_nodes[friend_name.lower()] = random_p
            self.random_list.append(random_p)
            print(f"✅ ADD {friend_name} CERTIFIED BY: {member.name}")
        else:
            print("❌ NO MEMBER WERE FOUND!")

    def find_friend_of(self):
        name = input("ENTER FRIEND NAME: ").lower()
        if name in self.all_nodes:
            p = self.all_nodes[name]
            vouchers = [f.name for f in p.random_neighbors if f in self.group_list]
            print(f"💡 {p.name} IS A FRIEND OF: {', '.join(vouchers) if vouchers else 'Group Member'}")
        else:
            print("❌ NOT FOUND")

def main():
    system = SocialSystem()
    while True:
        print("\n" + "="*10 + " 👥 FRIEND-FINDING SYSTEM " + "="*10)
        print("1. NEW GROUP\n2. ADD OTHER FRIENDS\n3. GROUP MEMBERS\n4. FRIEND OF\n0. EXIT")
        choice = input("## ENTER MENU >> ")
        match choice:
            case "1": system.add_group_member()
            case "2": system.add_random_connection()
            case "3": system.display_table(system.group_list, "GROUP MEMBERS")
            case "4": system.find_friend_of()
            case "0": break
            case _: print("INVALID!")

if __name__ == "__main__":
    main()