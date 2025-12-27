"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    
    # express_queue : Fast-track queue name (快速通道名單) ticket 1 
    # normal_queue : normal queue name (普通名單) ticket 0
    # ticket_type : type of ticket (票的類型)
    #　person_name : person name (人名)

    goal_queue = None # goal queue (目標列表)

    if ticket_type:
        express_queue.append(person_name)
        goal_queue = express_queue
    else:
        normal_queue.append(person_name)
        goal_queue = normal_queue

    return goal_queue

def find_my_friend(queue, friend_name):
    # queue : queue (列表)
    # frined_name : target (目標)

    return queue.index(friend_name)

def add_me_with_my_friends(queue, index, person_name):
    # queue : queue (隊伍)
    # index : the add person position (人要加入的位置)
    # person_name : person name (人名)
    
    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue, person_name):
    # queue : queue (隊伍)
    # person_name : the person be kicked (要踢的人)

    queue.remove(person_name)

    return queue
    
def how_many_namefellows(queue, person_name):
    # queue : queue (隊伍)
    # person_name : name you should count (要數的人名)
    time = 0 # 出現的次數

    time = queue.count(person_name)

    return time

def remove_the_last_person(queue):
    # queue : queue (隊伍)
    person = queue[-1] # the least one in queue
    
    queue.pop()
    return person
    
def sorted_names(queue):
    # queue : queue (隊伍)

    return sorted(queue)