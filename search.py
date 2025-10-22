# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = Stack()
    stack.push((problem.getStartState(), []))
    
    # Keep track of visited states to avoid cycles (graph search)
    visited = set()
    
    while not stack.isEmpty():
        state, actions = stack.pop()
        
        # Skip if already visited
        if state in visited:
            continue
        
        # Mark as visited
        visited.add(state)
        
        # Check if we reached the goal
        if problem.isGoalState(state):
            return actions  # Return the path (list of actions)
        
        # Get all possible next states
        for nextState, action, cost in problem.getSuccessors(state):
            if nextState not in visited:
                newActions = actions + [action]  # Add current action to path
                stack.push((nextState, newActions))
    
    return []
    
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    queue = Queue()
    queue.push((problem.getStartState(), []))
    
    # Keep track of visited states to avoid cycles
    visited = set()
    
    while not queue.isEmpty():
        state, actions = queue.pop()
        
        # Skip if already visited
        if state in visited:
            continue
        
        # Mark as visited
        visited.add(state)
        
        # Check if we reached the goal
        if problem.isGoalState(state):
            return actions  # Return the path
        
        # Get all possible next states
        for nextState, action, cost in problem.getSuccessors(state):
            if nextState not in visited:
                newActions = actions + [action]
                queue.push((nextState, newActions))
    
    return []

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    pq = PriorityQueue()
    pq.push((problem.getStartState(), [], 0), 0)  # (item, priority)
    
    # Keep track of visited states
    visited = set()
    
    while not pq.isEmpty():
        state, actions, cost = pq.pop()
        
        # Skip if already visited
        if state in visited:
            continue
        
        # Mark as visited
        visited.add(state)
        
        # Check if we reached the goal
        if problem.isGoalState(state):
            return actions  # Return the path
        
        # Get all possible next states
        for nextState, action, stepCost in problem.getSuccessors(state):
            if nextState not in visited:
                newActions = actions + [action]
                newCost = cost + stepCost  # Total cost so far
                pq.push((nextState, newActions, newCost), newCost)
    
    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    pq = PriorityQueue()
    startState = problem.getStartState()
    
    # Push start node with f = g + h
    pq.push((startState, [], 0), heuristic(startState, problem))
    
    visited = set()
    
    while not pq.isEmpty():
        state, actions, cost = pq.pop()
        
        # Skip already expanded states
        if state in visited:
            continue
        
        visited.add(state)
        
        # Goal check
        if problem.isGoalState(state):
            return actions
        
        # Explore successors
        for nextState, action, stepCost in problem.getSuccessors(state):
            newActions = actions + [action]
            newCost = cost + stepCost
            f = newCost + heuristic(nextState, problem)
            
            # Use update() in case the same state appears with lower cost
            pq.update((nextState, newActions, newCost), f)
    
    return []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
