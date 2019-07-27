from inmemory import InMemoryImpl

while True:

    print("*"*100)
    print("------------- 1.Add   2.View All  3.Update  4.Delete  5.Search  6.Exit -------------")
    print("*"*100)
    ch = int(input("Enter your Choice :"))

    if ch == 1:
        InMemoryImpl.add_contact()
    
    elif ch == 2:
        InMemoryImpl.view_contact()
    
    elif ch == 3:
        InMemoryImpl.update_contact()
    
    elif ch == 4:
        InMemoryImpl.delete_contact()
    
    elif ch == 5:
        InMemoryImpl.search()
    
    else:
        break