# copyright minzhou@bu.edu


def feet_to_meter(feet):
    return feet * 0.305


feet = float(input('Enter a value for feet: '))

print('%.1f feet is %.4f meters' %(feet, feet_to_meter(feet)))