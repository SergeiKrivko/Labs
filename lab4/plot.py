from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
import angem as ag

POINT_SIZE = 4
LINE_WIDTH = 2
POINT_WIDTH = 3
OBJECT_COLOR = Qt.black
DRAWING_COLOR = Qt.red
SELECT_COLOR = Qt.blue


class Plot(QWidget):
    add_point = pyqtSignal(ag.Point)
    select_object = pyqtSignal(int)

    def __init__(self, objects):
        super(Plot, self).__init__()

        self.painter = QPainter(self)

        self.objects = objects
        self.selected_object = -1
        self.temp_objects = tuple()
        self.obj_func = None
        self.on_mouse_left = None
        self.on_mouse_move = None

        self.x = 0
        self.y = 0
        self.mouse_pos = None
        self.moving_camera = False
        self.axis1 = ag.Line(ag.Point(0, 0), ag.Vector(1, 0))
        self.axis2 = ag.Line(ag.Point(0, 0), ag.Vector(0, 1))

        self.move_camera(QPoint(self.width() // 2, self.height() // 2))

        self.drawing_mode = False

    def paintEvent(self, a0):
        self.painter.begin(self)
        self.draw(self.axis1)
        self.draw(self.axis2)
        for obj in self.objects:
            self.draw(obj)
        for obj in self.temp_objects:
            self.draw(obj)
        if self.selected_object != -1:
            self.draw(self.objects[self.selected_object], color=SELECT_COLOR)
        self.painter.end()

    def update(self, *objects) -> None:
        self.temp_objects = objects
        super(Plot, self).update()

    def draw(self, obj, color=None):
        if isinstance(obj, ag.Point):
            if color:
                self.draw_point(obj, color)
            else:
                self.draw_point(obj)
        elif isinstance(obj, ag.Segment):
            self.draw_segment(obj)
        elif isinstance(obj, ag.Line):
            self.draw_line(obj)
        elif isinstance(obj, ag.Circle):
            self.draw_circle(obj)

    def draw_point(self, point: ag.Point, color=None):
        self.set_pen(color if color is not None else point.color, POINT_WIDTH)
        self.painter.drawEllipse(self.x_to_screen(point.x) - POINT_SIZE, self.y_to_screen(point.y) - POINT_SIZE,
                                 2 * POINT_SIZE, 2 * POINT_SIZE)

    def draw_segment(self, segment: ag.Segment, color=None):
        self.set_pen(color if color is not None else segment.color, LINE_WIDTH)
        self.painter.drawLine(self.x_to_screen(segment.p1.x), self.y_to_screen(segment.p1.y),
                              self.x_to_screen(segment.p2.x), self.y_to_screen(segment.p2.y))

    def draw_line(self, line: ag.Line, color=None):
        self.set_pen(color if color is not None else line.color, LINE_WIDTH)
        if line.vector.y:
            p1 = ag.Point(line.get_x(self.y_to_ag(0)), self.y_to_ag(0))
            p2 = ag.Point(line.get_x(self.y_to_ag(self.height())), self.y_to_ag(self.height()))
        else:
            p1 = ag.Point(self.x_to_ag(0), line.point.y)
            p2 = ag.Point(self.x_to_ag(self.width()), line.point.y)
        self.painter.drawLine(self.x_to_screen(p1.x), self.y_to_screen(p1.y),
                              self.x_to_screen(p2.x), self.y_to_screen(p2.y))

    def draw_circle(self, circle: ag.Circle, color=None):
        self.set_pen(color if color is not None else circle.color, LINE_WIDTH)
        self.painter.drawEllipse(int(self.x_to_screen(circle.center.x) - circle.radius),
                                 int(self.y_to_screen(circle.center.y) - circle.radius),
                                 2 * int(circle.radius), 2 * int(circle.radius))

    def mousePressEvent(self, a0) -> None:
        if a0.button() == 1:
            if self.drawing_mode:
                self.add_point.emit(ag.Point(self.x_to_ag(a0.x()), self.y_to_ag(a0.y()), color=OBJECT_COLOR))
            else:
                for index, obj in enumerate(self.objects):
                    if isinstance(obj, ag.Point) and abs(ag.Vector(
                            ag.Point(self.x_to_ag(a0.x()), self.y_to_ag(a0.y())), obj)) < 6:
                        self.select_object.emit(index)
                        break
        elif a0.button() == 2:
            self.moving_camera = True
            self.mouse_pos = a0.pos()

    def mouseReleaseEvent(self, a0) -> None:
        if a0.button() == 2:
            self.moving_camera = False

    def mouseMoveEvent(self, a0) -> None:
        if self.moving_camera:
            self.move_camera(a0.pos() - self.mouse_pos)
            self.mouse_pos = a0.pos()
        if self.drawing_mode:
            point = ag.Point(self.x_to_ag(a0.x()), self.y_to_ag(a0.y()), color=DRAWING_COLOR)
            self.update(point)

    def set_pen(self, color=Qt.red, width=1):
        pen = QPen()
        pen.setColor(color)
        pen.setWidth(width)
        self.painter.setPen(pen)

    def move_camera(self, a0):
        self.x += a0.x()
        self.y += a0.y()
        self.update()

    def x_to_ag(self, x):
        return x - self.x

    def y_to_ag(self, y):
        return -y + self.y

    def x_to_screen(self, x):
        return int(x + self.x)

    def y_to_screen(self, y):
        return int(-y + self.y)

    def set_drawing_mode(self, mode):
        self.drawing_mode = mode
        if self.drawing_mode:
            self.setMouseTracking(True)
        else:
            self.setMouseTracking(False)
            self.update()

    def end_creating_object(self):
        self.setMouseTracking(False)
        self.on_mouse_left = None
        self.on_mouse_move = None
        self.update()

    def select_point(self, objects=tuple(), object_func=None, end_func=None):
        def mouse_move(pos: QPoint):
            point = ag.Point(self.x_to_ag(pos.x()), self.y_to_ag(pos.y()))
            if object_func:
                self.update(*objects, *object_func(pos), point)
            else:
                self.update(*objects, point)

        self.on_mouse_left = end_func
        self.on_mouse_move = mouse_move

    def create_point(self, step=1, **kwargs):
        if step == 1:
            self.select_point(end_func=lambda pos: self.create_point(2, pos=pos))
        elif step == 2:
            self.add_point.emit(ag.Point(self.x_to_ag(kwargs['pos'].x()), self.y_to_ag(kwargs['pos'].y())))
            self.end_creating_object()

