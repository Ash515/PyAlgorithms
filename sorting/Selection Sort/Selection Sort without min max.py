list1=[34,5,6,81,0,5]
for i in range(len(list1)):
    m_val=list1[i]
    for j in range(i+1,len(list1)):
        if list1[j]<m_val:
            m_val=list1[j]
    
    m_ind=list1.index(m_val,i)
    list1[i],list1[m_ind]=list1[m_ind],list1[i]

print(list1)





