#ADD YOUR OWN PASSWORD HERE, AS A STRING
myPassword = #a string of your choice

#DO NOT MODIFY ANY CODE BELOW
import hashlib
m = hashlib.md5()
m.update(bytes(myPassword, "utf-8"))
print(m.digest())
