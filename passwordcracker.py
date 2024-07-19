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
    password = ['','','','']
    for a in chartset:
        password[0] = a

        for b in chartset:
            password[1] = b

            for c in chartset:
                password[2] = c
                
                for d in chartset:
                    password[3] = d

                    if hashlib.md5("".join(password).encode('utf-8')).hexdigest() == hash:
                        print("Password found{0}".format("".join(password)))
                        return("".join(password))
                    print("".join(password))





"""

def function_name(arguments):
    code
"""