import xml.etree.ElementTree as ET
import sqlite3
conn = sqlite3.connect('torn-users.db')


def insert_users():
    c = conn.cursor()
    tree = ET.parse('Accounts.xml')
    root = tree.getroot()

    users = []
    for account in root.findall('Accounts'):
        id = account.find('PlayerID').text
        state = account.find('PState').text
        users.append((id, state))
    c.executemany('INSERT INTO users(ID, STATE) VALUES (?,?)', users)
    conn.commit()
    conn.close()


def get_child(parent, name):
    child = parent.find(name)
    if child is None:
        return None
    return child.text


def update_users():
    c = conn.cursor()
    tree = ET.parse('OK.xml')
    root = tree.getroot()

    users = []
    for account in root.findall('OK'):
        id = get_child(account, 'PlayerID')
        name = get_child(account, 'playername')
        age = get_child(account, 'playerage')
        role = get_child(account, 'UsrRole')
        created = get_child(account, 'InitSignUp')
        last_action = get_child(account, 'last_action')
        total_duration = get_child(account, 'total_duration')
        total_units = get_child(account, 'total_units')
        rank = get_child(account, 'rank')
        level = get_child(account, 'level')
        last_update = get_child(account, 'Last_Update')

        users.append((name, age, role, created, last_action,
                      total_duration, total_units, rank, level, last_update, id))
    c.executemany("""UPDATE users 
            set name = ?, 
                age = ?, 
                role = ?, 
                created = ?, 
                last_action = ?, 
                total_duration = ?, 
                total_units = ?, 
                rank = ?, 
                level = ?, 
                last_update = ? 
                where ID = ?""",
                  users)
    conn.commit()
    conn.close()


# insert_users()
update_users()
