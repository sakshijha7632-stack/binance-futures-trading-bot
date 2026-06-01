from bot.validators import *

print(validate_side("buy"))
print(validate_side("sell"))

print(validate_order_type("market"))

print(validate_quantity("0.001"))