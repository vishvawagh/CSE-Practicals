# #Four queen problem 
def is_attacking(r1, c1, r2, c2):
    return r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2)

def find_solution(r):
    for c in range(4):
        for queen in range(r):
            if is_attacking(r, c, queen, board[queen]):
                break
        else:
            board[r] = c
            if r == 3:
                print_board()
            else:
                find_solution(r + 1)

def print_board():
    for r in range(4):
        for c in range(4):
            if board[r] == c:
                print("Q ", end="")
            else:
                print("* ", end="")
        print()
    print()

board = [-1] * 4
find_solution(0)
# #Graph colouring 
# def add_edge(graph, edge1, edge2):
#     graph[edge1][edge2] = 1
#     graph[edge2][edge1] = 1

# def safe_to_assign(i, j, graph, v, color):
#     for k in range(v):
#         if graph[i][k] == 1 and color[k] == j:
#             return False
#     return True

# def function(graph, m, v, i, color):
#     if i == v:
#         return True
#     for j in range(m):
#         if safe_to_assign(i, j, graph, v, color):
#             color[i] = j
#             if function(graph, m, v, i + 1, color):
#                 return True
#             color[i] = -1
#     return False

# def graph_coloring(graph, m, v):
#     color = [-1] * v
#     i = 0
#     return function(graph, m, v, i, color)

# def main():
#     m = 3  # no. of colors
#     v = 5  # no. of vertices
#     graph = [[0] * v for _ in range(v)]

#     add_edge(graph, 0, 1)
#     add_edge(graph, 0, 2)
#     add_edge(graph, 0, 3)
#     add_edge(graph, 2, 4)
#     add_edge(graph, 2, 3)
#     add_edge(graph, 3, 4)

#     result = graph_coloring(graph, m, v)
#     if result:
#         print("Graph can be colored with", m, "colors")
#     else:
#         print("Graph cannot be colored with", m, "colors")

# if __name__ == "__main__":
#     main()
