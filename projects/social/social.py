from random import randint
from collections import deque
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
        #  loop by given number and create a user name with each iteration
        for i in range(num_users):
            self.add_user(f"User: {i}")

        # Create friendships
        # total number of friendships for the graph
        total = num_users * avg_friendships

        #loop creating friendship edges using random
        added = 0
        while added < total:
            id1 = randint(1, self.last_id)
            id2 = randint(1, self.last_id)
            #check to see if numbers match and that the friend is not already assigned
            if id1 != id2 and id2 not in self.friendships[id1]:
                self.add_friendship(id1, id2)
                # increment to get closer to the total
                added += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        #import queue from collections
        path_queue = deque()
        #add the starting point for the traversal to the queue
        path_queue.append([user_id])
        #while queue is not empty traverse friends.
        while len(path_queue) > 0:
            #get the first path out of the queue
            path = path_queue.popleft()
            # grab the last friend in the path
            friend_id = path[-1]
            #check to see if that friend has been visited
            if friend_id in visited:
                continue
            #if not visited set the path to path to its value
            visited[friend_id] = path

            # Enqueue friends
            for id in self.friendships[friend_id]:
                new_path = path.copy()
                new_path.append(id)
                path_queue.append(new_path)

        friend_coverage = (len(visited) - 1) / (len(self.users) - 1)
        print(f"Percentage of users that are in extended network: {friend_coverage * 100: 0.1f}%")

        # Figure average of path lengths to get average degrees of separation (subtract one to not count user)
        total_length = 0
        for path in visited.values():
            total_length += len(path) - 1

        if len(visited) > 1:
            avg_separation = total_length / (len(visited) - 1)
            print(f"Average degree of separation: {avg_separation}")
        else:
            print("No friends")

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
