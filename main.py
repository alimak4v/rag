from core.embedder import get_embedding
from core.vector_base import *

while True:
    type_ = input("\n\nADD/FIND/ALL: ")
    if type_ == "ADD":
        line = input(">>> ")
        add(line)
    elif type_ == "FIND":
        line = input(">>> ")
        print(find(line))
    elif type_ == "ALL":
        print(all())
    else:
        print("please try again...")