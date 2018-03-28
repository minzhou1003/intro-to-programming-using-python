# copyright minzhou@bu.edu


def tips(sub, rate):
    return (sub * rate * 0.01, sub + sub * rate * 0.01)

[sub, rate] = input('Enter the subtotal and a gratuity rate: ').split(',')
sub = float(sub)
rate = float(rate)
print('The gratuity is %.2f and the total is %.2f' % (tips(sub, rate)[0], tips(sub, rate)[1]))