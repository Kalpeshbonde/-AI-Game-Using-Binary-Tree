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
    # Your tree construction logic remains the same
    pass


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
    # Read the content of game1.txt and construct the tree
    with open("/content/game1.txt", "r") as file:
        tree_content = file.read()

    root = eval(tree_content)

    while True:
        instruct()
        play(root)
        if not query("Shall we play again?"):
            print("Thanks for teaching me a thing or two.")
            print("Here is the tree:")
            root.print_tree()
            break
