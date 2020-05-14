import requests
import json
import traceback

def getLatest(cur):
    currency="EUR" if cur=="e" else "USD" if cur=="u" else "GBP" if cur=="p" else None
    if currency is None:
        return "Valuta non valida"

    endpoint="https://api.exchangeratesapi.io/latest"
    payload={
            "base":currency
    }
    try:
        response=requests.get(endpoint,params=payload)
        if response.status_code !=200:
            return "Errore nella comunicazione con il server"
        else:
            return json.loads(response.content)
    except Exception as e:
            print(e)
            return "Errore generico"

def getHistoricValue(date):
    endpoint=f"https://api.exchangeratesapi.io/{date['year']}-{date['month']}-{date['day']}"
    response=requests.get(endpoint)
    if response.status_code!=200:
        return "Errore nella comunicazione con il server"
    else:
        return json.loads(response.content)

def getInterval(dates):
    endpoint=f"https://api.exchangeratesapi.io/history?start_at={dates['year1']}-{dates['month1']}-{dates['day1']}&end_at={dates['year2']}-{dates['month2']}-{dates['day2']}"
    try:
        response=requests.get(endpoint)
        if response.status_code!=200:
            return "Errore nella comunicazione con il server"
        else:
            return json.loads(response.content)
    except Exception as e:
        print(e)
        traceback.print_stack()
        return "Errore generico"


if __name__ == '__main__':
    print(f"""Available command:\ntype 'latest' to get lateste exchange rate\ntype 'history' to get historic esxchange rates\n type 'quit' to exit""")

    while True:
        choice=input("-->").casefold()#casefold() è un toLowerCase potenziato
        if choice=='latest':
            cur=input("Which base currency do you want?\ntype 'E' for Euro\ntype 'U' for US dollars\ntype 'P' for GB pounds\n-->").casefold()
            output=getLatest(cur)
            print(output)
        elif choice=='history':
            user_input=input("Type 'D' for a single day or 'I' for an interval\n-->").casefold()
            if user_input=='d':
                date={}
                date["year"]=input("Write the year (YYYY):\n-->")
                date["month"]=input("Write the month (MM):\n-->").zfill(2)
                date["day"]=input("Write the day (DD):\n-->").zfill(2)#aggiunge tanti zeri quanto è la lunghezza specificata fra parentesi
                output=getHistoricValue(date)
            elif user_input=='i':
                dates={}
                dates["year1"]=input("Start year (YYYY):\n-->")
                dates["month1"]=input("Start month (MM):\n-->").zfill(2)
                dates["day1"]=input("Start day (DD):\n-->").zfill(2)

                dates["year2"]=input("End year (YYYY):\n-->")
                dates["month2"]=input("End month (MM):\n-->").zfill(2)
                dates["day2"]=input("End day (DD):\n-->").zfill(2)
                output=getInterval(dates)
            else:
                print("Scelta non valida, riprova")

            print(output)

        elif choice=='quit':
            break
        else:
            print("Scelta non valida, riprova")
