def gambler(quarters, usage, final, machine):
    while quarters > 0:
        quarters = quarters - 1
        if usage[0] == 35:
            quarters +=30
            usage[0] = 0
        elif usage[1] == 100:
            quarters +=60
            usage[1] = 0
        elif usage[2] == 10:
            quarters +=9
            usage[2] = 0
        final +=1
        usage[machine]+=1
        machine+=1
        if machine >2:
            machine = 0
    if quarters == 0:
        print(final)
gambler(77,[4,9,3],0,0)