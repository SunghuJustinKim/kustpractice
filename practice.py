print("Welcome to my first practice game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10

if age >= 18:
    print("You are old enough!")

    weapon = input("pick a weapon (sword/shield): ")

    play = input("Do you want to play? ").lower()
    if play == "yes":
        print("Let's play!")
        print("You are starting with", health, "health")
        left_or_right = input("First choice... Left or Right? (left/right)? ")
        if left_or_right == "left":
            ans = input("Travel down a path and reach a lake..Do you swim across or go around? (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side! ")

            elif ans == "across":
                print("You lost 5 health while swimming across the lake!")
                health -= 5
            ans = input("you notice a house and a river. Which do you go to? (river/house)? ")
            if ans == "house":
                print("You go to the house and lose 5 hp from a trap on the floor")
                health -= 5

                if health <=0:
                    print("you died because you had zero hp")
                else:
                    print("you lived and won!")
            elif ans == "house" and weapon == "shield":
                print("you won!")
        
        else:
            print("You died")

    else:
        print("Goodbye!")
else:
    print("You are not old enough to play...")


"""
elif age >= 14:
    print("You can play with parents!")

    play = input("Do you have a parent? ").lower()
    if play == "yes":
        print("Let's play!")

          weapon = input("pick a weapon (sword/shield): ")
    
    if weapon ==

    and or 
    if one of them are true it prints true
""" 
 










'''
str "hello", "hi", "89"
int 8, 7, 9 ,-10
float 6.0, 7.5, -9.8
bool True, False
'''