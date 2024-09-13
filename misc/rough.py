fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}
if (__name__ == '__main__'):
    user = input("enter name ---> ")
    while(user!="1"):
        try:
            
            if user in fake_users_db:
                    print(fake_users_db[user])
            else:
                raise IndexError(user)
            
        except IndexError as e:
            print(f"out db bound username >> {e}")
        user = input("enter name ---> ")