
import json


from app.models import Creator, Content

def populate_db():
    try:
        # Eliminar todos los datos existentes
        Content.objects.all().delete()
        Creator.objects.all().delete()
        
        # Cargar nuevos datos
        with open('creators.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: 'creators.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: 'creators.json' file is not a valid JSON.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    
    for entry in data:
        creator = Creator.objects.create(
            name=entry['name'],
            username=entry['username'],
            rating=entry['rating'],
            platform=entry['platform']
        )
        
        Content.objects.create(
            creator=creator, 
            url=entry['content']
            )

