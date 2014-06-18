class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastes_like(self):

        raise NotImplementedError("Subclasses are responsible for creating this method")

class HotDog(Food):
    def tastes_like(self):
        return "extremely processed meat"
class Hamburger(Food):
    def tastes_like(self):
        return "grilled goodness"
class ChickenPatty(Food):
    def tastes_like(self):
        return "tastes like chicken"

dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Micky Mouse shaped Chicken Tenders', 170))

for course in dinner:
    print "%s is type %s" % (course.name, type(course))
    print "has %s calories" % course.calories
    print "tastes like %s" % course.tastes_like()







#Beef/Turkey BallPark is type <class '__main__.HotDog'>
 # has 230 calories
 # and tastes like Extremely processed meat
#Lowfat Beef Patty is type <class '__main__.Hamburger'>
#  has 260 calories
 # and tastes like grilled goodness
#Micky Mouse shaped Chicken Tenders is type <class '__main__.ChickenPatty'>
 #has 170 calories
 # and tastes like chicken