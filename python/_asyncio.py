# Parallelism consists of performing multiple operations at the same time.
# Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores).
# Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

# Concurrency is a slightly broader term than parallelism.
# It suggests that multiple tasks have the ability to run in an overlapping manner.
# (There’s a saying that concurrency does not imply parallelism.)

# Threading is a concurrent execution model whereby multiple threads take turns executing tasks.
# One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL

# To recap the above,
# concurrency encompasses both multiprocessing (ideal for CPU-bound tasks)
# and threading (suited for IO-bound tasks).
# Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency.
# The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.

# Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.


# Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.
# Assumptions:

#     24 opponents
#     Judit makes each chess move in 5 seconds
#     Opponents each take 55 seconds to make a move
#     Games average 30 pair-moves (60 moves total)

# Synchronous version: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.
# Asynchronous version: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour. (Source)
