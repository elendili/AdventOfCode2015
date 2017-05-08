#!/usr/bin/python -u
import sys, argparse
import re, math
import itertools
from itertools import izip, tee

input = """Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.""".split('\n')

# input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.""".split('\n')

def find_distance(speed, fly_schedule, cutoff_time):
    distance=0
    for moment in fly_schedule:
        if moment>cutoff_time: break
        distance+=speed
    return distance

# cutoff_time = 1000
cutoff_time = 2503

class ReindeerMetric:
    def __init__(self, name):
        self.name=name
    def find_fly_schedule(self,cutoff_time):
        fly_start=1
        fly_finish=self.fly_duration+1
        fly_schedule=[]
        while(fly_finish <= cutoff_time + self.fly_duration):
            fly_schedule += range(fly_start,fly_finish)
            fly_start = fly_finish  + self.rest_duration
            fly_finish = fly_start + self.fly_duration
        return fly_schedule

    name=0
    speed=0
    fly_duration=0
    rest_duration=0
    schedule=[]
    lead_points=0
    total_distance=0
    current_distance=0

ReindeerMetrics={}
for index,line in enumerate(input):
    # if index>8:break
    name, speed, fly_duration, rest_duration = [z for z in re.findall('[A-Z]\w+|\d+', line)]
    reindeer =  ReindeerMetric(name)
    ReindeerMetrics[name]=reindeer
    reindeer.speed = int(speed)
    reindeer.fly_duration = int(fly_duration)
    reindeer.rest_duration = int(rest_duration)
    reindeer.schedule = reindeer.find_fly_schedule(cutoff_time)

print '=== First part ==='
for name, reindeer in ReindeerMetrics.items():
    reindeer.total_distance = find_distance(reindeer.speed, reindeer.schedule, cutoff_time)
    print name, '=', reindeer.total_distance

print(max(x.total_distance for x in ReindeerMetrics.values()))

print '=== Second part ==='
for i in range(1, cutoff_time+1):
    for name, reindeer in ReindeerMetrics.items():
        if i in reindeer.schedule:
            reindeer.current_distance+=reindeer.speed

    reindeer_distances = dict([(x.name, x.current_distance) for x in ReindeerMetrics.values()])
    leader_distance = max(reindeer_distances.values())
    distance_leader_names = [k for k, v in reindeer_distances.items() if v == leader_distance]
    for name in distance_leader_names:
        ReindeerMetrics[name].lead_points+=1
    leader_points = [(x.name, x.lead_points, x.current_distance) for x in ReindeerMetrics.values()]
    print i,'.', distance_leader_names, ':', leader_points
print max([x.lead_points for x in ReindeerMetrics.values()])