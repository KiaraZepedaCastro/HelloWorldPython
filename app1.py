import utils
from utils import kg_to_lbs

print(kg_to_lbs(100))

print(utils.kg_to_lbs(70))


from utils import find_max

numbers = [10, 7, 14, 500, 1000000]
maximum = find_max(numbers)
print(maximum)

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping
calc_shipping()

from ecommerce import shipping
shipping.calc_shipping()