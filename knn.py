"""sdonoghue 2025-09-25
"""
import statistics 

def e_dist_2(t1,t2):
    '''calcualte euclidian distance between 2 tuples, using first and second elements'''
    # sqrt[delta-x squared + delta-y squared ]
    eucludian_distance = ((t1[0] - t2[0])*(t1[0] -t2[0]) + (t1[1] - t2[1])*(t1[1] -t2[1]))**0.5
    return eucludian_distance

def e_dist_3(t1,t2):
    '''calcualte euclidian distance between 2 tuples, using first and second elements'''
    # sqrt[delta-x squared + delta-y squared + delta-z squared ]
    eucludian_distance = ((t1[0] - t2[0])*(t1[0] -t2[0]) + (t1[1] - t2[1])*(t1[1] -t2[1])+ (t1[2] - t2[2])*(t1[2] -t2[2]))**0.5
    return eucludian_distance
'''
def get_distances(training_set,sample):
    distances = []
    for train in training_set:
        d = e_dist_3(train,sample)
        distances.append([train,d])
    return distances
'''

def get_distances(training_set,sample):
    distances = []
    for train in training_set:
        d = e_dist_2(train,sample)
        distances.append([train,d])
    return distances

def sortkey(tuple):
    return tuple[1]

def clasify_flower(training_set,sample, k):
    '''Implmenting closest k classification algorithm. 
    
    selects the closet k items in the training set to the sample (by [0]&[1] only ), then calculates the modal colour [3] associated with them '''
    training_distances = get_distances(training_set,sample)
    sorted_t_dist = sorted(training_distances,key= lambda x: x[1])
    closest_k =  [d[0] for d in sorted_t_dist[0:k]]
    closest_k_colours = [k[3]for k in closest_k]
    modal_color =  statistics.mode(closest_k_colours)
    return modal_color



observations = [	(3, 3, 2, 'red'), 
(2, 7, 4, 'red'), 
(3, 4, 3, 'red'), 
(2, 8, 5, 'red'), 
(2, 5, 2, 'red'), 	
(3, 10, 5, 'red'), 
(1, 3, 2, 'red'), 
(2, 10, 2, 'red'), 
(3, 1, 4, 'red'), 
(5, 5, 1, 'red'), 
(6, 5, 18, 'yellow'), 
(9, 5, 14, 'yellow'), 
(6, 10, 18, 'yellow'), 
(7, 8, 8, 'yellow'), 
(5, 5, 5, 'yellow'), 
(4, 5, 13, 'yellow'), 
(6, 10, 8, 'yellow'), 
(10, 9, 4, 'yellow'), 
(6, 9, 4, 'yellow'), 
(8, 5, 4, 'yellow'), 
(5, 13, 9, 'blue'), 
(11, 12, 5, 'blue'), 
(14, 11, 7, 'blue'), 
(17, 12, 7, 'blue'), 
(5, 12, 7, 'blue'), 
(8, 11, 5, 'blue'), 
(8, 9, 5, 'blue'), 
(11, 9, 8, 'blue'), 
(18, 14, 6, 'blue'), 
(15, 12, 8, 'blue')]

sample = (3, 7, 2, 'unknown')

clasification =  clasify_flower(observations,(7,3,7,'unk'),7)
print(clasification)
