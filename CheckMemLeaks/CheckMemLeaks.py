f_trace=open("program_trace.txt")
list_str=f_trace.readlines()
mem={}
alias={}
n_str={}
flag=False
leak_flag=True
for x in list_str:
    split_str=x.split(" ")
    num_str= int(split_str[0])
    n_str[num_str]=1;
    split_str=split_str[1:]
    for y in split_str:
        if y[0]=="+":
            if y[2]>="0" and y[2]<="9":
                mem_comp=y.split(",")
                mem_num=int(mem_comp[0][2:])
                mem_comp=mem_comp[1:]
                mem_child=[]
                for z in mem_comp:
                    if z.find("(")!=-1:
                        mem_child.append(int(z[z.find("(")+1:]))
                        continue
                    if z.find(")")!=-1:
                        mem_child.append(int(z[:z.find(")")]))
                        continue
                    mem_child.append(int(z))
                mem[mem_num]=mem_child
            else:
                aliases=y.split(",")
                alias_num=int(aliases[1][:aliases[1].find(">")])
                list_alias=[]
                if alias.get(alias_num)!=None:
                    list_alias=alias.get(alias_num)
                list_alias.append(aliases[0][aliases[0].find("<")+1:])
                alias[alias_num]=list_alias
            if flag:
                mem_t=mem.copy()
                mem_keys=list(mem_t)
                mem_keys.sort()
                mem_keys.reverse()
                for i in range(len(mem_keys)):
                    for j in range(i+1,len(mem_keys)):
                        list_child=mem_t.get(mem_keys[j])
                        if mem_keys[i] in list_child:
                            del mem_t[mem_keys[i]]
                            break
                    if mem_t.get(mem_keys[i])!=None:
                        if alias.get(mem_keys[i])!=None:
                            del mem_t[mem_keys[i]]
                        else:
                            leak_flag=False
                            print("Check if there is a memory leak on ",num_str," line")
                flag=False
                if len(mem_t)!=0:
                    leak_flag=False
                    print("Check if there is a memory leak after comand on ",num_str," line")
        else:
            if y[2]>="0" and y[2]<="9":
                mem_comp=y.split(",")
                del mem[int(mem_comp[0][2:])]
            else:
                aliases=y.split(",")
                alias_num=int(aliases[1][:len(aliases[1])-2])
                list_alias=alias.get(alias_num)
                list_alias.remove(aliases[0][2:])
                if len(list_alias)==0:
                    del alias[alias_num]
                else:
                    alias[alias_num]=list_alias
            flag=True
if leak_flag:
    print("No memory leaks was found for trace - ",list(n_str))
