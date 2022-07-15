from re import A


alien_0 = {'color':'green', 'points': 5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

for key, value in sorted(alien_0.items()):
    print("\nKey: " + key)
    print("Value: "+ str(value))