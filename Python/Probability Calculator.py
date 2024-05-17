import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = Hat()
        hat_copy.contents = hat.contents.copy()  # Create a copy of the hat for each experiment
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls match the expected balls
        drawn_count = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        success = all(drawn_count.get(color, 0) >= expected_count for color, expected_count in expected_balls.items())
        
        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments
 
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                expected_balls={"red":2,"green":1},
                num_balls_drawn=5,
                num_experiments=2000)
print("Probability:", probability)              