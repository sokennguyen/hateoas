from faker import Faker
import csv


fake = Faker()


def generate_movie():
    return [fake.first_name(), fake.last_name(), fake.phone_number(), fake.ascii_email()]


with open('contact_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First', 'Last', 'Phone', 'Email'])
    for n in range(1, 100):
        writer.writerow(generate_movie())
