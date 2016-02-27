"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        :param col:
        :param row:
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        :param col:
        :param row:
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        :param entity_type:
        """
        width = self.get_grid_width()
        height = self.get_grid_height()

        visited = poc_grid.Grid(height, width)

        init = width * height
        distance_field = [[init for _ in xrange(width)] for _ in xrange(height)]

        if entity_type == HUMAN:
            aux = list(self._human_list)
        else:
            aux = list(self._zombie_list)

        boundary = poc_queue.Queue()
        for cell in aux:
            boundary.enqueue(cell)
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0

        # Breadth-First Search
        while len(boundary) != 0:
            cell = boundary.dequeue()
            for neighbor_cell in self.four_neighbors(cell[0], cell[1]):
                # check if neighbor_cell has not been visited and is passable
                if visited.is_empty(neighbor_cell[0], neighbor_cell[1]) and \
                        self.is_empty(neighbor_cell[0], neighbor_cell[1]):
                    visited.set_full(neighbor_cell[0], neighbor_cell[1])
                    # updates the best distance with the lower value
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = \
                        min(distance_field[neighbor_cell[0]][neighbor_cell[1]],
                            distance_field[cell[0]][cell[1]] + 1)
                    boundary.enqueue(neighbor_cell)

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        :param zombie_distance_field:
        """
        for human in list(self._human_list):
            best_neighbors = [human]

            neighbors = self.eight_neighbors(human[0], human[1])
            for neighbor in neighbors:
                # excludes neighbors not empty
                if not poc_grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                    continue

                aux = (best_neighbors[0][0], best_neighbors[0][1])
                best_neighbor_value = zombie_distance_field[aux[0]][aux[1]]
                neighbor_value = zombie_distance_field[neighbor[0]][neighbor[1]]
                if neighbor_value > best_neighbor_value:
                    best_neighbors = [neighbor]
                elif neighbor_value == best_neighbor_value:
                    best_neighbors.append(neighbor)

            random_best_neighbor = random.choice(best_neighbors)
            self._human_list.remove(human)
            self.add_human(random_best_neighbor[0], random_best_neighbor[1])

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        :param human_distance_field:
        """
        for zombie in list(self._zombie_list):
            best_neighbors = [zombie]

            neighbors = self.four_neighbors(zombie[0], zombie[1])
            for neighbor in neighbors:
                # excludes neighbors not empty
                if not poc_grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                    continue

                aux = (best_neighbors[0][0], best_neighbors[0][1])
                best_neighbor_value = human_distance_field[aux[0]][aux[1]]
                neighbor_value = human_distance_field[neighbor[0]][neighbor[1]]
                if neighbor_value < best_neighbor_value:
                    best_neighbors = [neighbor]
                elif neighbor_value == best_neighbor_value:
                    best_neighbors.append(neighbor)

            random_best_neighbor = random.choice(best_neighbors)
            self._zombie_list.remove(zombie)
            self.add_zombie(random_best_neighbor[0], random_best_neighbor[1])

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
