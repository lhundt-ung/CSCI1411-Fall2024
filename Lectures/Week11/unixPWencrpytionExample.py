import crypt

#Hashing function examples with SALT
password = "h@cker"
salt = "CS"
encrpytedPassword = crypt.crypt(password,salt)
print("First encypted Password: ", encrpytedPassword)


#Different password, same salt
password = "h@ckerman"
encrpytedPassword = crypt.crypt(password,salt)
print("Second encypted Password: ", encrpytedPassword)

#Same password, different salt
password = "h@ckerman"
salt="HX"
encrpytedPassword = crypt.crypt(password,salt)
print("Third encypted Password: ", encrpytedPassword)
