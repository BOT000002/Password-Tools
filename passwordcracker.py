chartset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
import hashlib




# generate password
# Generate num characters from cghar list

"""password = ['','','','']
for a in chartset:
    password[0] = a

    for b in chartset:
        password[1] = b

        for c in chartset:
            password[2] = c
            
            for d in chartset:
                password[3] = d

                if "".join(password) == hash:
                    print("Password found{0}".format("".join(password)))
                print("".join(password))"""


def password_cracker(hash):
    pass_list = []
    password = ['','','','']
    for a in chartset:
        password[0] = a

        for b in chartset:
            password[1] = b

            for c in chartset:
                password[2] = c
                
                for d in chartset:
                    password[3] = d
                    # Controls password printing
                    #print(hashlib.md5("".join(password).encode('utf-8')).hexdigest())
                    pass_list.append(hashlib.md5("".join(password).encode('utf-8')).hexdigest())
                    if hashlib.md5("".join(password).encode('utf-8')).hexdigest() == hash:
                        for passw in pass_list:
                            print(passw)
                        print("Password found: {0}".format("".join(password)))
                        return("".join(password))
    return False
                    #print("".join(password))




while True:
    user_hash = input("Enter Hash Here ").strip()

    if len(user_hash) == 32:
        password = password_cracker(user_hash)
        if password is False:
            print("Password not found")
        # if password not found?
    else:
        print("32 characters needed")
