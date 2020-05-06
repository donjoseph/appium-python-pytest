import datetime
import random
import names
from dateutil.relativedelta import relativedelta
from faker import Faker


def createSampleUsersWeb(noOfUsers=3):
    sampleData = []
    locations = ["Chicago", "San Francisco", "Atlanta"]
    location, firstName, lastName, email, password, phoneNumber = \
        "location", "firstName", "lastName", "email", "password", "phoneNumber"
    for i in range(0, noOfUsers):
        singleData = {}
        fake = Faker()
        singleData[firstName] = names.get_first_name()
        singleData[lastName] = names.get_last_name()
        singleData[email] = fake.email()
        singleData[password] = passwordGenerator()
        singleData[phoneNumber] = fake.phone_number()
        singleData[location] = random.choice(locations)
        sampleData.append(singleData)
    return sampleData


def createUsersPost(noOfUsers=3):
    sampleUsers = []
    title, body, userid = "title", "body", "userid"
    for i in range(0, noOfUsers):
        singleUser = {}
        singleUser[title] = names.get_first_name()
        singleUser[body] = names.get_full_name()
        singleUser[userid] = i
        sampleUsers.append(singleUser)
    return sampleUsers


def getFutureDate(days=0, years=0):
    futureDate = datetime.datetime.now() + relativedelta(days=days, years=years)
    return futureDate.strftime("%d/%m/%Y")


def getSampleWifiSettings(noOfSettings=1):
    sampleData = []
    for i in range(0, noOfSettings):
        singleData = {}
        singleData["wifiSettings"] = "new settings_" + str(i)
        sampleData.append(singleData)
    return sampleData


def passwordGenerator(length=8):
    possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
    random_character_list = [random.choice(possible_characters) for i in range(length)]
    random_password = "".join(random_character_list)
    return random_password
