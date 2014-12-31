# Use "if" and "else if" to handle any situation.
# Put it all together to defeat enemies and pick up coins!
# Make sure you bought great armor from the item shop! 400 health recommended.

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()

    if flag:
        # What happens when I find a flag?
        self.pickUpFlag(flag)
    elif enemy:
        # What happens when I find an enemy?
        distance = self.distanceTo(enemy)
        if distance > 10:
            self.shield()
        elif self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
            self.attack(enemy)
    elif item:
        # What happens when I find an item?
        pos = item.pos
        x = pos.x
        y = pos.y
        self.moveXY(x, y)