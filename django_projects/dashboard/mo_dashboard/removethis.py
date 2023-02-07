filename = "curaminputdata"    # your own filename
with open('curaminputdata','r') as file:
    to_return = []
    #a = file.readlines()
    a = file.read().splitlines()

    #print(a)
    for tab in a:
        tab = tab.split('|')
        to_return.append(tab)
    #print(to_return)

name={'firstkey':to_return}
print(name)
'''for v in name.values():
    for k in v:
        env=k[0]
        time=k[1]
        wo=k[2]
        print(env)
        print(time)
        print(wo)
   # print(v)
    #env=v[0]
    #time=v[1]
    #whichone=v[2]
    #print(env)
    #print(time)
    #print("env is" +env)
    #print("time is"+env)
    #print("whichone is"+env)
    #print(v)
#for i in name:
#    print(i)
#print(name['firstkey'][1])
#print(type(name['firstkey'][1]))'''