import main
import json

event = json.load(open('event.json'))

main.lambda_handler(event, {})
