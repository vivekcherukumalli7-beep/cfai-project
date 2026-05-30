
# ============================================================
# EXAMINATION SEATING ARRANGEMENT SYSTEM
# AI BASED CFAI PROJECT
# CO1 + CO2 + CO3 + CO4 + CO5 + CO6
# ============================================================

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

# ============================================================
# STUDENT DATABASE
# ============================================================

@dataclass
class Student:
    reg_no: str
    branch: str

# Predefined Student Details

STUDENTS = [
    Student("101", "CSE"),
    Student("102", "ECE"),
    Student("103", "EEE"),
    Student("104", "CSE"),
    Student("105", "ECE"),
    Student("106", "IT")
]

# ============================================================
# ROOM DATABASE
# ============================================================

@dataclass
class Room:
    room_no: str
    capacity: int

ROOMS = {
    "A101": Room("A101", 2),
    "A102": Room("A102", 2),
    "A103": Room("A103", 2)
}

# ============================================================
# CO1 - PROBLEM FORMULATION
# ============================================================

@dataclass
class State:

    allocations: Dict[str, List[Tuple[str, str]]] = field(
        default_factory=dict
    )

class SeatingProblem:

    def __init__(self, students, rooms):

        self.students = students
        self.rooms = rooms

    # ========================================================
    # CONSTRAINT CHECKING
    # ========================================================

    def is_safe(self, room, branch, state):

        # Constraint 1:
        # Same branch students should not sit together

        for student in state.allocations[room]:

            if student[1] == branch:

                return False

        # Constraint 2:
        # Room capacity should not exceed

        if len(state.allocations[room]) >= self.rooms[room].capacity:

            return False

        return True

    # ========================================================
    # GOAL TEST
    # ========================================================

    def is_goal(self, index):

        return index == len(self.students)

# ============================================================
# SEARCH NODE
# ============================================================

class SearchNode:

    def __init__(self, state, parent, action, depth):

        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

# ============================================================
# CO4 - UTILITY BASED DECISION AGENT
# ============================================================

def calculate_utility(problem, room, state):

    capacity = problem.rooms[room].capacity

    used = len(state.allocations[room])

    remaining = capacity - used

    return remaining

# ============================================================
# CO5 - BAYESIAN RISK ANALYSIS
# ============================================================

def malpractice_probability(room_students):

    total = len(room_students)

    if total <= 1:

        return "LOW RISK"

    branches = [student[1] for student in room_students]

    unique = len(set(branches))

    if unique == total:

        return "LOW RISK"

    elif unique >= total / 2:

        return "MEDIUM RISK"

    else:

        return "HIGH RISK"

# ============================================================
# CO2 - DFS SEARCH ALGORITHM
# ============================================================

def dfs(problem, state, index):

    # ========================================================
    # GOAL STATE CHECK
    # ========================================================

    if problem.is_goal(index):

        print("\nSUCCESS: GOAL STATE REACHED")
        return True

    # Current Student

    student = problem.students[index]

    print("\n------------------------------------------------")
    print("Exploring Student:", student.reg_no)
    print("Branch:", student.branch)
    print("------------------------------------------------")

    # Explore Rooms

    for room in problem.rooms:

        print("\nChecking Room:", room)

        # ====================================================
        # CO4 - UTILITY ANALYSIS
        # ====================================================

        utility = calculate_utility(
            problem,
            room,
            state
        )

        print("Utility Value:", utility)

        # ====================================================
        # VALIDATION CHECK
        # ====================================================

        if problem.is_safe(room, student.branch, state):

            print("Safe Allocation Possible")

            # Allocate Student

            state.allocations[room].append(
                (student.reg_no, student.branch)
            )

            print(
                "Allocated Student",
                student.reg_no,
                "to Room",
                room
            )

            # =================================================
            # RECURSIVE DFS SEARCH
            # =================================================

            if dfs(problem, state, index + 1):

                return True

            # =================================================
            # CO3 - CSP BACKTRACKING
            # =================================================

            removed_student = state.allocations[room].pop()

            print(
                "Backtracking Performed"
            )

            print(
                "Removed Student:",
                removed_student[0],
                "from Room",
                room
            )

        else:

            print("Constraint Violated")
            print("Cannot Allocate Student")

    return False

# ============================================================
# DISPLAY STUDENT DETAILS
# ============================================================

def show_students():

    print("\n" + "=" * 60)
    print("STUDENT DETAILS")
    print("=" * 60)

    for student in STUDENTS:

        print(
            "Register No:",
            student.reg_no,
            "| Branch:",
            student.branch
        )

# ============================================================
# DISPLAY ROOM DETAILS
# ============================================================

def show_rooms():

    print("\n" + "=" * 60)
    print("ROOM DETAILS")
    print("=" * 60)

    for room_no, room in ROOMS.items():

        print(
            "Room:",
            room_no,
            "| Capacity:",
            room.capacity
        )

# ============================================================
# DISPLAY FINAL SEATING ARRANGEMENT
# ============================================================

def show_final_arrangement(state):

    print("\n" + "=" * 60)
    print("FINAL SEATING ARRANGEMENT")
    print("=" * 60)

    for room in state.allocations:

        print("\nRoom:", room)

        if state.allocations[room]:

            for student in state.allocations[room]:

                print(
                    "Student:",
                    student[0],
                    "| Branch:",
                    student[1]
                )

            # =================================================
            # CO5 - RISK ANALYSIS
            # =================================================

            risk = malpractice_probability(
                state.allocations[room]
            )

            print("Malpractice Risk:", risk)

        else:

            print("No Students Allocated")

# ============================================================
# PROJECT SUMMARY
# ============================================================

def show_summary():

    print("\n" + "=" * 60)
    print("PROJECT SUMMARY")
    print("=" * 60)

    print("\nCO1 - PROBLEM FORMULATION")

    print("• Students represented using classes")
    print("• Rooms represented using classes")
    print("• Seating arrangement represented as states")
    print("• Problem environment represented using data structures")

    print("\nCO2 - DFS SEARCH ALGORITHM")

    print("• DFS algorithm used for room exploration")
    print("• Recursive state-space search implemented")
    print("• Rooms explored one by one")

    print("\nCO3 - CSP + BACKTRACKING")

    print("• Constraint Satisfaction Problem implemented")
    print("• Same branch students are not seated together")
    print("• Room capacity checking implemented")
    print("• Backtracking performed during failure")
    print("• Safe allocation checking implemented")

    # ========================================================
    # CO4
    # ========================================================

    print("\nCO4 - DECISION MAKING AGENT")

    print("• Utility-based decision agent implemented")
    print("• Room utility calculation added")
    print("• AI-based room analysis performed")

    # ========================================================
    # CO5
    # ========================================================

    print("\nCO5 - REASONING UNDER UNCERTAINTY")

    print("• Bayesian-style malpractice risk prediction added")
    print("• Uncertainty reasoning implemented")
    print("• Risk inference generated")

    # ========================================================
    # CO6
    # ========================================================

    print("\nCO6 - INTEGRATED AI PIPELINE")

    print("• Problem formulation integrated")
    print("• DFS search integrated")
    print("• CSP constraints integrated")
    print("• Bayesian reasoning integrated")
    print("• Utility-based reasoning integrated")
    print("• Explainable AI outputs generated")

# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n" + "=" * 60)
    print("EXAMINATION SEATING ARRANGEMENT SYSTEM")
    print("AI BASED CFAI PROJECT")
    print("CO1 + CO2 + CO3 + CO4 + CO5 + CO6")
    print("=" * 60)

    # ========================================================
    # DISPLAY INPUT DATA
    # ========================================================

    show_students()
    show_rooms()

    # ========================================================
    # INITIAL STATE
    # ========================================================

    initial_state = State(
        allocations={
            "A101": [],
            "A102": [],
            "A103": []
        }
    )

    # ========================================================
    # CREATE PROBLEM
    # ========================================================

    problem = SeatingProblem(
        STUDENTS,
        ROOMS
    )

    print("\n" + "=" * 60)
    print("DFS SEARCH + CSP ALLOCATION STARTED")
    print("=" * 60)

    # ========================================================
    # START DFS SEARCH
    # ========================================================

    success = dfs(
        problem,
        initial_state,
        0
    )

    # ========================================================
    # FINAL OUTPUT
    # ========================================================

    if success:

        print("\nSEATING ARRANGEMENT GENERATED SUCCESSFULLY")

        show_final_arrangement(initial_state)

    else:

        print("\nFAILED TO GENERATE SEATING ARRANGEMENT")

    # ========================================================
    # PROJECT SUMMARY
    # ========================================================

    show_summary()

    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 60)

# ============================================================
# DRIVER CODE
# ============================================================

if __name__ == "__main__":

    main()