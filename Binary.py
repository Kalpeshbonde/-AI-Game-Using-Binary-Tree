class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class MovieGuessingGame:
    def __init__(self, file_name="game1.txt"):
        self.title = ""
        self.help_info = ""
        self.root = None
        self.load_game(file_name)

    def load_game(self, file_name):
        with open(file_name, 'r') as file:
            self.title = file.readline().strip()
            self.help_info = file.readline().strip()
            self.root = self._build_tree(file)

    def _build_tree(self, file):
        def build_tree_recursive(file):
            line = file.readline().strip()
            if not line:
                return None

            parts = line.split(' ', 1)
            node_data = parts[0]
            question_or_answer = parts[1]

            node = TreeNode(node_data, None, None)
            if question_or_answer.startswith('Q'):
                node.left = build_tree_recursive(file)
                node.right = build_tree_recursive(file)

            return node

        return build_tree_recursive(file)

    def play_game(self):
        current_node = self.root

        while current_node:
            print(current_node.data)

            if not current_node.left and not current_node.right:
                break

            answer = input("Answer (Y/N): ").upper()

            while answer not in ["Y", "N"]:
                print("Invalid answer. Please enter 'Y' or 'N'.")
                answer = input("Answer (Y/N): ").upper()

            if answer == "Y":
                current_node = current_node.left
            else:
                current_node = current_node.right

    def display_tree(self):
        print("\nBinary Tree:")
        order = input("What order do you want to display?\n1. Inorder\n2. Preorder\n3. Postorder\n4. Return to main menu\n... your choice: ")
        if order.isdigit() and 1 <= int(order) <= 3:
            self._display_tree_order(self.root, int(order))
        else:
            print("Invalid traversal order.")

    def _display_tree_order(self, node, order):
        if order == 1:
            self._inorder_traversal(node)
        elif order == 2:
            self._preorder_traversal(node)
        elif order == 3:
            self._postorder_traversal(node)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.data)
            self._inorder_traversal(node.right)

    def _preorder_traversal(self, node):
        if node:
            print(node.data)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def _postorder_traversal(self, node):
        if node:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.data)

    def display_help(self):
        print("\nHelp Information:")
        print(self.help_info)


# Main program
if __name__ == "__main__":
    game = MovieGuessingGame()

    while True:
        print("\nMenu Operations:")
        print("P: Play the game")
        print("L: Load another text file")
        print("D: Display the binary tree")
        print("H: Help information")
        print("X: Exit the program")

        choice = input("...your choice: ").upper()

        if choice == "P":
            game.play_game()
        elif choice == "L":
            file_name = input("Enter the file name to load: ")
            game.load_game(file_name)
        elif choice == "D":
            game.display_tree()
        elif choice == "H":
            game.display_help()
        elif choice == "X":
            break
        else:
            print("Invalid choice. Please choose again.")
