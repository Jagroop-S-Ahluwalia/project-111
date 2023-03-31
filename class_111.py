import os
import shutil


# print(os.getcwd)

# # mypath = r"C:\Users\jagsm\Desktop\python\class 111"
# # print(os.listdir(mypath))

# mypath = r"C:\Users\jagsm\Desktop\python\class 112"
# mypath2 = r"C:\Users\jagsm\Desktop\python\class 213"

# # os.mkdir(mypath)
# # print("done")

# # print(os.path.exists(mypath))


# # rename = os.rename(mypath, mypath2)

# colour1 = r"C:\Users\jagsm\Desktop\python\class 111\colour 1.jpg"

# spliting = os.path.splitext(colour1)

# print(spliting[0])

colour1=r"C:\Users\jagsm\Desktop\python\class 111\colour 1.jpg"
d = r"C:\Users\jagsm\Desktop\python\class 213"

moving = shutil.move(colour1,d)

