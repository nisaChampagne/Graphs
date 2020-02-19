from random import *

from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # for user in num_users:
        for i in range(num_users):
            #add user  by last_id
            self.add_user(self.last_id)

        # Create friendships
        # create list with all possible friendships
        friend_combinations = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1): # larger than user id
                friend_combinations.append((user_id, friend_id)) # tuple

        # shuffle list
        shuffle(friend_combinations) # uses fisher-yates algorithm!
        # print('-----')
        # print(friend_combinations)
        # print('-----')
        
        # grab first n  friendship pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2 ):
            friendship = friend_combinations[i]
            self.add_friendship(friendship[0], friendship[1])
            # print('-----')
            # print(friend_combinations)
            # print('-----')

        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # n = total_friendships // 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        ## every means traversal BFS
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        #create a queue
        queue = Queue()
        # look for path so enqueue the starting point in a list
        queue.enqueue([user_id])
        #while the queue is not empty
        while queue.size() > 0:
            #dequeue the path
            path = queue.dequeue()
            #find the last vertex in the path
            vertex = path[-1]
            #if we have not visited this vertex:
            if vertex not in visited:
                # do something with that vertex
                # add it to visited

                #if visited was a set(), this would be 
                # visited.add(vertex)
                ### but visited is a dictionary so this is it:
                visited[vertex] = path
                # make a copy of path and enqueue for each vertex
                for friend in self.friendships[vertex]:
                    new_path = path[:]
                    new_path.append(friend)
                    queue.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
