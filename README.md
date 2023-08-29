# red_black_tree
## Most of the BST operations (e.g., search, max, min, insert,) take O(h) time where h is the height of the BST. The cost of these operations may become O(n) for a skewed Binary tree. If we make sure that the height of the tree remains O(log n) after every insertion and deletion, then we can guarantee an upper bound of O(log n) for all these operations. The height of a Red-Black tree is always O(log n) where n is the number of nodes in the tree. 
### Functions Implemented :
### Search: Search for a specific element in a Red-Black Tree. 
### Insertion: Insert a new node in a Red-Black tree. Tree balance must be maintained via the rotation operations. 
### Print Tree Height: Print the height of the Red-Black tree. This is the longest path from the root to a leaf-node. 
### Print Tree size: Print the number of elements in Red-Black tree. 
## Application:
### A simple English dictionary, with a simple text-based user interface, supporting the following functionalities:
### 1. Load Dictionary: loads the dictionary into a Red-Black Tree data structure to subbort efficient insertions and search operations. 
### 2. Print Dictionary Size: Prints the current size of the dictionary. 
### 3. Insert Word: Takes a word from the user and inserts it, only if it is not already in the dictionary. Otherwise, prints the appropriate error message (e.g. “ERROR: Word already in the dictionary!"). 
### 4. Look-up a Word: Takes a word from the user and prints “YES" or “NO" according to whether it is found or not. 

