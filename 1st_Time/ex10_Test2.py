

# These are the variables
balls = 50
players = 75
missing_balls = players - balls
add = balls + players
traits = "-"

print "\n"
print traits * 100
print "\n"

# These lines test different format integration between strings.
print "\nThere are", balls, "balls and", players, "players.  So", missing_balls, "players don't have a ball."
print "There are %r balls and %r players.  So %r players don't have a ball." % (balls, players, missing_balls)
print "There are %r balls" % (balls), 
print "and %r players." % (players),
print " So %r players don't have a ball.\n" % (missing_balls)

# These lines prints 3 times the same equation coded in a different way.
print "\t", balls, "+", players, "=" ,balls + players
print "\t%r + %r = %r" % (balls, players, add)
print "\t%r + %r = %r" % (balls, players, balls + players)

print "\n"
print traits * 100
print "\n"
