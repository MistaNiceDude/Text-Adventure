import sys
import time
import random
import rooms

HEALTH = 20
weapons = []
SHIRTS = ('cloth tunic', 'chain mail', 'leather shirt', 'plate armor','leather armor')

print('Welcome to a Text Quest')

print('Would you like to play')
confirmation = input()
if confirmation.lower() == 'y' or 'yes':
    print('Sweet lets go on an adventure')
else:
    sys.exit()
time.sleep(1)

def room1():
    global weapons
    print('As we walk we find a small cottage with smoke flowing from the chimney, the place looks friendly enough, should\
 we (G)o in or (W)alk away')
    choice = input()
    if choice == 'W':
        print('You walk past the cabin quietly, as to not disturb the owner')
    if choice == 'G':
        print('As we enter the cottage, we are greeted with a baseball bat to the back of the head....')
        time.sleep(4)
        print('"What the heck was that" you yell. As the blur leaves your eyes you see a scragly hunchbacked man leaning \
over a pot of boiling water singing a little tune.')
        time.sleep(1)
        print('Fresh meat for me, fresh meat for we, fresh meat for all of us to see!')
        time.sleep(.5)
        print('You think to yourself "Fresh meat"... "Us"... You look around and see no one but the old man.')
        print('And then you wonder wheres the fresh meat as you don''t see any animals lying around, IS HE GOING TO EAT YOU \
what are you going to do. (P)ick up the baseball bat and run or (T)ry to talk to the man and maybe earn a friend')
        decision = input()
        if decision == 'P':
            weapons.append('bat')
            return weapons



rooms = (room1)
print('We wake up in the middle of the forest with only a shirt and pants on, and we don\'t remember how we got here\
 or why we are here')
time.sleep(.5)
print('Which direction should we go after we stand up' '(L)eft, (R)ight, (S)traight')
direction = input()
if direction == 'left':
    room1()
print(f'Weapons in inventory: ' + {weapons})
 #   print('To the left we find a little cottage with smoke coming from the chimney. It seems like a friendly enough place\
 #should we go in or leave. (G)o in, (L)eave')
#elif direction == 'right':
 #   print('To the right we run into a pack of wolves and get bitten and lose 5 health, if we find a weapon we should pick\
 #so we can use it next time')
  #  HEALTH -= 5
   # print('Health = ' + str(HEALTH))
#elif direction == 'straight':
 #   print('Straight ahead there is a mountain that we must climb to get to other side')

#rooms.room1()


