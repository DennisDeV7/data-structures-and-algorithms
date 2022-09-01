from data_structures.hashtable import Hashtable


def left_join(hashmap1, hashmap2):
    joint_data = []

    for key, value in hashmap1.items():
        if hashmap2.get(key):
            joint_data.append([key, value, hashmap2[key]])
        else:
            joint_data.append([key, value, "NONE"])

    return joint_data
