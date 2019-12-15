import json

evan = open('eventful.json', encoding='utf-8')
evan_data = json.load(evan)

calder = open('data.json', encoding='utf-8')
calder_data = json.load(calder)

cleaned = {'events':[]}

for event in evan_data['events']:
    title = event['title']
    url = event['url']
    start_time = event['start_time']
    stop_time = event['stop_time']
    city = event['city_name']
    venue_name = event['venue_name']
    venue_address = event['venue_address']
    description = event['description']

    cleaned_event = {
        'title':title,
        'url':url,
        'start_time':start_time,
        'stop_time':stop_time,
        'city':city,
        'venue_name':venue_name,
        'venue_address':venue_address,
        'description':description
    }

    cleaned['events'].append(cleaned_event)


for event in calder_data['events']:
    title = event['title']
    url = None
    start_time = event['start']
    stop_time = event['end']
    city = None

    if event['entities']:
        venue_name = event['entities'][0]['name']
        venue_address = event['entities'][0]['formatted_address']
    else:
        venue_name = None
        venue_address = None

    description = event['description']

    cleaned_event = {
        'title':title,
        'start_time':start_time,
        'stop_time':stop_time,
        'venue_name':venue_name,
        'venue_address':venue_address,
        'description':description
    }

    cleaned['events'].append(cleaned_event)

event_data = open('eventdata.json', 'w')
json.dump(cleaned, event_data)
