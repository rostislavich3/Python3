from skpy import Skype, SkypeChats

sk = Skype("username", "password")
skc = SkypeChats(sk)
print(skc.recent())
