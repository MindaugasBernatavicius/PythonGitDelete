import logging

logging.basicConfig(
    filename='logs/main.log',
    level=logging.INFO
)


def add(i, j):
  return i + j


def multiply(i, j):
  return i * j


res_add = add(3, 2)
res_multiply = multiply(3, 2)

logging.info('{} : {}'.format('Addition result', res_add))
logging.info('{} : {}'.format('Multiplication result', res_multiply))


print("Helo")
print("Helo")
print("Hello!")