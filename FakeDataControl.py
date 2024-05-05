from faker import Faker
import product
import uuid
import datetime
import random
fake = Faker()

"""
customer
id_customer
id_document
des_name
des_address
des_genero
num_phone
des_email
dat_Birthday
dat_register
"""

for _ in range(1, 10):
    id_customer = uuid.uuid4()
    id_document = fake.ssn()
    nam_name = fake.name()
    des_address = fake.address()
    des_genero = fake.word(ext_word_list = ["M","F"])
    num_phone = fake.phone_number()
    des_email = fake.email()
    dat_Birthday = fake.date_of_birth(minimum_age= 18, maximum_age=75)
    start_date = datetime.datetime(1990,1,1)
    end_date = datetime.datetime(2024,1,1)
    dat_register= fake.date_between(start_date = start_date,end_date= end_date)

    customer =  {"id_customer": id_customer,
               "id_document" : id_document,
               "nam_name" : nam_name,
               "des_address" : num_phone,
               "des_genero": des_genero,
               "num_phone":num_phone,
               "des_email" : des_email,
               "dat_Birthday" : dat_Birthday,
               "dat_register":dat_register
               }
    print(customer)

    """ id_filial
        num_adress
        nam_maneger
        dat_openday
        num_callphone
        des_email
        """

for id_filial in range(1, 10):
    nome = fake.name()
    des_address = fake.address()
    num_phone = fake.phone_number()
    des_email = fake.company_email()
    dat_open = fake.date_of_birth (minimum_age=10, maximum_age=20)

    filial =  {"id_filial": id_filial,
               "des_address" : des_address,
               "nam_manager" : nome,
               "num_phone" : num_phone,
               "des_email" : des_email,
               "dat_openday":dat_open
               }

    print(filial)



"""
#sales
id_sale
idt_customer
idt_document
dat_transaction
des_payment_method
num_CreditCard
num_PaymentAmount
"""

for _ in range(1, 10):

    for id_invoice in range(1, 10):
        nam_product = product.product_generator()
        num_quantity = random.randint(1, 1000)
        num_value = random.randint(1, 1000) / 6

    invoice = {"id_invoice": id_invoice,
               "nam_product": nam_product,
               "num_quantity": num_quantity,
               "num_value": round(num_value, 2),
               }

    print(invoice)

    id_sale = uuid.uuid4()
    idt_invoice = id_invoice
    id_customer = id_customer
    id_document = id_document
    start_date = datetime.datetime(1990,1,1)
    end_date = datetime.datetime(2024,1,1)
    dat_transaction = fake.date_between(start_date = start_date, end_date= end_date)
    des_paymentMethod = fake.word(ext_word_list=["CreditCard","DebitCard","Cash"])
    num_CreditNumber = fake.credit_card_number()
    num_PaymentAmount = 10000

    
    sales =  {  "id_sale": id_sale,
                "id_invoice" : id_invoice,
                "id_filial" : id_filial,
                "id_customer" : id_customer,
                "id_document" : id_document,
                "dat_transaction" : dat_transaction,
                "des_paymentMethod" : des_paymentMethod,
                "num_CreditNumber":num_CreditNumber,
                "num_PaymentAmount": num_PaymentAmount

               }
    print(sales)
    
"""
# invoice
id_invoice
id_sale
nam_product
num_quantity
num_value
"""