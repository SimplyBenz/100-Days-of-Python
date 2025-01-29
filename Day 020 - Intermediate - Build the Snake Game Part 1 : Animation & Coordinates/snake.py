import turtle

STARTING_POSITIONS = [(0,0), (-23,0), (-46,0)]
MOVE_DISTANCE = 23
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # Creating snake with 3 segments in center of game
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.new_segment = turtle.Turtle()
            self.new_segment.penup()
            self.new_segment.shape("square")
            self.new_segment.speed("slow")
            self.new_segment.setposition(position)
            self.segments.append(self.new_segment)
    
    def move(self):
        #Make snake move forward
        # for seg_num in range(start = length of list named "segments", stop = 0, step = -1)
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)