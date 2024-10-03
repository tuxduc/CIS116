highway_number = int(input())

#if any below are true, give invalid and stop
if highway_number == 0:
    print(highway_number, 'is not a valid interstate highway number.')
    exit()
if highway_number == 200:
    print(highway_number, 'is not a valid interstate highway number.')
    exit()
if highway_number == 1000:
    print(highway_number, 'is not a valid interstate highway number.')
    exit()

if 1<=highway_number<=99:
    if highway_number %2 == 0:
        direction= 'east/west.'
    else:
        direction= 'north/south.'
    print(f"I-{highway_number} is primary, going {direction}")

if 100<=highway_number<=999:
    if highway_number %2 == 0:
        direction= 'east/west.'
    else:
        direction= 'north/south.'
    if str(highway_number)[1]== "0":
        print(f"I-{highway_number} is auxiliary, serving I-{str(highway_number)[-1]}, going {direction}")
    if str(highway_number)[2]== "0":
        print(f"I-{highway_number} is auxiliary, serving I-{str(highway_number)[-2:]}, going {direction}")