from dotenv import load_dotenv

# behave hooks
def before_all(context):
    load_dotenv('../.env')
