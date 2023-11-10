class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

    def print_tree(self, level=1):
        print("  " * (level - 1) + str(level) + ": " + self.data)
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)


def instruct():
    print("Please think of an ocean animal.")
    print("I will ask some yes/no questions to try to figure out which animal you're thinking of.")


def play(current):
    while current:
        if current.is_leaf():
            print("My guess is " + current.data + ".")
            if not query("Am I right?"):
                learn(current)
            else:
                print("I knew it all along!")
            break

        if query(current.data):
            current = current.left
        else:
            current = current.right



def beginning_tree():
    root_question = "Is it a mammal?"
    left_question = "Is it able to move on land?"
    left_question2 = "Is it a solitary animal?"
    right_question2 = "Is it larger than a truck?"
    right_question3 = "Does it have tusks?"
    right_question = "Does it have any limbs/tentacles?"
    left_question4 = "Does it have more than four limbs/tentacles?"
    left_question5 = "Does it have an exoskeleton?"
    left_question6 = "Does it have claws?"
    left_question7 = "Does it have a long tail?"
    right_question7 = "Does it have 8 arms?"
    right_question5 = "Does it have a shell?"
    right_question4 = "Can it sting?"
    left_question8 = "Is it long and snakelike?"
    right_question8 = "Is it generally smaller than a car?"

    animal1 = "Seal"
    animal2 = "Sea Lion"
    animal3 = "Walrus"
    animal4 = "Whale"
    animal5 = "Dolphin"
    animal6 = "Shrimp"
    animal7 = "Lobster"
    animal8 = "Crab"
    animal9 = "Jellyfish"
    animal10 = "Octopus"
    animal11 = "Squid"
    animal12 = "Turtle"
    animal13 = "Alligator"
    animal14 = "Eel"
    animal15 = "Stingray"
    animal16 = "Shark"
    animal17 = "Fish"

    root = BTNode(root_question)
    root.left = BTNode(left_question)
    root.left.left = BTNode(left_question2)
    root.left.left.left = BTNode(animal1)
    root.left.left.right = BTNode(right_question2)
    root.left.left.right.left = BTNode(animal3)
    root.left.left.right.right = BTNode(animal2)
    root.left.right = BTNode(right_question3)
    root.left.right.left = BTNode(animal4)
    root.left.right.right = BTNode(animal5)

    root.right = BTNode(right_question)
    root.right.left = BTNode(left_question4)
    root.right.left.left = BTNode(left_question5)
    root.right.left.left.left = BTNode(left_question6)
    root.right.left.left.left.left = BTNode(left_question7)
    root.right.left.left.left.left.left = BTNode(right_question7)
    root.right.left.left.left.left.left.left = BTNode(animal10)
    root.right.left.left.left.left.left.right = BTNode(animal11)
    root.right.left.left.left.left.right = BTNode(animal7)
    root.right.left.left.left.left.right.left = BTNode(animal8)
    root.right.left.left.left.left.right.right = BTNode(animal9)
    root.right.left.left.right = BTNode(right_question4)
    root.right.left.left.right.left = BTNode(left_question8)
    root.right.left.left.right.left.left = BTNode(animal14)
    root.right.left.left.right.left.right = BTNode(animal15)
    root.right.left.left.right.right = BTNode(right_question8)
    root.right.left.left.right.right.left = BTNode(animal17)
    root.right.left.left.right.right.right = BTNode(animal16)

    return root


def learn(current):
    guess_animal = current.data
    print("I give up. What are you?")
    correct_animal = input().strip()
    print(f"Please type a yes/no question that will distinguish a {correct_animal} from a {guess_animal}.")
    new_question = input().strip()

    current.data = new_question
    print(f"As a {correct_animal}, {new_question}")
    if query("Please answer"):
        current.left = BTNode(correct_animal)
        current.right = BTNode(guess_animal)
    else:
        current.left = BTNode(guess_animal)
        current.right = BTNode(correct_animal)


def query(prompt):
    answer = input(f"{prompt} [Y or N]: ").strip().upper()
    while answer not in ["Y", "N"]:
        answer = input("Invalid response. Please type Y or N: ").strip().upper()
    return answer.startswith("Y")


if __name__ == "__main__":
    root = beginning_tree()

    while True:
        instruct()
        play(root)
        if not query("Shall we play again?"):
            print("Thanks for teaching me a thing or two.")
            print("Here is the tree:")
            root.print_tree()
            break
