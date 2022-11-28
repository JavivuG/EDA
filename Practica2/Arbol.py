import math


class Point:
    """A point located at (x,y) in 2D space.

    Each Point object may be associated with a payload object.

    """

    def __init__(self, x, y, usr=None):
        self.x, self.y = x, y
        self.usr = usr

    def distancia_a(self, other):
        other_x, other_y = other.x, other.y
        return math.sqrt((self.x - other_x)**2+(self.y - other_y)**2)

class Rect:
    """A rectangle centred at (cx, cy) with width w and height h."""

    def __init__(self, cx, cy, w, h):
        self.cx, self.cy = cx, cy
        self.w, self.h = w, h
        self.oeste, self.este = cx - w/2, cx + w/2
        self.norte, self.sur = cy - h/2, cy + h/2

    def contains(self, point):
        """Is point (a Point object or (x,y) tuple) inside this Rect?"""

        point_x, point_y = point.x, point.y

        return (point_x >= self.oeste and point_x <  self.este and point_y >= self.norte and point_y < self.sur)

    def intersects(self, other):
        """Does Rect object other interesect this Rect?"""
        return not (other.oeste > self.este or other.este < self.oeste or other.norte > self.sur or  other.sur < self.norte)

class QuadTree:
    """A class implementing a quadtree."""

    def __init__(self, boundary, max_points=4, depth=0):
        """Initialize this node of the quadtree.

        boundary is a Rect object defining the region from which points are
        placed into this node; max_points is the maximum number of points the
        node can hold before it must dividir (branch into four more nodes);
        depth keeps track of how deep into the quadtree this node lies.

        """

        self.boundary = boundary
        self.max_points = max_points
        self.points = []
        self.depth = depth
        # A flag to indicate whether this node has dividird (branched) or not.
        self.dividido = False

    def dividir(self):
        """dividir (branch) this node by spawning four children nodes."""

        cx, cy = self.boundary.cx, self.boundary.cy
        w, h = self.boundary.w / 2, self.boundary.h / 2
        # The boundaries of the four children nodes are "northwest",
        # "northeast", "southeast" and "southwest" quadrants within the
        # boundary of the current node.
        self.noroeste = QuadTree(Rect(cx - w/2, cy - h/2, w, h), self.max_points, self.depth + 1)
        self.noreste = QuadTree(Rect(cx + w/2, cy - h/2, w, h), self.max_points, self.depth + 1)
        self.sureste = QuadTree(Rect(cx + w/2, cy + h/2, w, h), self.max_points, self.depth + 1)
        self.suroeste = QuadTree(Rect(cx - w/2, cy + h/2, w, h), self.max_points, self.depth + 1)
        self.dividido = True

    def insertar(self, point):
        """Try to insert Point point into this QuadTree."""

        if not self.boundary.contains(point):
            # The point does not lie inside boundary: bail.
            return False
        if len(self.points) < self.max_points:
            # There's room for our point without dividing the QuadTree.
            self.points.append(point)
            return True

        # No room: dividir if necessary, then try the sub-quads.
        if not self.dividido:
            self.dividir()

        return (self.noreste.insertar(point) or self.noroeste.insertar(point) or self.sureste.insertar(point) or self.suroeste.insertar(point))

    def query(self, boundary, found_points):
        """Find the points in the quadtree that lie within boundary."""

        if not self.boundary.intersects(boundary):
            # If the domain of this node does not intersect the search
            # region, we don't need to look in it for points.
            return False

        # Search this node's points to see if they lie within boundary ...
        for point in self.points:
            if boundary.contains(point):
                found_points.append(point)
        # ... and if this node has children, search them too.
        if self.dividido:
            self.noroeste.query(boundary, found_points)
            self.noreste.query(boundary, found_points)
            self.sureste.query(boundary, found_points)
            self.suroeste.query(boundary, found_points)
        return found_points


    def query_circle(self, boundary, centro1, centro2, radius, found_points):
        """Find the points in the quadtree that lie within radius of centre.

        boundary is a Rect object (a square) that bounds the search circle.
        There is no need to call this method directly: use query_radius.

        """

        if not self.boundary.intersects(boundary):
            # If the domain of this node does not intersect the search
            # region, we don't need to look in it for points.
            return False

        # Search this node's points to see if they lie within boundary
        # and also lie within a circle of given radius around the centre point.
        for point in self.points:
            centre=Point(centro1,centro2)
            if (boundary.contains(point) and point.distancia_a(centre) <= radius):
                found_points.append(point.usr)

        # Recurse the search into this node's children.
        if self.dividido:
            self.noroeste.query_circle(boundary, centro1, centro2, radius, found_points)
            self.noreste.query_circle(boundary, centro1,centro2, radius, found_points)
            self.sureste.query_circle(boundary, centro1,centro2, radius, found_points)
            self.suroeste.query_circle(boundary, centro1,centro2, radius, found_points)
        return found_points

    def query_radius(self, centro1, centro2, radius, found_points):
        """Find the points in the quadtree that lie within radius of centre."""

        # First find the square that bounds the search circle as a Rect object.
        boundary = Rect(centro1, centro2, 2*radius, 2*radius)
        return self.query_circle(boundary, centro1,centro2, radius, found_points)


    def __len__(self):
        """Return the number of points in the quadtree."""

        npoints = len(self.points)
        if self.dividido:
            npoints += len(self.noroeste)+len(self.noreste)+len(self.sureste)+len(self.suroeste)
        return npoints