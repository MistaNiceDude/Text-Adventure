import time


def room1():
    print('As we walk we find a small cottage with smoke flowing from the chimney, the place looks friendly enough, should\
 we (G)o in or (W)alk away')
    choice = input()
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


