
import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id=0

def init():
    global entries
    global next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        len_list=len(entries)
        if len_list >0:
            next_id=len_list+1
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    #print(entries)
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    #time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)
    entry_index=len(entries)+1
    entry = {"author": name, "text": text, "timestamp": time_string,"id": str(next_id)}
    next_id +=1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id

    for i in entries:
        if i['id']==id:
            print('true')
            index=entries.index(i)
            del entries[index]
    #print(entries)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

    return
