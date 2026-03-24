class FriendsSystem:
    def __init__(self):
        self.group_Member = []
        self.other_friends = {}



    def New_group(self):
        name = input('Name : ')
        if name not in self.group_Member:
            self.group_Member.append(name)
            print(f'ADD ==={name}=== IN GROUP SUCCESS !!!')
        else:
            print('THIS PERSON IS ALREADY IN THE GROUP')



    def AddOtherFriends(self):
        MemberName = input('ADD FRIENDS : ')

        if MemberName in self.group_Member:
            friendsOutGroup = input(f'ADD THE FRIENDS THE {MemberName}: ')
            self.other_friends[friendsOutGroup] = MemberName
            print(f'ADD ==={friendsOutGroup}=== IN THE GROUP SUCCESS')
        else:
            print(f'NONE DETECTED ==={MemberName}=== IN THE GROUP')


    
    def ShowGroupMember(self):
        print('\n===== MEMBER GROUP NAME =====')
        
        if not self.group_Member:
            print('THERE ARE NO MEMBERS IN THE GROUP')
        else:
            for idx, name in enumerate(self.group_Member, 1):
                print(f'{idx}.{name}')



    def Find_Who_added(self):
        friendsName = input("ADD THE NAME OF THE FRIENDS YOUR WANT TO CHECK : ")
        added_by = self.other_friends.get(friendsName)

        if added_by:
            print(f'THE {friendsName} WAS ADDED TO THE GROUP BY {added_by}')
        else:
            print(f'NONE DETECTED FRIENDS NAME IS ==={friendsName}=== IN THE SYSTEM')



class main:
    system = FriendsSystem()

    while True:
        print("\n===== FRIEND-FINDING SYSTEM (Test Mode) =====")
        print("1. NEW GROUP ")
        print("2. ADD OTHER FRIENDS ")
        print("3. GROUP MEMBERS ")
        print("4. THIS PERSON IS A FRIEND OF ")
        print("0. EXIT")

        choice = input('ENTER MENU : ')
        match choice:
            case '1': system.New_group()
            case '2': system.AddOtherFriends()
            case '3': system.ShowGroupMember()
            case '4': system.Find_Who_added()
            case '0': 
                print("CLOSE THE PROGRAME") 
                break
            case _:
                print('NO CHOICE I SUS YARUNGMAK I SHIP HAY')

if __name__ == '__main__':
    main()