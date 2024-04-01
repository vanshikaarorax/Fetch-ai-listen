import requests

url = "https://listennotes.p.rapidapi.com/api/v1/search"

querystring = {"q":"star wars","type":"episode","genre_ids":"68,82","language":"English","safe_mode":"1","sort_by_date":"0","offset":"0","only_in":"title","len_max":"10","len_min":"2","published_after":"1390190241000","published_before":"1490190241000"}

headers = {
	"X-RapidAPI-Key": "ee9cee517amsh93286852984572fp12f7adjsn1fa116b57475",
	"X-RapidAPI-Host": "listennotes.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
