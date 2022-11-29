class Stack:

    def __init__(self, elements=None):
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop()

    def clear(self):
        self.elements.clear()

    @property
    def is_empty(self):
        return len(self.elements) == 0

    @property
    def size(self):
        return len(self.elements)


day_planning = Stack(elements=['answer emails', 'go through slack', 'fill the lab journal', 'do experiments'])

print(f'There are {day_planning.size} activities planned for the day!')

urgent_things = input('Is there anything else that is urgent? ')

while not urgent_things == '':
    day_planning.push(urgent_things)
    urgent_things = input('Is there anything else that is urgent? ')

print(f"We have {day_planning.size} activities in the end. Let's start!")
state = input("Enter 'ready' when you are ready for a new task. "
              "Enter something else if you can't do this anymore. ")

while state == 'ready' and not day_planning.is_empty:
    print(day_planning.pop())
    state = input()

if not day_planning.is_empty:
    print(f"Oh, we have not done yet. There are {day_planning.size} things left.")
    saving = input("Enter 'yes' if you want to save undone things for tomorrow. ")
    if saving != 'yes':
        day_planning.clear()
    print(f'You have {day_planning.size} things planned for tomorrow.')
else:
    print(f"You've done all the things for today, good job!")

print('Have a nice evening!')
