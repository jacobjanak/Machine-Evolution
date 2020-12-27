import random
import copy
from displayTree import display_tree

options = ["Rock", "Paper", "Scissors"]

treeCount = 10
testCount = 100

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def generateRandomTree():
    randomOption = random.choice(options)
    root = Node(randomOption)

    for i in range(2):
        if random.choice([True, False, False]):
            root.children.append(generateRandomTree())
        else:
            randomOption = random.choice(options)
            child = Node(randomOption)
            root.children.append(child)

    return root


def scoreTree(root):
    score = 0
    node = root
    for opponentChoice in options:
        while len(node.children) > 0:
            if opponentChoice == node.value:
                node = node.children[1]
            else:
                node = node.children[0]

        ourChoice = node.value
        if ourChoice == opponentChoice:
            score += 0
        elif ourChoice == "Rock" and opponentChoice == "Scissors":
            score += 1
        elif ourChoice == "Paper" and opponentChoice == "Rock":
            score += 1
        elif ourChoice == "Scissors" and opponentChoice == "Paper":
            score += 1
        elif ourChoice == "Paper" and opponentChoice == "Scissors":
            score -= 1
        elif ourChoice == "Rock" and opponentChoice == "Paper":
            score -= 1
        elif ourChoice == "Scissors" and opponentChoice == "Rock":
            score -= 1

        node = root
        
    return score


def evolveTree(tree):
    tree = copy.deepcopy(tree)
    node = tree
    while len(node.children) > 0:
        nextChildIndex = random.choice([0, 1])
        if random.choice([True, False]):
            if random.choice([True, False]):
                node.children[nextChildIndex] = generateRandomTree()
            else:
                node.children[nextChildIndex] = Node(random.choice(options))
            return tree
        else:
            node = node.children[nextChildIndex]
    
    # if we get to end of tree, make a random evolution to the last node
    node.value = random.choice(options)
    return tree


# original trees get generated randomly
trees = []
for i in range(treeCount):
    trees.append(generateRandomTree())
scores = []
for tree in trees:
    scores.append((tree, scoreTree(tree)))
scores.sort(key=lambda x: x[1], reverse=True)
scores = scores[0:treeCount // 2]


# keep looping through and evolving trees
for _ in range(testCount):
    for i in range(treeCount // 2):
        newTree = evolveTree(scores[i][0])
        newTreeScore = scoreTree(newTree)
        scores.append((newTree, newTreeScore))

    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[0:treeCount // 2]


display_tree(scores[0][0])
print(scores[0][1])