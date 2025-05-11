'''
Extract Value:
"level1": "final_value"
"user": "Metropolis"
"settings": "dark"
"products": "iPhone 15"
"events": "AI & ML"
'''
data = {
    "level1": {
        "level2": {
            "level3": {
                "level4": {
                    "level5": "final_value"
                }
            }
        }
    },
    "user": {
        "info": {
            "details": {
                "address": {
                    "city": "Metropolis"
                }
            }
        }
    },
    "settings": {
        "preferences": {
            "theme": "dark"
        }
    },
    "products": {
        "electronics": {
            "phones": {
                "iphone": "iPhone 15"
            }
        }
    },
    "events": {
        "conference": {
            "2023": {
                "schedule": {
                    "day1": "AI & ML"
                }
            }
        }
    }
}

for key, value in data.items():
    temp = value
    while True:
        try:
            temp = next(iter(temp.values()))
        except AttributeError:
            break
    print(f'"{key}": "{temp}"')
    