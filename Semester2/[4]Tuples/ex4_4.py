def main():
    studentList = {'Smith': 58, 'Jones': 36, 'Peters': 78, 'Adams': 44}
    # studentList= {'Smith':58, 'Jones':86, 'peters':78, 'Adams':44}
    result = highestMark(studentList)
    print('Student with highest mark={0}'.format(result))


def highestMark(studentL):
    #name = max(studentL)
    #return name

    # OR

    highest = 0
    name = ''

    for key, value in studentL.items():
        if value > highest:
            highest = value
            name = key
    return name






main()
